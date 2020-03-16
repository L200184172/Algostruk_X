#3D
class linkedList(object):
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

    def tambah(self, d, posisi):
        if posisi == 1:
            d.next = self.head
            self.head = d
        if posisi == 7:
            self.tail.next = d
            self.tail = d
        if posisi == 2:
            d.next = self.head.next
            self.head.next = d
        if posisi == 3:
            d.next = self.head.next.next
            self.head.next.next = d
        if posisi == 4:
            d.next = self.head.next.next.next
            self.head.next.next.next = d
        if posisi == 5:
            d.next == self.head.next.next.next.next
            self.head.next.next.next.next = d
        if posisi == 6:
            d.next == self.head.next.next.next.next.next
            self.head.next.next.next.next.next = d
        if posisi > 7 or posisi < 0:
            raise AssertionError("Posisi harus direntang 0 sampai 7")


a = linkedList(5)
b = linkedList(7)
c = linkedList(11)
d = linkedList(17)

a.next = b
b.next = c
c.next = d

linked = LinkedList()
linked.head = a
linked.tail = d

z = linkedList(33)
linked.tambah(z,2)
linked.listprint()
print(linked.head.next.data)
