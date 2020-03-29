# nomer 1

class MhsTIF(object):
    def __init__ (self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

# MAKE AN OBJECT
c0 = MhsTIF("Hafshah", "L200184172", "Kendal", 240000)
c1 = MhsTIF("Azie", "L200183174", "Sragen", 230000)
c2 = MhsTIF("Aulia", "L200183070", "Boyolali", 250000)
c3 = MhsTIF("Nida", "L200183147", "Kalimantan", 235000)
c4 = MhsTIF("Dipa", "L200184137", "Surabaya", 240000)
c5 = MhsTIF("Ainayah", "L200183203", "Tasikmalaya", 250000)
c6 = MhsTIF("Naura", "L200183159", "Palembang", 245000)
c7 = MhsTIF("Farah", "L200183094", "Klaten", 245000)
c8 = MhsTIF("Luckyta", "L200183103", "Solo", 245000)
c9 = MhsTIF("Fandit", "L200180118", "Sragen", 270000)
c10 = MhsTIF("Anggit", "L200180119", "Kalimantan", 265000)

daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def swap (A, p, q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp
    
        
def urutNIM(daftar):
    n = len(daftar)
    for i in range (n-1):
        for j in range (n-i-1):
            if daftar[j].NIM > daftar[j+1].NIM:
                swap(daftar, j, j+1)
    for i in daftar:
        print(i.nama, i.NIM)

### RESULT
##>>> urutNIM(daftar)
##Fandit L200180118
##Anggit L200180119
##Aulia L200183070
##Farah L200183094
##Luckyta L200183103
##Nida L200183147
##Naura L200183159
##Azie L200183174
##Ainayah L200183203
##Dipa L200184137
##Hafshah L200184172
