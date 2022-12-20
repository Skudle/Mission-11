import random
import time
from coureur import Coureur
from classement import Classement
from temps import Temps
from resultat import Resultat
from orderedlinkedlist import OrderedLinkedList


class Main:
    """
    Classe principale pour la mission 11.
    @author  Kim Mens, UCLouvain
    @version 01 Décembre 2019
    """

    coureurs = [ Coureur("Alfred", 24), \
                 Coureur("Bernard", 27), \
                 Coureur("Claude", 19), \
                 Coureur("Daniel", 31),  \
                 Coureur("Emile", 25),  \
                 Coureur("Fred", 28),  \
                 Coureur("Gerard", 25) ]
    temps_Alfred = Temps(0, 0, 0)
    temps_Bernard = Temps(0, 0, 0)
    temps_Claude = Temps(0, 0, 0)
    temps_Daniel = Temps(0, 0, 0)
    temps_Emile = Temps(0, 0, 0)
    temps_Fred = Temps(0, 0, 0)
    temps_Gerard = Temps(0, 0, 0)

    result = [Resultat(Coureur("Alfred", 24), temps_Alfred), Resultat(Coureur("Bernard", 27), temps_Bernard), \
              Resultat(Coureur("Claude", 19), temps_Claude), Resultat(Coureur("Daniel", 31), temps_Daniel), \
              Resultat(Coureur("Emile", 25), temps_Emile), Resultat(Coureur("Fred", 28), temps_Fred), \
              Resultat(Coureur("Gerard", 25), temps_Gerard)]

    oll_lst = OrderedLinkedList()

    for i in result:
        oll_lst.insert(i)

    @classmethod
    def main(cls):
        # Créer un classement initialement vide pour la course
        cl = Classement()
        # Boucle infinie
        while True:
            # Choisir aléatoirement un coureur de la liste
            c = random.choice(cls.coureurs)
            # Lui assigner un temps entre 1000 et 5000 secondes
            cherche_coureur = True
            while cherche_coureur:
                for a in cls.result:
                    if a.coureur().nom() == c.nom():
                        a.temps().add_secondes(random.randint(1000, 5000))
                        cherche_coureur = False
                        break
            # Créer un résultat pour ce coureur avec ce temps
            print(a)
            # Cherche le dernier résultat de ce coureur dans le classement.
            r1 = cl.get(a.coureur().nom())
            # Imprime le classement actuel de coureur dans le classement.
            if r1 is None :
                print("  Pas encore classé")
            else:
                print("  Actuellement classé " + str(cl.get_position(c)))
                print("  Dernier temps enregistré = " + str(r1.temps()))
            # Compare son dernier résultat stocké avec son nouveau résultat
            if r1 is not None and r >= r1:
                print("  Moins bon temps, ignoré")
            else:
                print("  Nouveau temps est meilleur; sera enregistré")
                cl.remove(c)
                cl.add(r)
                print("  Maintenant classé " + str(cl.get_position(c)));
                print()
                print("CLASSEMENT:")
                print(cl)
                #print()
            # Attendre une seconde avant de recommencer la boucle while   
            time.sleep(1)


Main.main()