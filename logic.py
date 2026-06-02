def hitung_nilai_periode(cs, pe):
    """
    Menghitung nilai per periode.
    Aturan: Class Standing (CS) 60%, Periodical Exam (PE) 40%
    """
    return (cs * 0.60) + (pe * 0.40)

def hitung_final_grade(p1, p2):
    """
    Menghitung Final Grade untuk Non-Board Subjects.
    Aturan: P1 50%, P2 50%
    """
    return (p1 * 0.50) + (p2 * 0.50)

def konversi_grade(fg):
    """
    Mengkonversi nilai angka ke Grade Huruf, Grade Point, dan Status Kelulusan.
    Berdasarkan skala Universitas Horizon Indonesia.
    """
    # Menggunakan pembulatan 2 angka desimal untuk presisi pengecekan batas
    fg_rounded = round(fg, 2)

    if fg_rounded >= 90.00:
        return "A", 4.00, "Lulus"
    elif fg_rounded >= 85.00:
        return "A-", 3.75, "Lulus"
    elif fg_rounded >= 80.00:
        return "B+", 3.50, "Lulus"
    elif fg_rounded >= 70.00:
        return "B", 3.00, "Lulus"
    elif fg_rounded >= 65.00:
        return "B-", 2.75, "Lulus"
    elif fg_rounded >= 60.00:
        return "C+", 2.50, "Lulus"
    elif fg_rounded >= 50.00:
        return "C", 2.00, "Lulus"
    else:
        return "D", 1.00, "Tidak Lulus"