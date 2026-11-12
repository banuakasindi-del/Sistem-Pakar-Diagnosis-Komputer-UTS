import streamlit as st
from knowledge_base import RULES

st.set_page_config(page_title="PakarKom - Diagnosis Komputer", page_icon="🖥️", layout="wide")
st.title("🖥️ PakarKom")
st.subheader("Sistem Pakar untuk Diagnosis Awal Kerusakan Komputer")
st.write("Jawab gejala yang dialami. Sistem akan menelusuri basis aturan menggunakan Forward Chaining.")

questions = [
    ("tidak_menyala", "Komputer sama sekali tidak menyala."),
    ("lampu_indikator_mati", "Lampu indikator komputer tidak menyala."),
    ("menyala_tanpa_tampilan", "Komputer menyala tetapi layar tidak menampilkan gambar."),
    ("bunyi_beep", "Terdengar bunyi beep saat komputer dinyalakan."),
    ("komputer_menyala", "Unit komputer tampak menyala (kipas/lampu aktif)."),
    ("monitor_no_signal", "Monitor menampilkan pesan 'No Signal'."),
    ("mati_mendadak", "Komputer sering mati atau restart mendadak."),
    ("kipas_bising_panas", "Kipas sangat bising atau komputer terasa panas."),
    ("boot_gagal", "Komputer gagal masuk ke sistem operasi."),
    ("pesan_disk_error", "Muncul pesan disk/drive error saat boot."),
    ("perbaikan_otomatis", "Muncul layar Automatic Repair/Startup Repair."),
    ("komputer_lambat", "Komputer terasa sangat lambat."),
    ("iklan_pop_up", "Muncul iklan/pop-up tidak dikenal."),
    ("ram_penuh", "Penggunaan RAM sering hampir/penuh."),
    ("internet_tidak_terhubung", "Komputer tidak dapat terhubung ke internet."),
    ("perangkat_lain_terhubung", "Perangkat lain dapat terhubung ke jaringan yang sama."),
    ("keyboard_tidak_berfungsi", "Keyboard tidak merespons."),
    ("perangkat_lain_normal", "Mouse/perangkat lain masih berfungsi normal.")
]
with st.sidebar:
    st.header("Pilih gejala")
    selected = []
    for key, label in questions:
        if st.checkbox(label, key=key):
            selected.append(key)
    st.caption("Pilih semua gejala yang benar-benar terjadi.")

c1, c2 = st.columns([2,1])
with c1:
    st.info("Tips: pilih gejala yang dapat diamati. Jika tidak yakin, jangan menebak.")
    if st.button("🔎 Diagnosis", type="primary", use_container_width=True):
        if not selected:
            st.warning("Pilih minimal satu gejala sebelum diagnosis.")
        else:
            matches = []
            for rule in RULES:
                matched = [s for s in rule["symptoms"] if s in selected]
                if len(matched) == len(rule["symptoms"]):
                    matches.append((rule, matched))
            st.session_state["result"] = (selected, matches)
with c2:
    st.metric("Jumlah aturan", len(RULES))
    st.metric("Gejala tersedia", len(questions))

if "result" in st.session_state:
    selected, matches = st.session_state["result"]
    st.divider()
    st.header("Hasil diagnosis")
    st.write("Gejala yang dipilih:", ", ".join(selected))
    if not matches:
        st.warning("Belum ada aturan yang cocok. Gejala mungkin memerlukan pemeriksaan lebih lanjut atau kombinasi aturan baru.")
    else:
        for rule, matched in matches:
            st.success(f"**{rule['name']}**")
            st.write(f"Aturan aktif: {rule['id']} — gejala cocok: {', '.join(matched)}")
            st.progress(rule["confidence"])
            st.caption(f"Skor keyakinan heuristik aturan: {rule['confidence']*100:.0f}% (bukan probabilitas klinis/terkalibrasi).")
            st.write("**Saran awal:**", rule["solution"])
    st.warning("Keselamatan: matikan dan cabut daya sebelum pemeriksaan fisik. Jangan membuka PSU atau menangani komponen bertegangan. Untuk bau terbakar, percikan, baterai menggembung, atau kerusakan fisik, hentikan penggunaan dan hubungi teknisi.")
st.divider()
st.caption("Prototipe akademik. Hasil adalah indikasi awal berdasarkan aturan yang disusun, bukan kepastian kerusakan.")
