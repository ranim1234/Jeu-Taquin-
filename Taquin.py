import time
import copy
import numpy
from collections import deque
from Noeud import Noeud


class Taquin(object):
  
    def __init__(self, NoeudInitial):

        self.NoeudInitial = NoeudInitial
        self.final = '0,1,2,3,4,5,6,7,8'
        self.noeudsCandidats = deque([NoeudInitial])
        # set est une table haché c'est pour cela que l'etat est transformé en string
        self.NoeudsVisites = set([NoeudInitial.etatString])
        self.cheminfinal = []
        self.hauteurArbre = 0
        self.Fini = False


    def transforme(self, etatNoeud, indexEspace, Nouveauindex):
        NouveauEtat = copy.deepcopy(etatNoeud) # copier la valeur et non pas une reference
        NouveauEtat[indexEspace] = etatNoeud[Nouveauindex]
        NouveauEtat[Nouveauindex] = '0'
        return NouveauEtat


    def creerNeoudCandidat(self, monNoeud):
        etat = monNoeud.etat
        indexEspace = monNoeud.etat.index('0')
        if indexEspace % 3 != 0: # can go left
            self.ajouterNoeudCandidat(
                Noeud(self.transforme(etat, indexEspace, indexEspace-1), monNoeud))
        if indexEspace > 2: # can go up
            self.ajouterNoeudCandidat(
                Noeud(self.transforme(etat, indexEspace, indexEspace-3), monNoeud))
        if indexEspace < 6: # can go down
            self.ajouterNoeudCandidat(
                Noeud(self.transforme(etat, indexEspace, indexEspace-1), monNoeud))
        if indexEspace % 3 != 2: # can go right
            self.ajouterNoeudCandidat(
                Noeud(self.transforme(etat, indexEspace, indexEspace+1), monNoeud))

    def creerNeoudCandidatIterative(self, monNoeud):
        etat = monNoeud.etat
        indexEspace = monNoeud.etat.index('0')
        if indexEspace % 3 != 0 and self.hauteurArbre >= monNoeud.hauteur:
            self.ajouterNoeudCandidat(
                Noeud(self.transforme(etat, indexEspace, indexEspace-1), monNoeud))
        if indexEspace > 2 and self.hauteurArbre >= monNoeud.hauteur:
            self.ajouterNoeudCandidat(
                Noeud(self.transforme(etat, indexEspace, indexEspace-3), monNoeud))
        if indexEspace < 6 and self.hauteurArbre >= monNoeud.hauteur:
            self.ajouterNoeudCandidat(
                Noeud(self.transforme(etat, indexEspace, indexEspace-1), monNoeud))
        if indexEspace % 3 != 2 and self.hauteurArbre >= monNoeud.hauteur:
            self.ajouterNoeudCandidat(
                Noeud(self.transforme(etat, indexEspace, indexEspace+1), monNoeud))


    def ajouterNoeudCandidat(self, nouveau):
        if nouveau.etatString not in self.NoeudsVisites:
            self.NoeudsVisites.add(nouveau.etatString)
            self.noeudsCandidats.append(nouveau)
  

    def verifEtatFinal(self, Noeud):
        if Noeud.etatString == self.final:
            self.Fini = True
            return self.afficher(Noeud)
        else:
            return self.creerNeoudCandidat(Noeud)

 

    def rechercheLargeurDabord(self):
        while (len(self.noeudsCandidats) > 0 and not self.Fini):
            # prend le premier element dans la liste 
            NoeudCourant = self.noeudsCandidats.popleft()
            self.verifEtatFinal(NoeudCourant)
   

    def rechercheProfondeurDabord(self):
        while (len(self.noeudsCandidats) > 0 and not self.Fini):
            # prend le dernier element ajouté de liste 
            NoeudCourant = self.noeudsCandidats.pop()
            self.verifEtatFinal(NoeudCourant)


    def afficher(self, NoeudFinal):
        resultat = self.chemin(NoeudFinal)
        print('chemin:')
        print(numpy.array(resultat))
        print("Temps d'execution :",time.process_time(), 'sec')
        print('Le nombre des noeuds visités :', len(self.NoeudsVisites))
        print("l'hauteur de la solution :", NoeudFinal.hauteur)
        

   
    def chemin(self, Noeud):
        while Noeud.parent:
            self.cheminfinal.append(Noeud.etat)
            Noeud = Noeud.parent
        self.cheminfinal.reverse()
        return self.cheminfinal

        

