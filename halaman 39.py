##if target in arrayTempatYangDicari :
##    print("targetnya terdapat dalam array itu")
##else :
##    print ("target tidak terdapat di array itu")


def cariLurus (wadah, target) :
    n = len (wadah)
    for i in range(n):
        if wadah[i] == target :
            return True
    return False

###run
##A = [3, 5, 7, 8, 4]
##cariLurus(A, 3)
