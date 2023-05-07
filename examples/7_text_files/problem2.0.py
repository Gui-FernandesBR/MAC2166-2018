""" ARQUIVOS DE TEXTO """
""" PROBLEMA 2 """
""" Dado um numero inteiro impar n>0, faca uma funcao molduras_concentricas 
    (n, v1, v2) com um padrao de molduras concentricas, alternando entre v1 e
    v2 como nos exemplos """
# EXEMPLO 1:
"""
0 0 0 0 0
0 1 1 1 0
0 1 0 1 0
0 1 1 1 0
0 0 0 0 0
"""

print("Algoritmo para imprimir uma matriz com duas molduras concentricas")


def cria_matriz(n, p):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            if i == 0 or j == 0 or j == n - 1 or i == n - 1:
                linha.append(p)
            else:
                linha.append(" ")
        matriz.append(linha)
    matriz[n // 2][n // 2] = 0
    return matriz


def imprime_matriz(M):
    for i in range(len(M)):
        print("|", end=" ")
        for j in range(len(M[0])):
            print(M[i][j], end=" ")
        print("|", end="")
        print("")


def molduras_concentricas(n, v1, v2):
    M = cria_matriz(n, 0)
    for i in range(n):
        for j in range(n):
            dh = n // 2 - j
            if dh < 0:
                dh = -dh
            dv = n // 2 - i
            if dv < 0:
                dv = -dv
            if dh > dv:
                if dh % 2 == 0:
                    M[i][j] = v1
                else:
                    M[i][j] = v2
            else:
                if dv % 2 == 0:
                    M[i][j] = v1
                else:
                    M[i][j] = v2
    return M


n = int(input("Digite a ordem da matriz (numero impar): "))
v1 = int(input("Digite o elemento para a moldura 1: "))
v2 = int(input("Digite o elemento para a moldura 2: "))
imprime_matriz(molduras_concentricas(n, v1, v2))

fim = input("Tecle enter para encerrar")
