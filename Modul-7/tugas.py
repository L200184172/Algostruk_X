## TUGAS ##

import re

# nomer 1
a = open('indonesia.txt', 'r', encoding = 'latin1')
teks1 = a.read()
a.close()

pola1 = r'\sme\w+'
nomer1 = re.findall(pola1, teks1)
print(nomer1)


# nomer 2
b = open('indonesia.txt', 'r', encoding = 'latin1')
teks2 = b.read()
b.close()

pola2 = r'di\w+'
nomer2 = re.findall(pola2, teks2)
print(nomer2)

# nomer 3
c = open('indonesia.txt', 'r', encoding = 'latin1')
teks3 = c.read()
c.close()

pola3 = r'di\s\w+'
nomer3 = re.findall(pola3, teks3)
print(nomer3)


# nomer 4
d = open('KEI.html', 'r', encoding = 'latin1')
teks4 = d.read()
d.close()

pola4 = r'(\w+)</a></td>'
nomer4 = re.findall(pola4, teks4)
print(nomer4)

e = open('KEI.html', 'r', encoding = 'latin1')
teks5 = e.read()
e.close()

pola5 = r'(\w+)</a></td>\n<td>(\d.\d+)'
tuples = re.findall(pola5, teks5)
print(tuples)

print("####################################################")
tupp = [(t[0], float(t[1]))for t in tuples]
print(tupp)
