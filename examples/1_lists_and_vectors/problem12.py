"""17.Dada uma seqüência de n números inteiros, determinar um segmento de
soma máxima."""  # SECULO XX


def main():
    lista = []
    tam = int(input("Digite o tamanho da lista:"))
    for k in range(tam):
        num = int(input("Digite o %dº numero da lista" % (k + 1)))
        lista.append(num)
    maior_fatia = lista
    for ini in range(tam):
        for fim in range(tam - ini, tam):
            f = fatia(lista, ini, fim)
            if soma(maior_fatia) < soma(f):
                maior_fatia = lista[ini:fim]
    print("A fatia que nos dá a maior soma eh >>> ", maior_fatia)


def fatia(lista, ini, fim):
    fat = lista[ini:fim]
    return fat


def soma(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma


main()
fim = input("Tecle enter para encerrar")
