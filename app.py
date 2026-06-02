import streamlit as st
# Mengimpor fungsi dari file logic.py
from logic import hitung_nilai_periode, hitung_final_grade, konversi_grade

# Konfigurasi Halaman
st.set_page_config(page_title="Grading System", page_icon="🎓")

st.title("🎓 Horizon University Grading System")
st.markdown("Aplikasi Konversi Nilai Mahasiswa **(Non-Board Subjects)** - FICT")
st.divider()

st.header("📝 Input Nilai Mahasiswa")
st.info("Masukkan nilai dengan rentang 0.00 hingga 100.00")

# Menggunakan kolom agar tampilan rapi
col1, col2 = st.columns(2)

with col1:
    st.subheader("Period 1 (P1)")
    # Batas input 0-100 langsung di-handle oleh Streamlit (mencegah bug input)
    cs1 = st.number_input("Class Standing (CS) - P1", min_value=0.0, max_value=100.0, step=0.1)
    pe1 = st.number_input("Periodical Exam (PE) - P1", min_value=0.0, max_value=100.0, step=0.1)

with col2:
    st.subheader("Period 2 (P2)")
    cs2 = st.number_input("Class Standing (CS) - P2", min_value=0.0, max_value=100.0, step=0.1)
    pe2 = st.number_input("Periodical Exam (PE) - P2", min_value=0.0, max_value=100.0, step=0.1)

st.divider()

# Tombol untuk mengeksekusi perhitungan
if st.button("Hitung Final Grade", type="primary"):
    
    # 1. Hitung nilai per periode memanggil logic.py
    p1_score = hitung_nilai_periode(cs1, pe1)
    p2_score = hitung_nilai_periode(cs2, pe2)
    
    # 2. Hitung Final Grade memanggil logic.py
    fg = hitung_final_grade(p1_score, p2_score)
    
    # 3. Konversi ke Grade, Point, dan Status memanggil logic.py
    grade, point, status = konversi_grade(fg)
    
    # --- TAMPILAN HASIL ---
    st.header("📊 Hasil Perhitungan")
    
    # Menampilkan detail P1 dan P2
    st.write(f"**Nilai P1:** {p1_score:.2f}")
    st.write(f"**Nilai P2:** {p2_score:.2f}")
    
    # Menggunakan metrik Streamlit agar UI terlihat bagus
    metrik_col1, metrik_col2, metrik_col3 = st.columns(3)
    metrik_col1.metric(label="Final Grade (Angka)", value=f"{fg:.2f}")
    metrik_col2.metric(label="Grade (Huruf & Point)", value=f"{grade} ({point:.2f})")
    
    # Memberi warna berbeda pada status lulus/gagal
    if status == "Lulus":
        metrik_col3.metric(label="Status", value=status)
        st.success("Selamat! Mahasiswa dinyatakan LULUS.")
    else:
        metrik_col3.metric(label="Status", value=status)
        st.error("Maaf, Mahasiswa dinyatakan TIDAK LULUS.")