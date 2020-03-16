#4C
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
        
    def tambahAkhir(self, b):
        self.tail.next = b
        self.tail = b


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


y = linked(70)
link.tambahAkhir(y)
link.listPrint()
