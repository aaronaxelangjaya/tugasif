import csv
import os
from models import Buku


def muat_data():
    daftar_buku = []

    # Mengambil lokasi folder tempat tampil_buku.py berada
    folder = os.path.dirname(os.path.abspath(__file__))
    file_csv = os.path.join(folder, "buku.csv")

    if not os.path.exists(file_csv):
        print(f"File tidak ditemukan: {file_csv}")
        return daftar_buku

    with open(file_csv, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if not row.get("judul"):
                continue

            buku = Buku(
                row["judul"],
                row["penulis"],
                row["isbn"],
                row["status"]
            )

            daftar_buku.append(buku)

    return daftar_buku


def tampilkan_buku():
    daftar_buku = muat_data()

    if not daftar_buku:
        print("\nTidak ada data buku.\n")
        return

    print("\n" + "=" * 90)
    print("DAFTAR BUKU PERPUSTAKAAN".center(90))
    print("=" * 90)

    print(
        f"{'No':<4}"
        f"{'Judul':<30}"
        f"{'Penulis':<25}"
        f"{'ISBN':<22}"
        f"{'Status'}"
    )

    print("-" * 90)

    for i, buku in enumerate(daftar_buku, 1):
        print(
            f"{i:<4}"
            f"{buku.judul:<30}"
            f"{buku.penulis:<25}"
            f"{buku.isbn:<22}"
            f"{buku.status}"
        )

    print("-" * 90)
    print(f"Total Buku: {len(daftar_buku)}")
    print("=" * 90)


def main():
    tampilkan_buku()


if __name__ == "__main__":
    main()