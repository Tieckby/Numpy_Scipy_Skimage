#coding:utf-8

import numpy as np #Importation du module Numpy(Tableau à n-dimension) meilleur en calcul scientifiques

mat1 = np.array([[1, -1], [-2, 0], [3, 4]])
print(f"\nLa matrice mat1 {mat1.shape}: {mat1}")
print(f"\nLa somme des éléments de la matrice est : {mat1.sum()}")
print(f"\nLe type de donnée est : {mat1.dtype}")

transposeMat1 = mat1.T
print(f"\nLa transposée de cette matrice est {transposeMat1.shape} : {transposeMat1}")

produit = transposeMat1.dot(mat1)
print(f"\nLe produit {produit.shape} de mat1 et son transposée est donc : {produit}")

mat1Vide = np.ones((3, 2)) #np.zeros((3, 3)) pour les 0
print(f"\nRemplissage d'une matrice {mat1Vide.shape} vide avec  des 1., de dimension : {mat1Vide.ndim}\n{mat1Vide}")

addMatrice = np.add(mat1, mat1Vide)
print(f"Addition des matrices mat1 et mat1Vide  : {addMatrice}")