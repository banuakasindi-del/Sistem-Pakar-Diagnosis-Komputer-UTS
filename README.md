# PakarKom — Sistem Pakar Diagnosis Kerusakan Komputer

## Ringkasan
Prototipe sistem pakar berbasis aturan dengan metode Forward Chaining. Basis pengetahuan berisi 10 aturan diagnosis awal. Aplikasi dibuat dengan Python dan Streamlit.

## Persyaratan
Python 3.9 atau lebih baru.

## Menjalankan aplikasi
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Menjalankan evaluasi
```bash
python evaluate.py
```
Evaluasi menjalankan lima skenario uji yang telah ditetapkan. Hasil aktual dicetak ke terminal.

## Struktur
- `app.py`: antarmuka web dan proses diagnosis.
- `knowledge_base.py`: fakta/gejala, aturan, saran penanganan.
- `evaluate.py`: lima skenario uji.
- `requirements.txt`: dependensi.

## Cara kerja
1. Pengguna memilih gejala.
2. Gejala terpilih menjadi fakta awal.
3. Mesin inferensi memeriksa apakah seluruh prasyarat suatu aturan terpenuhi.
4. Aturan yang cocok menghasilkan diagnosis dan saran.
5. Jika tidak ada aturan cocok, sistem menyatakan belum dapat menentukan diagnosis.

## Batasan dan keselamatan
Aturan merupakan pengetahuan awal yang disusun untuk prototipe akademik dan belum divalidasi teknisi. Skor keyakinan adalah nilai heuristik yang melekat pada aturan, bukan probabilitas terkalibrasi. Satu gejala dapat memiliki beberapa penyebab. Jangan membuka PSU atau membongkar perangkat saat masih terhubung listrik.

## Pengembangan
Validasi aturan bersama teknisi, tambah gejala/aturan, rekam kasus nyata yang dianonimkan, dan lakukan pengujian dengan data kasus yang lebih luas.
