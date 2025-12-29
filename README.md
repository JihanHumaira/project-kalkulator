# 📊 Aplikasi Tabungan & Laporan Keuangan (Python)
## Update
Project ini telah direfaktor menjadi struktur modular dan ditambahkan fitur laporan keuangan berbasis CSV.

## Deskripsi
Aplikasi berbasis Python untuk mencatat transaksi tabungan, menyimpan data secara permanen, serta menghasilkan laporan keuangan otomatis.  
Aplikasi ini dibuat sebagai project pembelajaran untuk melatih pengelolaan data, struktur program yang rapi, dan analisis data sederhana menggunakan file CSV.

---

## Fitur Utama
- Menambah saldo tabungan
- Mengurangi saldo tabungan
- Menyimpan saldo ke file (`saldo.txt`)
- Mencatat riwayat transaksi ke file CSV (`riwayat.csv`)
- Validasi input (mencegah input huruf dan angka negatif)
- Laporan keuangan total
- Laporan keuangan bulanan
- Struktur kode modular (multi-file)

---

## Struktur Folder
tabungan_app/
│
├── main.py # Program utama (menu)
├── utils.py # Fungsi bantuan (waktu, validasi input)
├── storage.py # Pengelolaan file (saldo & CSV)
├── transaksi.py # Logika transaksi tabungan
├── laporan.py # Laporan & tampilan data
│
├── saldo.txt # Menyimpan saldo terakhir
└── riwayat.csv # Riwayat transaksi


## Cara Menjalankan Program
1. Pastikan Python sudah terinstall
2. Siapkan file `saldo.txt` dengan isi angka awal, contoh: 200000
3. Jalankan program:
```bash
python main.py

# output
=== LAPORAN BULAN 01-2025 ===
Total Pemasukan : 150000
Total Pengeluaran: 50000
Saldo Akhir      : 300000

Teknologi yang Digunakan:
-Python 3
-CSV (data storage)
-Modular programming

Tujuan Pembelajaran
    -Project ini dibuat untuk melatih:
    -Dasar Python dan struktur program
    -File handling (TXT & CSV)
    -Validasi input
    -Analisis data sederhana
    -Penulisan kode yang terstruktur dan mudah dibaca

Catatan
    -Project ini bersifat pembelajaran dan dapat dikembangkan lebih lanjut, misalnya:
    -Export laporan ke file
    -Visualisasi data
    -Integrasi database
