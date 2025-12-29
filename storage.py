import csv
import os

def simpan_saldo(saldo):
    with open("saldo.txt", "w") as file:
        file.write(str(saldo))

def baca_saldo():
    with open("saldo.txt", "r") as file:
        return int(file.read())

def buat_header_csv():
    if not os.path.exists("riwayat.csv"):
        with open("riwayat.csv", "w", newline="") as file:
            writer=csv.writer(file)
            writer.writerow(["Waktu","Jenis", "Jumlah", "Saldo"])

def simpan_riwayat_csv(waktu, jenis, jumlah, saldo):
    with open("riwayat.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([waktu, jenis, jumlah, saldo])
