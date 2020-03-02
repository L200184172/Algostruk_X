#nomer 6
lower = 2
upper = 1000

print ("bilangan prima antara", lower, " and ", upper, ":")
for i in range (lower, upper+1):
    if i > 1:
        for k in range (2, i):
            if (i % k) == 0:
                break
        else :
            print(i)
