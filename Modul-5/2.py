# nomer 2

A = [2, 5, 7, 17, 23, 56]
B = [4, 8, 26, 32, 40, 59]

C = A+B

def swap (A, p, q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp
    
        
def urutList(C):
    n = len(C)
    for i in range (n-1):
        for j in range (n-i-1):
            if C[j] > C[j+1]:
                swap(C, j, j+1)
    print(C)

###result
##>>> urutList(C)
##[2, 4, 5, 7, 8, 17, 23, 26, 32, 40, 56, 59]
