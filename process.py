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