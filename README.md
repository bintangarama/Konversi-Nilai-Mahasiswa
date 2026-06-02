# 🎓 Grading System - FICT

**🌐 Live Demo:** [https://konversi-nilai-mahasiswa.streamlit.app/](https://konversi-nilai-mahasiswa.streamlit.app/)

Aplikasi berbasis web sederhana untuk mengonversi dan mengalkulasi nilai akhir mahasiswa (**Non-Board Subjects**). Dibangun menggunakan [Streamlit](https://streamlit.io/) dengan UI yang natural dan tema _Eye-Care_ (lembut di mata).

Aplikasi ini dikonfigurasi berdasarkan skala penilaian **Universitas Horizon Indonesia**.

## ✨ Fitur

- **Input Nilai**: Mengisi nilai _Class Standing_ (CS) dan _Periodical Exam_ (PE) untuk Period 1 & 2.
- **Kalkulasi Otomatis**: Menghitung secara langsung _Final Grade_, _Letter Grade_, _Point_ IP, dan Status Kelulusan.
- **Validasi Data**: Mencegah perhitungan jika form belum lengkap.
- **Tampilan Interaktif**: Dilengkapi dengan indikator visual _progress bar_ dan metrik hasil yang bersih.
- **Eye-Care Theme**: Menggunakan warna-warna yang tidak kontras berlebihan agar nyaman dilihat dalam waktu lama.

## 🚀 Cara Menjalankan

### 1. Prasyarat

Pastikan Python sudah terinstal di komputer Anda. Anda juga memerlukan _library_ Streamlit.
Jika belum menginstal Streamlit, jalankan perintah berikut di terminal:

```bash
pip install streamlit
```

### 2. Menjalankan Aplikasi

Buka terminal (atau Command Prompt / PowerShell), arahkan ke folder proyek ini, dan jalankan perintah:

```bash
streamlit run app.py
```

### 3. Mengakses Aplikasi

Setelah perintah dijalankan, Streamlit akan secara otomatis membuka aplikasi di browser Anda (biasanya di `http://localhost:8501`).

## 📁 Struktur File

- `app.py`: File utama aplikasi yang berisi tampilan antarmuka (UI) Streamlit.
- `logic.py`: Berisi logika perhitungan nilai, persentase bobot, dan skala konversi.
- `.streamlit/config.toml`: File konfigurasi tema Streamlit untuk tampilan background dan warna aksen yang lebih natural.

---
