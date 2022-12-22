from orderedlinkedlist import OrderedLinkedList
import unittest
from coureur import Coureur
from resultat import Resultat
from temps import Temps
from linked_list import LinkedList


class OrderedLinkedListTest(unittest.TestCase):
    a = Coureur("tom", 12)
    b = Coureur("Pam", 20)
    c = Coureur("Pommate", 2)
    temps_c = Temps(0, 1, 0)
    temps_a = Temps(0, 10, 0)
    temps_b = Temps(0, 5, 0)
    d = Resultat(a, temps_a)
    e = Resultat(b, temps_b)
    f = Resultat(c, temps_c)
    c = OrderedLinkedList([d, e])

    def test_insert(self):
        OrderedLinkedListTest.c.insert(OrderedLinkedListTest.f)
        self.assertEqual(str(OrderedLinkedListTest.c.first()), "Pommate    : 00:01:00")


if __name__ == '__main__':
    unittest.main(verbosity=2)