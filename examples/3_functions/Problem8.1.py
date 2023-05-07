# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 12:05:20 2018

@author: Guilherme Fernandes Alves
"""

""" PROBLEMA 8.2 """
### Dados dois inteiros positivos, calcular o máximo divisor comum entre eles
print("Algoritmo para calcular o mdc entre dois numeros")


def mdc(a, b):
    i = 1
    mdc = 1
    while i <= a and i <= b:
        if a % i == 0 and b % i == 0:
            mdc = i
        i += 1
    return mdc


def main():
    a = int(input("Digite o primeiro numero: "))
    b = int(input("Digite o segundo  numero: "))
    print("O Maximo divisor comum entre %d e %d eh: %d" % (a, b, mdc(a, b)))


main()
print(">>> PRONTO !!!")
fim = input("Tecle enter para encerrar")
