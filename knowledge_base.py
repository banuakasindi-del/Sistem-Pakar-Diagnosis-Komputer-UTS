# Basis pengetahuan sistem pakar diagnosis komputer
# Format: ID, nama kerusakan, daftar gejala yang harus cocok, solusi, tingkat keyakinan (heuristik)
RULES = [
    {
        "id": "R01", "name": "Masalah daya / PSU atau adaptor",
        "symptoms": ["tidak_menyala", "lampu_indikator_mati"],
        "solution": "Periksa stopkontak, kabel daya, sakelar PSU, adaptor, dan konektor daya. Jangan membuka PSU; mintalah teknisi menguji PSU dengan alat yang sesuai.",
        "confidence": 0.90
    },
    {
        "id": "R02", "name": "RAM longgar atau bermasalah",
        "symptoms": ["menyala_tanpa_tampilan", "bunyi_beep"],
        "solution": "Matikan komputer dan cabut daya. Jika memahami prosedur keselamatan, pasang ulang RAM; coba satu modul secara bergantian. Jika tidak yakin, serahkan kepada teknisi.",
        "confidence": 0.85
    },
    {
        "id": "R03", "name": "Gangguan monitor atau kabel display",
        "symptoms": ["komputer_menyala", "monitor_no_signal"],
        "solution": "Pastikan monitor menyala, pilih input yang benar, periksa kabel HDMI/DisplayPort/VGA, lalu coba kabel atau monitor lain.",
        "confidence": 0.88
    },
    {
        "id": "R04", "name": "Panas berlebih (overheating)",
        "symptoms": ["mati_mendadak", "kipas_bising_panas"],
        "solution": "Pastikan ventilasi tidak tertutup, bersihkan debu dengan perangkat mati, periksa kipas. Penggantian thermal paste sebaiknya dilakukan oleh orang yang kompeten.",
        "confidence": 0.86
    },
    {
        "id": "R05", "name": "Penyimpanan HDD/SSD bermasalah",
        "symptoms": ["boot_gagal", "pesan_disk_error"],
        "solution": "Utamakan pencadangan data bila drive masih terbaca. Periksa koneksi drive dan status SMART; hindari instal ulang atau format sebelum data penting diamankan.",
        "confidence": 0.90
    },
    {
        "id": "R06", "name": "Sistem operasi atau file boot rusak",
        "symptoms": ["boot_gagal", "perbaikan_otomatis"],
        "solution": "Gunakan Startup Repair atau media pemulihan sistem operasi. Cadangkan data terlebih dahulu; jangan memilih reset/format sebelum memahami dampaknya.",
        "confidence": 0.82
    },
    {
        "id": "R07", "name": "Infeksi malware atau aplikasi mencurigakan",
        "symptoms": ["komputer_lambat", "iklan_pop_up"],
        "solution": "Putuskan koneksi jaringan jika aktivitas mencurigakan berlangsung, jalankan pemindaian antivirus tepercaya, hapus aplikasi yang tidak dikenal, dan perbarui sistem.",
        "confidence": 0.80
    },
    {
        "id": "R08", "name": "Keterbatasan RAM atau beban aplikasi tinggi",
        "symptoms": ["komputer_lambat", "ram_penuh"],
        "solution": "Tutup aplikasi yang tidak diperlukan, periksa penggunaan memori di Task Manager, kurangi aplikasi startup, dan pertimbangkan peningkatan RAM yang kompatibel.",
        "confidence": 0.84
    },
    {
        "id": "R09", "name": "Gangguan jaringan / Wi-Fi",
        "symptoms": ["internet_tidak_terhubung", "perangkat_lain_terhubung"],
        "solution": "Periksa mode pesawat, Wi-Fi, router, dan driver jaringan. Coba sambungkan ulang serta jalankan pemecah masalah jaringan.",
        "confidence": 0.87
    },
    {
        "id": "R10", "name": "Keyboard atau perangkat input bermasalah",
        "symptoms": ["keyboard_tidak_berfungsi", "perangkat_lain_normal"],
        "solution": "Periksa koneksi USB/Bluetooth, baterai keyboard, port lain, dan pengaturan bahasa/input. Uji keyboard pada perangkat lain.",
        "confidence": 0.83
    }
]
