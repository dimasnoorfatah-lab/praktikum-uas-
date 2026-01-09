class MahasiswaProcess:
    def hitung_grade(self, nilai):
        if nilai >= 85:
            return "A"
        elif nilai >= 70:
            return "B"
        elif nilai >= 60:
            return "C"
        elif nilai >= 50:
            return "D"
        else:
            return "E"
