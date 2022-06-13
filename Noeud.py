
class Noeud(object):
    def __init__(self, etat, parent=False):
        self.etatString = ','.join(etat)
        self.etat = etat
        self.parent = parent
        if parent == False:
            self.hauteur = 0
        else:
            self.hauteur = parent.hauteur+1
