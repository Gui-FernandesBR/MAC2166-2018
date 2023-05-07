# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 11:14:18 2018

@author: Guilherme Fernandes Alves
"""

""" PROBLEMA 8.0 """
""" Dados numeros inteiros "n", "i" e "j", todos maiores do que zero, imprimir 
    em ordem crescente os n primeiros naturais que são multiplos de i, de j ou 
    de ambos. """
print("Algoritmo para te devolver os n primeiros multiplos de i ou de j")
tam = int(input("Digite o tamanho da seq. de retorno: "))
A = int(input("Escolha o primeiro valor (i): "))
B = int(input("Escolha o segundo valor (j): "))


def multiplo(N, n):
    """Funcao que diz se N eh multiplo de n"""
    if N >= n:
        if N % n == 0:
            return True
        else:
            return False
    else:
        if n % N == 0:
            return True
        else:
            return False


L = []
i = 1
while len(L) < tam:
    if multiplo(i, A) or multiplo(i, B):
        L.append(i)
    i += 1
print(L)
