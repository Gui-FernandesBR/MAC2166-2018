# PROBLEMA 6.0
""" Escreva uma funcao que recebe como parametro um numero inteiro k e retorna
    os coeficientes de (x+y)^n"""
print("Algoritmo para encontrar os coeficientes de (a+b)^n")


# Programa de função em cascata
def fatorial(k):
    """(int)->int
    Recebe um inteiro k e retorna o valor de k!
    pré-condição:supõe que k é um inteiro não negativo"""
    k_fat = 1
    i = 2
    while i <= k:
        k_fat = k_fat * i
        i = i + 1
    return k_fat


def binomial(m, n):
    """(int,int)->int
    recebe 2 inteiros m en retorna o valor da combinação de m,n a n.
    pré-condição: supõe que m e n são números inteiros não negativos e m>=n"""
    return fatorial(m) / (fatorial(m - n) * fatorial(n))


def main():
    """programa que lê um inteiro não negativo n e imprime os valores de
    binomial(n,0),binomial(n,1),...,binominal(n,n)"""
    n = int(input("digite o expoente da soma:"))
    i = 0
    while i < n:
        print("O %dº coeficiente de (a+b)^%d eh = %d" % (i + 1, n, binomial(n, i)))
        i += 1
        if i == n:
            print("O %dº coeficiente de (a+b)^%d eh = 1" % (i + 1, n))


main()  # chama a execução
fim = input("Digite enter para encerrar")
