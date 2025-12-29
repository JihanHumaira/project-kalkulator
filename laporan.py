import csv
from utils import input_angka

def laporan_keuangan():
    total_tambah =0
    total_kurang =0
    saldo_akhir =0 
    with open("riwayat.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            jenis = row["Jenis"]
            jumlah = int(row["Jumlah"])
            saldo_akhir=int(row["Saldo"])

            if jenis == "Tambah":
                total_tambah += jumlah
            elif jenis == "Kurang":
                total_kurang += jumlah
    print("n/===Laporan Keuangan====")
    print(f"Total Pemasukan : {total_tambah}")
    print(f"Total Pengeluaran: {total_kurang}")
    print(f"Saldo Akhir : {saldo_akhir}")
    
def laporan_bulanan():
    bulan = input_angka("Masukkan Bulan (1-12): ")
    tahun = input_angka("Masukkan Tahun (contoh: 2025): ")

    total_tambah = 0
    total_kurang = 0
    saldo_akhir = 0 
    with open("riwayat.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            waktu = row["Waktu"]
            jenis = row["Jenis"]
            jumlah = int(row["Jumlah"])
            
            tahun_data=int(waktu[0:4])
            bulan_data=int(waktu[5:7])

            if tahun_data == tahun and bulan_data == bulan:
                saldo_akhir = int(row["Saldo"])

                if jenis == "Tambah":
                    total_tambah += jumlah
                elif jenis =="Kurang":
                    total_kurang += jumlah
    print(f"\n===Laporan Bulan {bulan:02d}-{tahun}=== ")
    print(f"Total Pemasukan: {total_tambah}")
    print(f"Total Pengurangan: {total_kurang}")
    print(f"Saldo Akhir: {saldo_akhir}")

def lihat_tabungan(saldo):
    print(f"SALDO SEKARANG : {saldo}")

def lihat_riwayat():
    try:
        with open("riwayat.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # skip header

            print("\n=== RIWAYAT TRANSAKSI ===")
            for row in reader:
                waktu, jenis, jumlah, saldo = row
                print(f"{waktu} | {jenis} | {jumlah} | Saldo: {saldo}")

    except FileNotFoundError:
        print("Belum ada riwayat transaksi.")
