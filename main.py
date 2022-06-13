from Noeud import Noeud
from Taquin import Taquin
etatInitial = ['3', '1', '2', '4', '5', '0', '6', '7', '8']
print('Etat initial',etatInitial)
print('-------------------------------------------------------------------------------------------------------------------------')
NoeudInitial = Noeud(etatInitial)

Taquin = Taquin(NoeudInitial)


print('commencer par taper le numéro de votre choix :')
print('1-rechercheLargeurDabord')
print('2-rechercheProfondeur')
x = input() 
if x=='1':
    Taquin.rechercheLargeurDabord()
elif x =='2': 
    Taquin.rechercheProfondeurDabord()
else :
  print('echec!!!!!!!!vous devez entrer soit 1  soit 2 ')
print("fin de jeux ")
