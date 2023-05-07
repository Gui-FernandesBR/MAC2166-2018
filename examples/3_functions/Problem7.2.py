# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 10:59:19 2018

@author: Guilherme Fernandes Alves
"""
""" PROBLEMA 7.2"""
""" Dada uma seq. com n numeros inteiros positivos, determinar o fatorial de 
    cada numero da sequencia """
print("Algoritmo para calcular o fatorial de n numeros de uma seq.")


def fatorial(a):
    if a == 0:
        return 1
    else:
        return a * fatorial(a - 1)


L = []
n = int(input("Digite o valor de n: "))
for i in range(n):
    num = int(input("Digite o %dº numero da sequencia: " % (i + 1)))
    b = fatorial(num)
    print("O fatorial de", num, "eh:", b)
    L.append(b)
print(">>>", L)
fim = input("tecle enter para encerrar>>>")
