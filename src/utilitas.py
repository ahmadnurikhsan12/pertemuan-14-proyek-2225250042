
"""Fungsi untuk memformat laporan."""


def format_laporan(statistik, ketuntasan, kkm):
    if statistik["jumlah"] == 0:
        return "Tidak ada data nilai valid.\n"

    laporan = (
        "LAPORAN REKAP NILAI MATEMATIKA\n"
        f"Jumlah data: {statistik['jumlah']}\n"
        f"KKM: {kkm:g}\n"
        f"Rata-rata: {statistik['rata_rata']:.2f}\n"
        f"Nilai minimum: {statistik['minimum']:g}\n"
        f"Nilai maksimum: {statistik['maksimum']:g}\n"
        f"Jumlah tuntas: {ketuntasan['tuntas']}\n"
        f"Jumlah belum tuntas: {ketuntasan['belum_tuntas']}\n"
    )

    return laporan
