#3B
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

    def hapus(self, posisi): 
        hapus = self.head 
        if posisi == 0: 
            self.head = temp.next
            hapus = None
        for i in range(posisi-1): 
            hapus = hapus.next
            if hapus is None: 
                break
        next = hapus.next.next
        hapus.next = next


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

print("data asli : ")
linked.listprint()

print("data setelah dihapus")
linked.hapus(1)
linked.listprint()
