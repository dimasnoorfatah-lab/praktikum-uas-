# tugas uas 

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

        class Mahasiswa:
Ini adalah deklarasi sebuah Class. Bayangkan Class sebagai sebuah "cetakan" atau "blueprint". Di sini, kamu memberi tahu Python bahwa setiap "Mahasiswa" nantinya akan memiliki pola data yang sama.

def __init__(self, nim, nama, nilai):
Ini adalah fungsi khusus yang disebut Constructor. Fungsi ini akan otomatis dijalankan saat kamu membuat objek baru dari class tersebut.
self: Ini adalah referensi ke objek itu sendiri. Gunanya agar Python tahu data mana yang sedang diproses.
nim, nama, nilai: Ini adalah parameter atau input yang harus kamu masukkan saat membuat data mahasiswa baru.

 self.nim = nim (dan seterusnya)
Di dalam bagian ini, kita menyimpan data dari parameter ke dalam "kantong" milik objek tersebut.
self.nim adalah atribut (variabel di dalam objek).
nim adalah nilai yang kamu masukkan saat membuat objek.

2. main.py 

    from process import prosesmahasiswa
from view import viewmahasiswa

def main():
    proses = prosesmahasiswa()
    view = viewmahasiswa()
    mahasisawa = None 
    while mahasiswa is None:
      mahasiswa = proses.inputmahasiswa()
      view.tampilkanmahasiswa(mahasiswa)
      if __name__ == "__main__":
         main()
         rom process import prosesmahasiswa: Mengambil logika pemrosesan data (seperti input) dari file bernama process.py.

from view import viewmahasiswa: Mengambil logika tampilan (cara menampilkan data) dari file bernama view.py.

Ini mengikuti prinsip Separation of Concerns, di mana urusan input, proses, dan tampilan dipisahkan.


Di sini, Anda membuat "instans" atau objek dari masing-masing kelas.

proses akan digunakan untuk menjalankan fungsi-fungsi penginputan.

view akan digunakan untuk menjalankan fungsi penampilan data ke layar.


mahasiswa = None: Menyiapkan variabel kosong sebagai penampung awal.

while mahasiswa is None: Program akan terus meminta input selama variabel mahasiswa masih kosong. Ini berguna untuk memastikan user benar-benar mengisi data sebelum lanjut ke tahap berikutnya.

proses.inputmahasiswa(): Memanggil fungsi di dalam file process.py untuk mengambil data (seperti Nama, NIM, Nilai) dari pengguna

   pada fungsi main() hanya akan berjalan jika file ini dieksekusi secara langsung, bukan karena di-import oleh file lain.

3. process.py 
                class DaftarMahasiswa:
    def __init__(self):
        self.list_mhs = []

    def tambah_data(self, mhs):
        self.list_mhs.append(mhs)

    def validasi_input(self, nim):
        if not nim:
            raise ValueError("NIM tidak boleh kosong!")
        
        for mhs in self.list_mhs:
            if mhs.nim == nim:
                raise ValueError(f"NIM {nim} sudah terdaftar!")

                pada __init__  Membuat "database" sementara di dalam memori komputer.

 Setiap kali Anda membuat objek dari DaftarMahasiswa, sebuah list kosong bernama list_mhs akan dibuat. List ini berfungsi sebagai wadah untuk menampung seluruh objek mahasiswa yang akan ditambahkan nanti. 

 Memasukkan data baru ke dalam list.
 Metode ini menerima parameter mhs (yang diasumsikan sebagai objek mahasiswa berisi nama, NIM, dll.) lalu menambahkannya ke urutan paling akhir di dalam list.

 pengecekan data kosong 
 Ini adalah bagian paling cerdas dari kode Anda. Bagian ini berfungsi untuk mencegah kesalahan data sebelum data tersebut disimpan
 Jika variabel nim tidak diisi (kosong), program akan sengaja menghentikan proses dan mengeluarkan pesan error. Ini memastikan tidak ada mahasiswa "tanpa identitas".

duplikat nim 
 Program akan melakukan looping (perulangan) untuk memeriksa setiap mahasiswa yang sudah ada di dalam list. Jika NIM yang diinput sama dengan NIM yang sudah tersimpan, program akan menolak data tersebut.

4. view.py 

    class viewmahasiswa:
    def tampilkan_data(self, mhs):
        print("\Data Mahasiswa:")
        print("-" *28)
        print(f"| { 'nama':<10} | { 'nim':<10} | { 'nilai':<5} |")
        print("-" *28)
        print(f"| { mhs.nama:<10} | { mhs.nim:<10} | { mhs.nilai:<5} |")
        print("-" *28)

         class viewmahasiswa: Ini adalah kelas yang mengelompokkan fungsi-fungsi yang berkaitan dengan tampilan mahasiswa.

def tampilkan_data(self, mhs): Sebuah fungsi (metode) yang menerima parameter mhs. Parameter mhs ini diharapkan adalah sebuah objek yang memiliki atribut nama, nim, dan nilai.

print("\Data Mahasiswa:")
print("-" * 28)
Bagian ini berfungsi mencetak judul dan membuat garis horizontal menggunakan karakter strip (-) sebanyak 28 kali untuk membentuk bingkai tabel.
print(f"| { 'nama':<10} | { 'nim':<10} | { 'nilai':<5} |")
Kode ini menggunakan f-string alignment:

:<10: Artinya teks akan rata kiri (left-aligned) dengan lebar kolom 10 karakter.

:<5: Artinya teks akan rata kiri dengan lebar kolom 5 karakter.

Ini memastikan bahwa meskipun nama mahasiswa panjang atau pendek, garis vertikal (|) akan tetap lurus sejajar ke bawah.

print(f"| { mhs.nama:<10} | { mhs.nim:<10} | { mhs.nilai:<5} |")
Di sini, program mengambil nilai asli dari objek mhs.

mhs.nama, mhs.nim, dan mhs.nilai dimasukkan ke dalam kolom yang sudah diatur lebarnya tadi.

Hasil Output
Jika Anda memiliki mahasiswa bernama Budi dengan NIM 123 dan nilai 90, maka kodingan ini akan menghasilkan tampilan seperti berikut di terminal:

Plaintext

Data Mahasiswa:
----------------------------
| nama       | nim        | nilai |
----------------------------
| Budi       | 123        | 90    |
----------------------------
Kesimpulan
Tujuan utama kodingan ini adalah User Experience (UX). Daripada hanya mencetak data secara berantakan, penggunaan :<10 memastikan data tersaji dalam format tabel yang profesional dan mudah dibaca oleh pengguna

link yt https://youtu.be/cy2g3R1OSv0





