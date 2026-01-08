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