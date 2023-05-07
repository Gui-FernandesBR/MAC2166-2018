""" Problema 9.0
    Dados um número n>0 e uma sequencia c/ n numeros
    inteiros, imprimílos na ordem inversa a da leitura
"""
print("Algoritmo para imprimir uma lista na ordem inversa à de leitura")


def main():
    lista = []
    tamanho = int(input("digite o tamanho da sequencia:"))
    i = 0
    while i < tamanho:
        elem = int(input("digite o %do elemento:" % (i + 1)))
        lista.append(elem)
        i += 1
    i = i - 1
    while i > -1:
        print(lista[i], end="  ")
        i = i - 1


main()
print("")
fim = input("tecle enter para encerrar")
