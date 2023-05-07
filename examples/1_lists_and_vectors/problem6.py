# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 17:13:22 2018

@author: Guilherme Fernandes Alves
"""

""" PROBLEMA DE PROVA"""
""" Escreva uma funcao que recebe um inteiro n e um vetor x com n numeros
    reais e retorna sua media."""


def media(L):
    ln = len(L)
    soma = 0
    for i in range(ln):
        soma += L[i]
    return soma / ln


def leia_vetor(linha):
    L = []
    for i in range(linha):
        num = int(input("Digite o elemento da linha %d: " % (i + 1)))
        L.append(num)
    return L


def main():
    lines = int(input("Digite o numero de linhas para o vetor: "))
    L = leia_vetor(lines)
    print(L)
    print("A media dos elementos do vetor acima eh:", media(L))


main()
