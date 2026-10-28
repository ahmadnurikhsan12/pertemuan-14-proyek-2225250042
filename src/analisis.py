
"""Fungsi untuk analisis nilai."""


def validasi_nilai(nilai):
    return (
        isinstance(nilai, (int, float))
        and 0 <= nilai <= 100
    )


def hitung_statistik(data):
    if not data:
        return {
            "jumlah": 0,
            "rata_rata": None,
            "minimum": None,
            "maksimum": None
        }

    nilai = [item["nilai"] for item in data]

    return {
        "jumlah": len(nilai),
        "rata_rata": sum(nilai) / len(nilai),
        "minimum": min(nilai),
        "maksimum": max(nilai)
    }


def tentukan_status(nilai, kkm):
    if nilai >= kkm:
        return "Tuntas"
    return "Belum tuntas"


def hitung_ketuntasan(data, kkm):
    tuntas = sum(
        1 for item in data
        if tentukan_status(item["nilai"], kkm) == "Tuntas"
    )

    return {
        "tuntas": tuntas,
        "belum_tuntas": len(data) - tuntas
    }
