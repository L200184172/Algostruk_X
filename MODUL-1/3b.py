#nomer 3b
def jumlahKonsonan(y):
    a = 0
    b = len(y)
    vokal = "aiueoAIUEO"
    for i in y: 
        if i not in vokal:
            a += 1
    return b , a
