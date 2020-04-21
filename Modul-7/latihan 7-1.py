## halaman 65

import re

s = 'sebuah contoh kata:teh !!'
cocok = re.findall(r'kata:\w\w\w',s)

# Pernyataan-IF sesudah findall() akan memeriksa apakah pencarian berhasil
if cocok :
    print('menemukan', cocok) #'menemukan [kata:teh]' 
else :
    print('tidak menemukan')


# latihan 7.1 halaman 68
a = 'sebuah contoh kata:batagor !!'
cocok = re.findall(r'kata:\w\w\w',a)

# Pernyataan-IF sesudah findall() akan memeriksa apakah pencarian berhasil
if cocok :
    print('menemukan', cocok) #'menemukan [kata:teh]' 
else :
    print('tidak menemukan')

b = 'sebuah contoh kata:es teh !!'
cocok = re.findall(r'kata:\w\w\w',b)

# Pernyataan-IF sesudah findall() akan memeriksa apakah pencarian berhasil
if cocok :
    print('menemukan', cocok) #'menemukan [kata:teh]' 
else :
    print('tidak menemukan')
