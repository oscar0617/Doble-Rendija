# -*- coding: utf-8 -*-
"""
Created on Tue 11 15:30:48 2022
@author: Oscar Lesmes & Milton Gutierrez
"""
import math
import numpy as np
##Funciones auxiliares
def matrizPorVector(matriz, vector):
    matriz = np.array(matriz)
    vector = np.array(vector)
    producto = matriz.dot(vector)
    return producto

def cantidadDeClicks(matriz, vector, clicks):
    for i in range(len(matriz)):
        print(matriz[i])
    for i in range(clicks):
        vector = matrizPorVector(matriz, vector)
    print("-" * 2)
    return vector
##########################################

def pruebaClicks1Complejos():
    print("Usando números complejos")
    matriz = [[0, 0, 0, 0, 0, 0, 0, 0],
             [1/math.sqrt(2), 0, 0, 0, 0, 0, 0, 0],
             [1/math.sqrt(2), 0, 0, 0, 0, 0, 0, 0],
             [0, (-1+1j)/math.sqrt(6), 0, 1, 0, 0, 0, 0],
             [0, (-1-1j)/math.sqrt(6), 0, 0, 1, 0, 0, 0],
             [0, (1-1j)/math.sqrt(6), (-1+1j)/math.sqrt(6), 0, 0, 1, 0, 0],
             [0, 0, (-1-1j)/math.sqrt(6), 0, 0, 0, 1, 0],
             [0, 0, (1-1j)/math.sqrt(6), 0, 0, 0, 0, 1]]
    matriz = np.matrix(matriz)
    matriz = np.round(matriz, 3)
    vector = [6, 2, 1, 5, 3, 10, 4, 7]
    print(vector, "Valor Inicial")
    print(cantidadDeClicks(matriz, vector, 1), "Clicks = 1")

def purebaConProbabilidades():
    print("La matriz con las probabilidades es:")
    matriz = [[0, 0, 0, 0, 0, 0, 0, 0],
             [1/2, 0, 0, 0, 0, 0, 0, 0],
             [1/2, 0, 0, 0, 0, 0, 0, 0],
             [0, 1/3, 0, 1, 0, 0, 0, 0],
             [0, 1/3, 0, 0, 1, 0, 0, 0],
             [0, 1/3, 1/3, 0, 0, 1, 0, 0],
             [0, 0, 1/3, 0, 0, 0, 1, 0],
             [0, 0, 1/3, 0, 0, 0, 0, 1]]

    vector = [0, 0, 1, 0, 0, 0, 0, 0]
    print(vector, "Estado inicial")
    print(cantidadDeClicks(matriz, vector, 1), "Clicks = 1")
