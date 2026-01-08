class viewmahasiswa:
    def tampilkan_data(self, mhs):
        print("\Data Mahasiswa:")
        print("-" *28)
        print(f"| { 'nama':<10} | { 'nim':<10} | { 'nilai':<5} |")
        print("-" *28)
        print(f"| { mhs.nama:<10} | { mhs.nim:<10} | { mhs.nilai:<5} |")
        print("-" *28)
