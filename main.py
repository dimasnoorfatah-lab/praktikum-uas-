# =========================
# CLASS DATA
# =========================
class StudentData:
    def __init__(self):
        self.name = ""
        self.nim = ""
        self.score = 0

    def set_data(self, name, nim, score):
        self.name = name
        self.nim = nim
        self.score = score

    def get_name(self):
        return self.name

    def get_nim(self):
        return self.nim

    def get_score(self):
        return self.score


# =========================
# CLASS PROCESS
# =========================
class StudentProcess:
    def calculate_grade(self, score):
        if score >= 85:
            return "A"
        elif score >= 75:
            return "B"
        elif score >= 65:
            return "C"
        elif score >= 50:
            return "D"
        else:
            return "E"

    def calculate_status(self, score):
        return "LULUS" if score >= 65 else "TIDAK LULUS"


# =========================
# CLASS VIEW
# =========================
class StudentView:
    def get_input(self):
        try:
            name = input("Masukkan Nama Mahasiswa : ")
            nim = input("Masukkan NIM            : ")
            score = float(input("Masukkan Nilai (0-100)  : "))

            if name == "" or nim == "":
                raise ValueError("Nama dan NIM tidak boleh kosong")

            if score < 0 or score > 100:
                raise ValueError("Nilai harus antara 0 sampai 100")

            return name, nim, score

        except ValueError as e:
            print(f"\nInput tidak valid! ({e})")
            print("Silakan ulangi input.\n")
            return self.get_input()

    def display_result(self, name, nim, score, grade, status):
        print("\n=== DATA NILAI MAHASISWA ===")
        print("+----------------------+----------------------+")
        print("| Keterangan           | Nilai                |")
        print("+----------------------+----------------------+")
        print(f"| Nama Mahasiswa       | {name:<20} |")
        print(f"| NIM                  | {nim:<20} |")
        print(f"| Nilai                | {score:<20} |")
        print(f"| Grade                | {grade:<20} |")
        print(f"| Status               | {status:<20} |")
        print("+----------------------+----------------------+")


# =========================
# MAIN PROGRAM
# =========================
def main():
    # Inisialisasi objek
    data = StudentData()
    process = StudentProcess()
    view = StudentView()

    # Input dari user
    name, nim, score = view.get_input()

    # Simpan data
    data.set_data(name, nim, score)

    # Proses data
    grade = process.calculate_grade(data.get_score())
    status = process.calculate_status(data.get_score())

    # Tampilkan hasil
    view.display_result(
        data.get_name(),
        data.get_nim(),
        data.get_score(),
        grade,
        status
    )


# Menjalankan program
if __name__ == "__main__":
    main()
