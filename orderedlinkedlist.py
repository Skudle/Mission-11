from coureur import Coureur
from resultat import Resultat
from temps import Temps
from linked_list import LinkedList


class OrderedLinkedList():

    def __init__(self, head=None):
        super().__init__()
        self.__head = head
        self.__sorted_lst = None
        self.__length = 0

    def __str__(self):
        iter1 = self.first()
        s = f"{str(self.first())}\n"
        while iter1.next() is not None:
            s += f"{str(iter1.next().value())}\n"
            iter1 = iter1.next()
        return s

    def first(self):
        return self.__head

    def length(self):
        return self.__length

    def insert(self, cargo):
        node = LinkedList.Node(cargo)
        self.__length += 1
        if self.__head is None:  # when this is the first element being added,
            self.__head = node
            node.__next = None
            return self
        else:
            if node < self.__head:
                temp = self.__head
                self.__head = node
                node.set_next(temp)
            else:
                iter_ = self.__head
                while iter_.next() is not None:
                    if node < iter_.next():
                        node.set_next(iter_.next())
                        iter_.set_next(node)
                        return self
                    else:
                        iter_ = iter_.next()
                iter_.set_next(node)
            return self


'''a = Coureur("Tom", 12)
b = Coureur("Pam", 20)
c = Coureur("Pommate", 2)
cc = Coureur("Pomme2", 2)
temps_cc = Temps(0, 0, 1)
temps_c = Temps(0, 1, 0)
temps_a = Temps(0, 10, 0)
temps_b = Temps(0, 5, 0)
d = Resultat(a, temps_a)
e = Resultat(b, temps_b)
f = Resultat(c, temps_c)
ccc = Resultat(cc, temps_cc)
c = OrderedLinkedList()

c.insert(e)
c.insert(d)
c.insert(f)
c.insert(ccc)
print(c)'''
