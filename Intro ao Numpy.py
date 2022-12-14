# -*- coding: utf-8 -*-
"""Atividade 02.09.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WbTCg6RyE5KB4zHJrqy6YBddP6cGLXCT
"""

print("Davi Torelli")

"""# Introdução ao Python

## Exemplos de array
"""

import numpy as np

notas =  []
media = 0
soma = 0
contaElementos = 0

for n in range(0,5,1):
  notas.append(float(input("Entre com a nota do aluno: ")))

print(notas[1])

for x in range(0,5,1):
  soma += notas[x]
  contaElementos+=1

media = soma/contaElementos
print("A media das notas -->",media)

#utilizando numpy
#convert list to numpy array
x = np.array(notas)
print("A media com numpy -->", np.mean(notas))
print("A media com numpy array -->", x.mean())
print("A soma do vetor com numpy -->", np.sum(notas), " - ", x.sum())
print("O maior elemento -->", np.max(notas), " - ", x.max())
print("O menor elemento -->", np.min(notas), " - ", x.min())

"""Faça um programa que leia 10 números inteiros, armazene-os em um array e depois percorra o array somando todos os valores. No final, mostre a soma."""

import numpy as np
n=[]

for x in range(10):
  n.append(int(input(f"Digite o valor {x+1}: ")))
x = np.array(n)
print("O valor da soma é: ", x.sum())

"""Faça um programa que leia 5 números inteiros, armazene-os em um array e some todos os valores cujo índice seja par. Mostre a soma no final"""

import numpy as np
n = []
nPar = []

for x in range (5):
  n.append(int(input(f"Digite o valor {x+1}: ")))

for valor in n:
  if(valor % 2 == 0):
    nPar.append(valor)
x = np.array(nPar)
print(f"Numeros pares: {x}")
print(f"A soma dos números pares é {x.sum()}")

"""Faça um programa que leia 5 números inteiros, armazene-os em um array e exiba-os em ordem inversa."""

import numpy as np

num= []

for x in range (5):
  num.append(int(input(f"Digite o {x+1}º valor: ")))

x = np.array(num)
print("Array em ordem inversa: ",np.flip(x))

"""Faça um programa que leia 5 números inteiros, armazene-os em um array e mostre a soma de todos os números pares e a soma de todos os números ímpares."""

import numpy as np

num = []
numPar = []
numImpar = []

for x in range (5):
  num.append(int(input(f"Digite o {x + 1}º valor: ")))

for valor in num:
  if(valor % 2 == 0):
    numPar.append(valor)
    par = np.array(numPar)

  elif(valor % 2 != 0):
    numImpar.append(valor)
    impar = np.array(numImpar)

print(f"Soma par: {par.sum()}")
print(f"Soma impar: {impar.sum()}")