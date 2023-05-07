""" Problema de Hanoi
    São dados um conjunto de n discos com diferentes tamanhos e três bases A, B
    e C. O problema consiste em imprimir os passos necessários para transferir
    os discos da base A para a base B, utilizando a base C como auxiliar, nunca
    colocando discos maiores sobre os menores
"""


def hanoi(n, orig, dest, aux):
    """função do problema de Hanoi, esse barato aqui eh recursivo"""
    if n == 1:
        print("Mover de", orig, "para", dest)
    else:
        hanoi(n - 1, orig, aux, dest)
        print("Mover de", orig, "para", dest)
        hanoi(n - 1, aux, dest, orig)


def main():
    n = int(input("Digite o número de discos: "))
    hanoi(n, "A", "B", "C")


main()
