
"""Fungsi untuk membaca data nilai dan menyimpan laporan."""


def baca_data(path):
    data = []

    with open(path, "r", encoding="utf-8") as file:
        for nomor, baris in enumerate(file, start=1):
            baris = baris.strip()

            if not baris:
                continue

            bagian = baris.split(",")

            if len(bagian) != 2:
                print(f"Baris {nomor} dilewati: format tidak sesuai.")
                continue

            kode = bagian[0].strip()

            try:
                nilai = float(bagian[1].strip())
            except ValueError:
                print(f"Baris {nomor} dilewati: nilai bukan angka.")
                continue

            if not kode or not 0 <= nilai <= 100:
                print(f"Baris {nomor} dilewati: data tidak valid.")
                continue

            data.append({"kode": kode, "nilai": nilai})

    return data


def simpan_laporan(teks, path):
    with open(path, "w", encoding="utf-8") as file:
        file.write(teks)
