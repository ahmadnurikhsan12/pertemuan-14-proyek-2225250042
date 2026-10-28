
"""Program utama rekap dan analisis nilai kelas."""

from pathlib import Path
from analisis import hitung_statistik, hitung_ketuntasan
from data_io import baca_data, simpan_laporan
from utilitas import format_laporan

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "nilai_contoh.txt"
OUTPUT_PATH = ROOT / "output" / "laporan.txt"
KKM = 60


def main():
    try:
        data = baca_data(DATA_PATH)
    except FileNotFoundError:
        print("File data tidak ditemukan.")
        return

    if not data:
        print("Tidak ada data nilai valid.")
        return

    statistik = hitung_statistik(data)
    ketuntasan = hitung_ketuntasan(data, KKM)
    laporan = format_laporan(statistik, ketuntasan, KKM)

    print(laporan, end="")

    try:
        simpan_laporan(laporan, OUTPUT_PATH)
    except OSError as error:
        print(f"Gagal menyimpan laporan: {error}")
        return

    print("Laporan berhasil disimpan di output/laporan.txt")


if __name__ == "__main__":
    main()
