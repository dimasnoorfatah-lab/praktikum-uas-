class MahasiswaView:
    def input_data(self):
        try:
            nim = input("Masukkan NIM Mahasiswa : ")
            nilai = int(input("Masukkan Nilai Mahasiswa : "))

            if nilai < 0 or nilai > 100:
                raise ValueError("Nilai harus antara 0 - 100")

            return nim, nilai

        except ValueError as e:
            print("Error:", e)
            return self.input_data()

    def tampilkan_tabel(self, nim, nilai, grade):
        print("\n=== DATA MAHASISWA ===")
        print("+------------+--------+-------+")
        print("| NIM        | Nilai  | Grade |")
        print("+------------+--------+-------+")
        print(f"| {nim:<10} | {nilai:<6} | {grade:^5} |")
        print("+------------+--------+-------+")
