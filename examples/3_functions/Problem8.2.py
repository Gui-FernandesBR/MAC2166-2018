# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 19:16:38 2018

@author: Guilherme Fernandes Alves
"""

""" PROBLEMA 8.2 """
""" Dados um numero n, n>0, e uma sequencia com n numeros inteiros, verificar
    se a sequencia eh um progressao aritmetica """

print("Algoritmo para verificar se uma sequencia eh ou nao uma p.a.")


def leia_sequencia():
    tam = int(input("Digite o tamanho da sequencia: "))
    L = []
    for i in range(tam):
        num = int(input("Digite o %dº numero da sua sequencia: " % (i + 1)))
        L.append(num)
    return L


def main():
    L = leia_sequencia()
    tam = len(L)
    razao = L[1] - L[0]
    a = 1
    b = 2
    P_A = True
    while a < tam - 1 and b < tam - 1 and P_A:
        if b > a:
            if L[b] - L[a] != razao:
                P_A = False
            a = b + 1
        else:
            if L[a] - L[b] != razao:
                P_A = False
            b = a + 1
    if P_A:
        print("A sequencia escolhida eh uma progressão aritmetica de razao", razao)
    else:
        print("A sequencia escolhida NÃO eh uma pa")


main()
fim = input("Tecle enter para acabar: ")
