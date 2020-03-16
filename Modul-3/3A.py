#3a
class tugasLink(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
        
    def listprint(self):
        printval = self.head
        hasil = []
        while printval is not None:
            hasil.append(printval.data)
            printval = printval.next
        print(hasil)

    def cari(self, nilai):
            cek = self.head
            a = 1
            while cek is not None:
                if cek.data == nilai:
                    print("terdapat pada urutan ke-"+str(a))
                    break
                if cek.data != nilai:
                    a += 1
                    cek = cek.next

a = tugasLink(10)
b = tugasLink(20)
c = tugasLink(30)
d = tugasLink(40)

a.next = b
b.next = c
c.next = d

linked = LinkedList()
linked.head = a
linked.tail = d

print("linked list yang tersedi : ")
linked.listprint() 
print("ketik 'linked.cari(x)' untuk mengetahui urutan")





