# Tugas UAS
Buatlah program sederhana dengan ketentuan:
• Program harus dibuat dengan konsep modular dan OOP (pisahkan
  class data, class view, dan class process)
• Program harus meminta input dari pengguna
• Tambahkan validasi input (dapat menggunakan konsep eksepsi)
• Program menapilkan hasil (dapat berupa table view)

1. data.py
   
   class Mahasiswa:
    def __init__(self, nim, nama, nilai):
        self.nim = nim
        self.nama = nama
        self.nilai = nilai

   penjelasan :  class Mahasiswa:
Ini adalah deklarasi sebuah Class. Bayangkan Class sebagai sebuah "cetakan" atau "blueprint". Di sini, kamu memberi tahu Python bahwa setiap "Mahasiswa" nantinya akan memiliki pola data yang sama.

def __init__(self, nim, nama, nilai):
Ini adalah fungsi khusus yang disebut Constructor. Fungsi ini akan otomatis dijalankan saat kamu membuat objek baru dari class tersebut.
self: Ini adalah referensi ke objek itu sendiri. Gunanya agar Python tahu data mana yang sedang diproses.
nim, nama, nilai: Ini adalah parameter atau input yang harus kamu masukkan saat membuat data mahasiswa baru.

self.nim = nim (dan seterusnya)
Di dalam bagian ini, kita menyimpan data dari parameter ke dalam "kantong" milik objek tersebut.
self.nim adalah atribut (variabel di dalam objek).
nim adalah nilai yang kamu masukkan saat membuat objek


2. main.py
   

