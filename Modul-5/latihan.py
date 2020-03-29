# halaman 47

def swap (A, p, q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp


# halaman 48
def cariPosisiYangTerkecil (A, dariSini, sampaiSini):
    posisiYangTerkecil = dariSini
    for i in range (dariSini +1, sampaiSini):
        if A[i] < A[posisiYangTerkecil]:
            posisiYangTerkecil = i
        return posisiYangTerkecil

# buble sort
def bubleSort(A):
    n = len(A)
    for i in range (n-1):
        for j in range (n-i-1):
            if A[j] > A[j+1]:
                swap(A, j, j+1) 




A = [18, 13, 44, 25, 66, 107, 78, 89]


# selection sort
def selectionSort(A):
    n = len(A)
    for i in range (n-1):
        indexKecil = cariPosisiYangTerkecil (A, i, n)
        if indexKecil != 1 :
          swap (A, i, indexKecil)


#insertion sort
def insertionSort(A):
    n = len(A)
    for i in range (1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

A = [18, 13, 44, 25, 66, 107, 78, 89]
L = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
O = [12,6, 90, 45, 32, 74, 81, 66, 11]

### RESULT
##>>> bubleSort(L)
##>>> L
##[2, 4, 5, 10, 13, 18, 23, 29, 31, 51, 64]
##>>> selectionSort(A)
##>>> A
##[13, 18, 25, 44, 66, 78, 89, 107]
##>>> insertionSort(O)
##>>> O
##[6, 11, 12, 32, 45, 66, 74, 81, 90]

