#nomer 5
class Mahasiswa(object):
    def __init__ (self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        self.listKuliah = []

    def listKuliah(self):
        return self.listKuliah

    def hapusKuliah (self, matkul):
        self.listKuliah.remove(matkul)

    def ambilKuliah (self, matkul):
        self.listKuliah.append(matkul)
