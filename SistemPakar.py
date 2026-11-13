import argparse

import Aturan as kb


def fakta_dasar(aturan):
    hasil = {a["maka"] for a in aturan}
    dasar = []
    for a in aturan:
        for j in a["jika"]:
            if j not in hasil and j not in dasar:
                dasar.append(j)
    return dasar


def tanya_user():
    print(kb.JUDUL)
    print("Jawab y/t.")
    memori = set()
    for i, f in enumerate(fakta_dasar(kb.ATURAN), 1):
        jawab = ""
        while jawab not in ("y", "t"):
            jawab = input(f"{i}. {kb.PERTANYAAN.get(f, f)} (y/t) > ").strip().lower()
        if jawab == "y":
            memori.add(f)
    return memori


def syarat_terpenuhi(aturan, memori):
    ada = [j in memori for j in aturan["jika"]]
    return all(ada) if aturan["mode"] == "dan" else any(ada)


def forward_chaining(fakta_awal):
    memori = set(fakta_awal)
    alasan = {}
    log = []
    while True:
        cocok = [r for r in kb.ATURAN
                 if syarat_terpenuhi(r, memori) and r["maka"] not in memori]
        if not cocok:
            break
        r = cocok[0]
        memori.add(r["maka"])
        alasan[r["maka"]] = r
        log.append(r)
    return memori, alasan, log


def pilih_kesimpulan(memori):
    hasil = [k for k in kb.KESIMPULAN if k in memori]
    for grup in kb.EKSKLUSIF:
        ada = [k for k in grup if k in hasil]
        for lebih in ada[1:]:
            hasil.remove(lebih)
    return hasil


def jelaskan(fakta, memori, alasan, tingkat=0):
    pad = "  " * tingkat
    r = alasan.get(fakta)
    if r is None:
        print(f"{pad}{kb.LABEL.get(fakta, fakta)}  <- fakta dari user")
        return
    print(f"{pad}{kb.LABEL.get(fakta, fakta)}  <- {r['id']} ({r['mode'].upper()}, sumber {r['sumber']})")
    for j in r["jika"]:
        if j in memori:
            jelaskan(j, memori, alasan, tingkat + 1)


def tampilkan(fakta_user):
    memori, alasan, log = forward_chaining(fakta_user)

    print("\nFakta awal:", ", ".join(sorted(fakta_user)) or "(tidak ada)")
    print()
    for n, r in enumerate(log, 1):
        print(f"Siklus {n}: {r['id']} -> {kb.LABEL.get(r['maka'], r['maka'])}")
    print(f"Siklus {len(log) + 1}: tidak ada aturan baru, berhenti")

    hasil = pilih_kesimpulan(memori)
    print()
    if not hasil:
        print("Kesimpulan: tidak ada (fakta yang diberikan belum memenuhi aturan mana pun)")
    else:
        print("Kesimpulan:")
        for k in hasil:
            print("  -", kb.LABEL.get(k, k))
        print("Alasan:")
        for k in hasil:
            jelaskan(k, memori, alasan, 1)

    print("\nSumber:")
    for kode, teks in kb.SUMBER.items():
        print(f"  {kode}: {teks}")
    print("\nCatatan:", kb.BATAS)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fakta", help="daftar fakta 'ya' dipisah koma (lewati tanya-jawab)")
    args = ap.parse_args()

    if args.fakta is not None:
        fakta = {f.strip() for f in args.fakta.split(",") if f.strip()}
        print(kb.JUDUL)
    else:
        fakta = tanya_user()
    tampilkan(fakta)


if __name__ == "__main__":
    main()