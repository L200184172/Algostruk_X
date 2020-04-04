# nomer 5

class MhsTIF:
    def __init__(self, nama, nim, kota):
        self.nama = nama
        self.nim = nim
        self.kota = kota

# MAKE AN OBJECT
c0 = MhsTIF("Hapsa", 172, "Kendal")
c1 = MhsTIF("Azie", 174, "Sragen")
c2 = MhsTIF("Aulia", 70, "Boyolali")
c3 = MhsTIF("Nida", 147, "Kalimantan")
c4 = MhsTIF("Dipa", 137, "Surabaya")
c5 = MhsTIF("Sipa", 203, "Tasikmalaya")
c6 = MhsTIF("Farah", 94, "Klaten")
c7 = MhsTIF("Lukita", 103, "Solo")
c8 = MhsTIF("Naura", 159, "Palembang")
c9 = MhsTIF("Fandit", 118, "Sragen")
c10 = MhsTIF("Paidi", 157, "Bogor")

Daftar = [c0.nim, c1.nim, c2.nim, c3.nim, c4.nim, c5.nim, c6.nim, c7.nim, c8.nim, c9.nim, c10.nim]


def merge_sort(A, B):
    start = A[0]
    end = A[1]
    mid = (end - start) // 2 + start
    
    if start < mid:
        merge_sort((start, mid), B)

    if mid + 1 <= end and end - start != 1:
       merge_sort((mid + 1, end), B)

    subList(B, A[0], A[1])
    
    return B
    
    
def subList(B, start, end):
    mulai = start
    List = (end - start)//2 + start + 1
    List2 = List
    new_list = []
    
    while start < List and List2 <= end:
        first1 = B[start]
        first2 = B[List2]
        if first1 > first2:
            new_list.append(first2)
            List2 += 1
        else:
            new_list.append(first1)
            start += 1
            
    while start < List :
        new_list.append(B[start])
        start += 1

    while List2 <= end:
        new_list.append(B[List2])
        List2 += 1
        
    for i in new_list:
        B[mulai] = i
        mulai += 1
        
    return B

def mergeSort(B):
    return merge_sort((0, len(B) - 1), B)

print(Daftar)
mergeSort(Daftar)
print(Daftar)
