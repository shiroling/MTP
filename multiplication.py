# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:48:48 2022

@author: invite
"""

from random import *

"""
#Improve your multiplication skills
print("Souhaitez-vous choisir deux nombres aléatoires à multiplier ou deux nombres au hasard ?")
print("Entrez a pour choisir aléatoirement et n'importe quelle autre chaîne de caractère sinon ")
choix = input("Choix : ")
if (choix == 'a'):
    print("Vous avez choisi de prendre deux nombres aléatoires")
else:
    print("Vous pouvez choisir vos nombres")
    nb1 = int(input("Nombre 1 : "))
    nb2 = int(input("Nombre 2 : "))
    print(nb1)
    print(nb2)
    
    resultat = int(input(nb1, "x", nb2, "= "))
    print(resultat)

n = int(input("Choisissez un nombre de chiffre pour le premier chiffre à multiplier : "))
if (n > 999999):
    print("Choisissez un nombre moins grand")
    print(n)
    """


print("Faisons des multiplications simples")

a = randint(1, 10)
b = randint(1, 10)
result = a * b
n = 0

while result != n:
   print(a, "*", b)
   n = int(input("résultat = "))
