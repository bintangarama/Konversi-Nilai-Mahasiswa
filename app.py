import streamlit as st
# import function dari file logic.py
from logic import hitung_nilai_periode, hitung_final_grade, konversi_grade

# Config page
st.set_page_config(
    page_title="Grading System",
    page_icon=":material/school:",
    layout="centered",
    initial_sidebar_state="expanded"
)

# SIDEBAR : Referensi Skala Nilai
with st.sidebar:
    
    st.title(":material/list_alt: Skala Konversi Nilai")
    
    # Data untuk st.table
    skala_data = [
        {"Rentang Nilai": "90.00 - 100.00", "Grade": "A", "Point": "4.00", "Status": "Lulus"},
        {"Rentang Nilai": "85.00 - 89.99", "Grade": "A-", "Point": "3.75", "Status": "Lulus"},
        {"Rentang Nilai": "80.00 - 84.99", "Grade": "B+", "Point": "3.50", "Status": "Lulus"},
        {"Rentang Nilai": "70.00 - 79.99", "Grade": "B", "Point": "3.00", "Status": "Lulus"},
        {"Rentang Nilai": "65.00 - 69.99", "Grade": "B-", "Point": "2.75", "Status": "Lulus"},
        {"Rentang Nilai": "60.00 - 64.99", "Grade": "C+", "Point": "2.50", "Status": "Lulus"},
        {"Rentang Nilai": "50.00 - 59.99", "Grade": "C", "Point": "2.00", "Status": "Lulus"},
        {"Rentang Nilai": "0.00 - 49.99", "Grade": "D", "Point": "1.00", "Status": "Tidak Lulus"},
    ]
    st.caption("Referensi konversi nilai :")
    st.table(skala_data)
    

# MAIN PAGE: Header
st.title(":material/school: Grading System")
st.markdown("Aplikasi konversi dan kalkulasi nilai akhir mahasiswa.")
st.divider()

# MAIN PAGE: Input Nilai
st.subheader(":material/edit_document: Input Nilai Mahasiswa")
st.info("Masukkan nilai komponen Class Standing (CS) dan Periodical Exam (PE) dengan rentang 0.00 hingga 100.00", icon=":material/info:")

# form input nilai 
with st.form("grading_form", border=True):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### :material/looks_one: Periode 1 (P1)")
        cs1 = st.number_input("Class Standing (CS) - P1", min_value=0.0, max_value=100.0, step=0.1, value=None, help="Bobot Class Standing P1 adalah 60%")
        pe1 = st.number_input("Periodical Exam (PE) - P1", min_value=0.0, max_value=100.0, step=0.1, value=None, help="Bobot Periodical Exam P1 adalah 40%")
        
    with col2:
        st.markdown("### :material/looks_two: Periode 2 (P2)")
        cs2 = st.number_input("Class Standing (CS) - P2", min_value=0.0, max_value=100.0, step=0.1, value=None, help="Bobot Class Standing P2 adalah 60%")
        pe2 = st.number_input("Periodical Exam (PE) - P2", min_value=0.0, max_value=100.0, step=0.1, value=None, help="Bobot Periodical Exam P2 adalah 40%")
        
    # Tombol submit form
    submitted = st.form_submit_button("Hitung Final Grade", type="primary", use_container_width=True)

# PROSES PERHITUNGAN & TAMPILAN HASIL
if submitted:
    # LOGIKA VALIDASI FORM KOSONG 
    if cs1 is None or pe1 is None or cs2 is None or pe2 is None:
        st.warning("Mohon lengkapi seluruh nilai (CS dan PE) pada P1 dan P2 sebelum menghitung.", icon=":material/warning:")
    else:
        # Eksekusi perhitungan (memanggil logic.py)
        p1_score = hitung_nilai_periode(cs1, pe1)
        p2_score = hitung_nilai_periode(cs2, pe2)
        
        fg = hitung_final_grade(p1_score, p2_score)
        grade, point, status = konversi_grade(fg)
        
        st.divider()
        st.subheader(":material/analytics: Hasil Perhitungan & Evaluasi")
        
        result_container = st.container(border=True)
        
        with result_container:
            # Baris 1: Detail per periode
            st.markdown("#### Detail Per Periode")
            col_p1, col_p2 = st.columns(2)
            with col_p1:
                st.metric(label="Nilai Akhir P1", value=f"{p1_score:.2f}")
            with col_p2:
                st.metric(label="Nilai Akhir P2", value=f"{p2_score:.2f}")
            
            st.divider()
            
            # Baris 2: Final Grade dan Grade Huruf
            st.markdown("#### Ringkasan Evaluasi")
            col_fg, col_grade = st.columns(2)
            with col_fg:
                st.metric(label="Final Grade (Angka)", value=f"{fg:.2f}")
            with col_grade:
                st.metric(label="Grade (Huruf & Point)", value=f"{grade} ({point:.2f})")
            
            # Progress bar visualisasi nilai
            st.markdown(f"**Visualisasi Nilai Akhir ({fg:.2f}%)**")
            progress_value = min(max(fg / 100.0, 0.0), 1.0)
            st.progress(progress_value)
            
            st.write("") # Spacer
            
            # Alert kelulusan
            if status == "Lulus":
                st.success(f"**LULUS** — Selamat! Mahasiswa dinyatakan LULUS dengan indeks prestasi **{point:.2f}**.", icon=":material/check_circle:")
            else:
                st.error(f"**TIDAK LULUS** — Maaf, Mahasiswa dinyatakan TIDAK LULUS dengan indeks prestasi **{point:.2f}**.", icon=":material/cancel:")