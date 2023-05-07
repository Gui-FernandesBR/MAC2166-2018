""" Problema 10.0
    Dados um número inteiro n e uma sequencia com
    n números inteiros, imprimí-los eliminando as
    repetições
"""
print("Algoritmo para imprimir elementos de uma lista eliminando repeticoes")


def main():
    n = int(input("Digite o tamanho da lista: "))
    lista_numeros = []
    for i in range(n):
        num = int(input("Digite um numero: "))
        j = indice(num, lista_numeros)
        if j == None:
            lista_numeros.append(num)
    for i in range(len(lista_numeros)):
        print(lista_numeros[i], end=" ")


def indice(item, lista):
    n = len(lista)
    for i in range(n):
        if item == lista[i]:
            return i
    return None


main()
print("")
fim = input("tecle enter para encerrar")
