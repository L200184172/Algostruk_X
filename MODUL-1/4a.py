#nomer 4 RERATA
def rerata(x):
    jumlah = 0
    for i in range (len(x)):
        jumlah += x[i]
    jumlah = jumlah / len (x)
    return jumlah
