""" Problema 10.2
    Dados um numero n e uma sequencia com n numeros reais,
    determinar a maior soma de segmento da sequencia.
    Segmento de seq. eh uma subsequencia de numeros consecutivos
"""
print("Algoritmo para encontrar a fatia de maior soma em uma lista")


def main():
    n = int(input("Digite o tamanho da lista: "))
    lista = []
    for i in range(n):
        num = float(input("Digite um número para a seq: "))
        lista.append(num)
    soma_max = lista[0]
    for tan in range(1, n + 1):
        for i in range(1, n + 1):
            fatia_lista = fatia(lista, i, i + tan)
            soma_lista = soma(fatia_lista)
            if soma_lista > soma_max:
                soma_max = soma_lista
    print("A maior soma de uma fatia eh =", soma_max)


def soma(lista):
    soma_lista = 0
    for elem in lista:
        soma_lista += elem
    return soma_lista


def fatia(lista, ini, fim):
    fatia = []
    k = 0
    for i in range(ini, fim):
        fatia.append(lista[k])
        k += 1
    return fatia


main()
fim = input("tecle enter para encerrar o programa")
