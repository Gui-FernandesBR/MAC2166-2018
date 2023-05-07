# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 16:46:57 2018
@author: Guilherme Fernandes Alves
"""
""" PROBLEMA DE PROVA """
"""Dizemos que uma matriz A com m linhas e n colunas tem banda nula k ≤ m se as
 k diagonais de A, começando a partir do canto inferior esquerdo, são nulas."""

print("Algoritmo que conta o numero de banda nulas de uma matriz")


def leia_matriz(m, n):
    """Funcao simples para receber uma matriz do usuario"""
    M = []
    for i in range(m):
        linha = []
        for j in range(n):
            a = input("Digite o elemento da linha %d coluna %d: " % (i + 1, j + 1))
            num = int(a)
            linha.append(num)
        M.append(linha)
    return M


def banda_nula(M, line):
    """Funcao que verifica se uma banda da matriz eh nula"""
    """ Nao sabe oq eh essa banda de que estou falando? Leia o primeiro 
    docstring"""
    i = line
    j = 0
    eh_nula = True
    while i < len(M) and eh_nula:
        if M[i][j] != 0:
            eh_nula = False
        j += 1
        i += 1
    return eh_nula


def imprime_matriz(matriz):
    for i in range(len(matriz)):
        print("|", end="")
        for j in range(len(matriz[0])):
            if j != len(matriz[0]) - 1:
                print(matriz[i][j], end=" ")
            else:
                print(matriz[i][j], end="")
        print("|", end="")
        print("")


def main():
    n_linhas = int(input("Digite o numero de linhas: "))
    n_colunas = int(input("Digite o numero de colunas: "))
    matriz = leia_matriz(n_linhas, n_colunas)
    k = 0
    for i in range(n_linhas - 1, -1, -1):
        if banda_nula(matriz, i):
            k += 1
        else:
            break
    imprime_matriz(matriz)
    print("A matriz acima tem banda nula", k)


main()
fim = input("Tecle enter para encerrar: ")
