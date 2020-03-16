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

    def tambahDepan(self, b):
        b.next = self.head
        self.head = b


        
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

x = linkedList(13)
linked.tambahDepan(x)
linked.listprint()
print(linked.head.data)
