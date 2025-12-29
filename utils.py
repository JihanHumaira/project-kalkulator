from datetime import datetime

def waktu_sekarang():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def input_angka(pesan):
    while True:
        try:
            angka=int(input(pesan))
            if angka <= 0:
                print("MASUKKAN ANGKA LEBIH DARI 0")
            else:
                return angka
        except ValueError:
            print("INPUT HARUS BERUPA ANGKA!")
