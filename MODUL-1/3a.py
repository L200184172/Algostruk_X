#nomer 3a
def jumlahVokal (x):
    a = 0
    b = len(x)
    vokal = "aiueoAIUEO"
    for i in x: 
        if i in vokal:
            a += 1
    return b , a
