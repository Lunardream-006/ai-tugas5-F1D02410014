JUDUL = "Kelayakan mengambil mata kuliah pada KRS"

BATAS = (
    "Pengetahuan dalam sistem ini berasal dari dua artikel jurnal (S1 dan S2) "
    "dan hanya mencakup syarat pengambilan mata kuliah, prioritas pemilihan, "
    "serta batas SKS berdasarkan IPK. Batas SKS dan prasyarat dapat berbeda "
    "pada tiap perguruan tinggi dan program studi. Hasilnya hanya saran awal "
    "untuk menyusun KRS; keputusan akhir ada pada pedoman akademik dan dosen "
    "pembimbing akademik masing-masing."
)

SUMBER = {
    "S1": "Wijana, K., Oslan, Y., & Kristanto, H. (2019). Generator Pemilihan Jadwal Kuliah "
          "dengan Teknik Penelusuran, Penyaringan dan Perangkingan. Research Fair Unisri, "
          "3(1), 419-426. https://ejurnal.unisri.ac.id/index.php/rsfu/article/view/2600/2332",
    "S2": "Febriadi, B. (2016). Sistem Pakar Berbasis Aturan dalam Bimbingan Penasehat "
          "Akademik Menggunakan Metode Forward Chaining. Digital Zone: Jurnal Teknologi "
          "Informasi dan Komunikasi, 7(1). https://doi.org/10.31849/digitalzone.v7i1.528",
}

KESIMPULAN = [
    "syarat_mk_terpenuhi", "prioritas_tinggi", "prioritas_rendah",
    "batas_sks_24", "batas_sks_22", "batas_sks_20",
    "boleh_tambah_mk_lain", "boleh_pilih_mengulang",
]

EKSKLUSIF = [["batas_sks_24", "batas_sks_22", "batas_sks_20"]]

LABEL = {
    "mk_tanpa_prasyarat": "mata kuliah tidak berprasyarat",
    "lulus_mk_prasyarat": "sudah lulus mata kuliah prasyarat",
    "sks_prasyarat_terpenuhi": "jumlah SKS yang ditempuh memenuhi prasyarat SKS",
    "mk_sesuai_semester": "mata kuliah sesuai posisi semester menurut kurikulum",
    "mk_pilihan_bebas": "mata kuliah pilihan bebas",
    "ipk_3_00": "IPK minimal 3,00",
    "ipk_2_75": "IPK minimal 2,75",
    "ipk_2_00": "IPK minimal 2,00",
    "ipk_di_bawah_2": "IPK di bawah 2,00",
    "syarat_mk_terpenuhi": "mata kuliah BOLEH diambil (syarat pengambilan terpenuhi)",
    "prioritas_tinggi": "mata kuliah PRIORITAS TINGGI untuk KRS (sesuai posisi semester)",
    "prioritas_rendah": "mata kuliah PRIORITAS RENDAH (pilihan bebas, diambil paling akhir)",
    "batas_sks_24": "batas beban studi 24 SKS",
    "batas_sks_22": "batas beban studi 22 SKS",
    "batas_sks_20": "batas beban studi 20 SKS",
    "boleh_tambah_mk_lain": "boleh menambah mata kuliah diulang, semester lebih tinggi, atau pilihan jika SKS masih tersisa",
    "boleh_pilih_mengulang": "boleh memilih mata kuliah yang diulang untuk KRS",
}

PERTANYAAN = {
    "mk_tanpa_prasyarat": "Apakah mata kuliah yang ingin diambil tidak berprasyarat?",
    "lulus_mk_prasyarat": "Apakah Anda sudah lulus mata kuliah prasyaratnya?",
    "sks_prasyarat_terpenuhi": "Apakah jumlah SKS yang sudah Anda tempuh memenuhi prasyarat SKS mata kuliah itu?",
    "mk_sesuai_semester": "Apakah mata kuliah itu berada pada posisi semester Anda menurut kurikulum?",
    "mk_pilihan_bebas": "Apakah mata kuliah itu mata kuliah pilihan bebas?",
    "ipk_3_00": "Apakah IPK Anda minimal 3,00?",
    "ipk_2_75": "Apakah IPK Anda minimal 2,75?",
    "ipk_2_00": "Apakah IPK Anda minimal 2,00?",
    "ipk_di_bawah_2": "Apakah IPK Anda di bawah 2,00?",
}

ATURAN = [
    {"id": "R1", "mode": "atau", "jika": ["mk_tanpa_prasyarat", "lulus_mk_prasyarat", "sks_prasyarat_terpenuhi"],
     "maka": "syarat_mk_terpenuhi", "sumber": "S1"},
    {"id": "R2", "mode": "dan", "jika": ["syarat_mk_terpenuhi", "mk_sesuai_semester"],
     "maka": "prioritas_tinggi", "sumber": "S1"},
    {"id": "R3", "mode": "dan", "jika": ["syarat_mk_terpenuhi", "mk_pilihan_bebas"],
     "maka": "prioritas_rendah", "sumber": "S1"},
    {"id": "R4", "mode": "dan", "jika": ["ipk_3_00"],
     "maka": "batas_sks_24", "sumber": "S2"},
    {"id": "R5", "mode": "dan", "jika": ["ipk_2_75"],
     "maka": "batas_sks_22", "sumber": "S2"},
    {"id": "R6", "mode": "dan", "jika": ["ipk_2_00"],
     "maka": "batas_sks_20", "sumber": "S2"},
    {"id": "R7", "mode": "atau", "jika": ["ipk_3_00", "ipk_2_75", "ipk_2_00"],
     "maka": "boleh_tambah_mk_lain", "sumber": "S2"},
    {"id": "R8", "mode": "dan", "jika": ["ipk_di_bawah_2"],
     "maka": "boleh_pilih_mengulang", "sumber": "S2"},
]