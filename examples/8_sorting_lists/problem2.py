""" ORDENAÇÃO DE LISTAS """
""" Dada uma lista L com n>0 numeros inteiros no intervalo de 0 a 255, faça uma
    função para ordenar os seus elementos em ordem crescente """


def ordenação_por_contagem(L):
    n = len(L)
    c = [0] * 256
    for i in range(0, n):
        c[L[0]] += 1
        i = 0
        for k in range(0, c[k]):
            L[i] = k
            i += 1
