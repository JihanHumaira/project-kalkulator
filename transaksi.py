from utils import input_angka, waktu_sekarang
from storage import simpan_saldo, simpan_riwayat_csv

def tambah_tabungan(saldo):
    tambah=input_angka("Masukkan Jumlah Tabungan: ")
    saldo=saldo+tambah
    simpan_saldo(saldo)

    waktu=waktu_sekarang()
    simpan_riwayat_csv(waktu, "Tambah", tambah, saldo)
    print(f"SALDO SEKARANG: {saldo}")
    return saldo

def kurang_tabungan(saldo):
    kurang=input_angka("Masukkan Kurang Tabungan: ")
    if kurang>saldo:
        print("SALDO TIDAK CUKUP!")
    else:
        saldo=saldo-kurang
        simpan_saldo(saldo)

        waktu=waktu_sekarang()
        simpan_riwayat_csv(waktu, "Kurang", kurang, saldo)
     
        print(f"SALDO SEKARANG: {saldo}")
    return saldo