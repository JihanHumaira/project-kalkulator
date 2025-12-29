from utils import waktu_sekarang, input_angka

from storage import (
    simpan_saldo,
    baca_saldo,
    buat_header_csv,
    simpan_riwayat_csv
)
from transaksi import tambah_tabungan, kurang_tabungan
from laporan import (
    lihat_tabungan,
    lihat_riwayat,
    laporan_keuangan,
    laporan_bulanan)

saldo=baca_saldo()
buat_header_csv()
while True:
    print("== Program Tabungan ==")
    print("1. Tambah Saldo")
    print("2. Kurangi Saldo")
    print("3. Lihat Saldo")
    print("4. Lihat Riwayat Transaksi")
    print("5. Lihat Laporan Keuangan")
    print("6. Lihat Laporan Keuangan Bulanan")
    print("7. Keluar")
    pilihan = input("Pilih Menu (1/2/3/4/5/6/7): ")
    
    if pilihan == "1":
        saldo=tambah_tabungan(saldo)
    elif pilihan =="2":
        saldo=kurang_tabungan(saldo)
    elif pilihan =="3":
        lihat_tabungan(saldo)
    elif pilihan =="4":
        lihat_riwayat()
    elif pilihan =="5":
        laporan_keuangan()
    elif pilihan =="6":
        laporan_bulanan()
    elif pilihan =="7":
        print("PROGRAM SELESAI!")
        break
    else:
        print("INVALID!!!")