from orderedlinkedlist import OrderedLinkedList
from coureur import Coureur
from resultat import Resultat
from temps import Temps
from linked_list import LinkedList


class Classement():
    """
    Une implémentation primitive de classement, non ordonnée et de capacité fixe.
    @author Kim Mens
    @version 01 Décembre 2019
    """

    __maxcapacity = 10

    def __init__(self, oll=OrderedLinkedList()):
        super().__init__()
        """
        @pre: -
        @post: un classement vide de taille 0 a été créé
        """
        self.__oll = oll  # dictionnaire de résultats actuelle (clé = coureur; valeur = résultat)

    def size(self):
        """
        Méthode accesseur.
        Retourne la taille de ce classement.
        @pre:  -
        @post: Le nombre de résultats actuellement stockés dans ce classement a été retourné.
        """
        return self.oll().length()

    def oll(self):
        return self.__oll

    def add(self, r):
        """
        Ajoute un résultat r dans ce classement.
        @pre:  r est une instance de la classe Resultat
        @post: Le résultat r a été inséré selon l'ordre du classement.
               En cas d'ex-aequo, r est inséré après les autres résultats de même ordre.
        ATTENTION : L'implémentation actuelle ne respecte pas encore la post-condition!
                    Le résultat est simplement ajouté à la dictionnaire, sans tenir compte de l'ordre.
                    Une dictionnaire ne donne pas de garanties sur l'ordre des éléments.
        """
        if self.size() >= self.__maxcapacity:
            raise ValueError("Capacity of classement exceeded")
        else:
            self.oll().insert(r)

    def get(self,c):
        """
        Retourne le résultat d'un coureur donné.
        @pre c est un Coureur
        @post retourne le premier (meilleur) Resultat r du coureur c dans le
              classement. Retourne None si le coureur ne figure pas (encore)
              dans le classement.
        """
        iter1 = self.oll().first()
        if iter1 is None:
            return None
        while iter1.next() is not None:
            if iter1.value().coureur().nom() == c.nom():
                return iter1.value()
            iter1 = iter1.next()
        if iter1.value().coureur().nom() == c.nom():
            return iter1.value()
        return None

    def get_position(self,c):
        """
        Retourne la meilleure position d'un coureur dans ce classement.
        @pre c est un Coureur
        @post retourne un entier représentant la position du coureur c dans ce classement,
              à partir de 1 pour la tête de ce classement. Si le coureur figure plusieurs fois
              dans le classement, la première (meilleure) position est retournée.
              Retourne -1 si le coureur ne figure pas dans le classement.
        ATTENTION : L'implémentation actuelle ne respecte pas encore la post-condition!
                    Etant donné que la dictionnaire de résultats ne connaît pas de position,
                    pour le moment cette méthode retourne toujours "***position inconnue***".
                    A vous de la corriger en utilisant une liste chaînée ordonnée
                    comme structure de données, plutôt qu'une simple dictionnaire.
        """
        iter1 = self.oll().first()
        position = 0
        while iter1.next() is not None:
            position += 1
            if iter1.value().coureur().nom() == c.nom():
                return position
            iter1 = iter1.next()
        if iter1.value().coureur().nom() == c.nom():
            position += 1
            return position
        return -1

    def remove(self,c):
        """
        Retire un résultat du classement.
        @pre  c est un Coureur
        @post retire le premier (meilleur) résultat pour le coureur c du classement.
              c est comparé au sens de __eq__. Retourne c si un résultat a été retiré,
              of False si c n'est pas trouvé dans la liste.
        """
        iter1 = self.oll().first()
        previous_iter1 = self.oll().first()
        if iter1 is None:
            return None
        while iter1.next() is not None:
            if iter1.value().coureur().nom() != c:
                previous_iter1 = iter1
                iter1 = iter1.next()
            else:
                if self.oll().first().value().coureur().nom() == c:
                    self.oll().remove_first()
                    break
                previous_iter1.set_next(iter1.next())
                break
        previous_iter1.set_next(iter1.next())

    def __str__(self):
        """
        Méthode magique
        Retourne une représentation string de cet objet.
        @pre:  -
        @post: Retourne une représentation de ce classement sous forme d'un string,
               avec une ligne par résultat.
        """
        s = ""
        iter1 = self.oll().first()
        while iter1.next() is not None:
            s += "  " + str(self.get_position(iter1.value().coureur())) + " > " + str(iter1.value().temps()) + "\n"
            iter1 = iter1.next()
        s += "  " + str(self.get_position(iter1.value().coureur())) + " > " + str(iter1.value().temps()) + "\n"
        return s


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
z = Classement(c)
z.add(ccc)
print(z)'''
