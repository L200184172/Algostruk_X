# nomer 6

class MhsTIF(object):
    def __init__ (self, nama, NIM, kota):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        
    def __str__ (self) :
        s = self.nama + " " + str(self.NIM) + " " + self.kotaTinggal
        return s

    def getNim(self) :
        return self.NIM
    

# MAKE AN OBJECT
c0 = MhsTIF("Hafshah", 172, "Kendal")
c1 = MhsTIF("Azie", 174, "Sragen")
c2 = MhsTIF("Aulia", 70, "Boyolali")
c3 = MhsTIF("Nida", 147, "Kalimantan")
c4 = MhsTIF("Dipa", 137, "Surabaya")
c5 = MhsTIF("Ainayah", 203, "Tasikmalaya")
c6 = MhsTIF("Naura", 159, "Palembang")
c7 = MhsTIF("Farah", 94, "Klaten")
c8 = MhsTIF("Luckyta", 103, "Solo")
c9 = MhsTIF("Fandit", 118, "Sragen")
c10 = MhsTIF("Paidi", 157, "Bogor")

Daftar = [c0.NIM, c1.NIM, c2.NIM, c3.NIM, c4.NIM, c5.NIM, c6.NIM, c7.NIM, c8.NIM, c9.NIM, c10.NIM]


# Quick Sort Baru
def quickSort(L, ascending = True): 
    QShelp(L, 0, len(L), ascending)
    
def QShelp(L, low, high, ascending = True): 
    result = 0
    if low < high: 
        pivot_location, result = Partition(L, low, high, ascending)  
        result += QShelp(L, low, pivot_location, ascending)  
        result += QShelp(L, pivot_location + 1, high, ascending)
    return result


def Partition(L, low, high, ascending = True):
    result = 0 
    pivot, pidx = mot(L, low, high)
    L[low], L[pidx] = L[pidx], L[low]
    i = low + 1
    for j in range(low + 1, high, 1):
        result += 1
        if (ascending and L[j] < pivot) or (not ascending and L[j] > pivot):
            L[i], L[j] = L[j], L[i]  
            i += 1
    L[low], L[i - 1] = L[i - 1], L[low] 
    return i - 1, result


# Median Of Three
def mot(L, low, high):
    mid = (low + high - 1) // 2
    a = L[low]
    b = L[mid]
    c = L[high - 1]
    if a <= b <= c:
        return b, mid
    if c <= b <= a:
        return b, mid
    if a <= c <= b:
        return c, high - 1
    if b <= c <= a:
        return c, high - 1
    return a, low

print(Daftar)
quickSort(Daftar)
print(Daftar)
