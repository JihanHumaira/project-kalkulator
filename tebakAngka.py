import random

angka_rahasia = random.randint(1, 10)

print("Selamat datang di Game Tebak Angka!")
print("Aku sudah memilih angka dari 1 sampai 10.")
print("Coba tebak ya!")

tebakan = int(input("Masukkan tebakan kamu: "))

if tebakan == angka_rahasia:
    print("Keren! Kamu benar!")
else:
    print("Salah! Angka yang benar adalah:", angka_rahasia)
