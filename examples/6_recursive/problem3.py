"""Função recursiva"""
"""Problema 3"""
"""Calcular x elevado a n inteiro positivo"""
print("Algoritmo que calcula x elevado a n positivo de maneria recursiva")
x = int(input("Digite a base da exponecial:"))
n = int(input("Agora digite o expoente: "))


def potencia(x, n):
    if n == 0:
        return 1
    else:
        return x * potencia(x, n - 1)
        # n=n-1


print("O valor de %d elevado a %d eh" % (x, n), potencia(x, n))
fim = input("Tecle enter para encerrar")
