#4B
class linked(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        
    def listPrint(self):
        isi = self.head
        tempat = []
        while isi is not None:
            tempat.append(isi.data)
            isi = isi.next
        print(tempat)
        
    def tambahDepan(self, a):
        a.next = self.head
        self.head = a


a = linked(10)
b = linked(20)
c = linked(30)
d = linked(40)

a.next = b
b.next = c
c.next = d


link = LinkedList()
link.head = a
link.tail = d

print("Hasil nomor 2")
x = linked(60)
link.tambahDepan(x)
link.listPrint()
