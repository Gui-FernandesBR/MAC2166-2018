"""
Created on Wed Jun  6 21:40:39 2018

@author: Guilherme Fernandes Alves
"""
""" OPERACAO DE LISTAS """
""" PROBLEMA 1 - caso do baralho """
""" Dada uma lista com n>0 numeros inteiros, faca uma funcao para ordenar os
    seus elementos em ordem crescente """
### Basicamente, vamos definir varias funcoes que fazem a mesma coisa ###


def troca(L, i, j):
    """Funcao que recebe um lista (L) e dois inteiros ("i" e "j"), troca os
    elementos das posicoes L[i] e L[j]"""
    tmp = L[i]
    L[i] = L[j]
    L[j] = tmp


def indice_maior(L, n):
    """Funcao que recebe uma lista e diz qual o indice do maior elemento"""
    imax = 0
    for i in range(1, n):
        if L[i] > L[imax]:
            imax = i
    return imax


def ordenacao_insercao(L):  ### insert-sort ###
    n = len(L)
    for i in range(0, n - 1):
        x = L[i + 1]
        j = i
        while j >= 0 and L[j] > x:
            L[j + 1] = L[j]
            j -= 1
            L[j + 1] = x
    return L


def ordenacao_selecao(L):  ### select-sort ###
    n = len(L)
    for tam in range(n, 1, -1):
        imax = indice_maior(L, tam)
        troca(L, imax, tam - 1)
    return L


def ordenacao_bolha(L):  ### booble-sort ###
    n = len(L)
    houveTroca = False
    for i in range(n - 1, 0, -1):
        for j in range(0, i):
            if L[j] > L[j + 1]:
                troca(L, j, j + 1)
                houveTroca = True
            if not houveTroca:
                break
    return L


print("Algoritmo para colocar uma lista em ordem crescente")
print("Este algoritmo possui 3 maneiras diferentes de realizar a tarefa acima")
print(">>> Escolha qual método você quer usar >>>")
jogada = int(
    input("1-ordenacao por insercao; 2-ordenacao por selecao ou 3-ordenacao_bolha : ")
)

tam = int(input("Digite o tamanho da lista: "))
lista = []
for i in range(tam):
    num = int(input("Digite o %do elemento da lista: " % (i + 1)))
    lista.append(num)
lista1 = lista[:]
final = False
while not final:
    if jogada == 1:
        M = ordenacao_insercao(lista)
        print("A lista L=", lista1, "em ordem crescente fica:")
        print(">>>>>", M)
        fim = input("tecle enter para encerrar")
        final = True
    elif jogada == 2 and not final:
        M = ordenacao_selecao(lista)
        print("A lista L=", lista1, "em ordem crescente fica:")
        print(M)
        print("tecle enter para encerrar")
        final = True
    elif jogada == 3 and not final:
        M = ordenacao_bolha(lista)
        print("A lista L=", lista1, "em ordem crescente fica:")
        print(M)
        print("tecle enter para encerrar")
        final = True
    elif not final:
        jogada = int(input("Digitou errado, otario!!!"))
