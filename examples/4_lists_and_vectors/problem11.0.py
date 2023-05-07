""" Problema 11.0
    Escreva um programa que lê n e uma matriz A de inteiros
    de dimensão nxn, e verifica se A é simetrica
"""
print("Codigo para verificar se uma matriz eh ou nao simetrica")


def main():
    a_mat = leia_matriz()
    imprime_matriz(a_mat)
    if simetrica(a_mat):
        print(">>> A matriz é simetrica")
    else:
        print(">>> A matriz não eh simetrica")


def imprime_matriz(matriz):
    n_linhas = len(matriz)
    n_colunas = len(matriz[0])
    for i in range(n_linhas):
        for j in range(n_colunas):
            print("%d" % (matriz[i][j]), end=" ")
        print()  # pula a linha


def leia_matriz():
    n_linhas = n_colunas = int(input("Digite a ordem da matriz: "))
    matriz = []
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            num = int(
                input("Digite o elemento da linha %d coluna %d: " % (i + 1, j + 1))
            )
            linha.append(num)
        matriz.append(linha)
    return matriz


def simetrica(matriz):
    n = len(matriz)
    e_simetrica = True
    i = 0
    while i < n and e_simetrica:
        j = 0
        while j < i and e_simetrica:
            if matriz[i][j] != matriz[j][i]:
                e_simetrica = False
            j += 1
        i += 1
    return e_simetrica


main()
fim = input("tecle enter para encerrar")
