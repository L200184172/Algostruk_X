#4a
class linked(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def cetakDepan():
        a.next = b
        b.next = c
        c.next = d
        print (a.data)
        print (a.next.data)
        print (a.next.next.data)
        print (a.next.next.next.data)

    def cetakBelakang():
        d.prev = c
        c.prev = b
        b.prev = a
        print (d.data)
        print (d.prev.data)
        print (d.prev.prev.data)
        print (d.prev.prev.prev.data)


            
a = linked(10)
b = linked(20)
c = linked(30)
d = linked(40)

print("cetak dari depan")
linked.cetakDepan()

print("cetak dari belakang")
linked.cetakBelakang()


