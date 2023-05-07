"""Dada uma matriz quadrada nxn, calcular a soma de seus elementos da diagonal
secundaria"""
print(
    "Algoritmo capaz de receber uma matriz quadrada e calcular a soma dos elementos das diagonais"
)

n = n_linhas = n_colunas = int(input("digite a ordem da matriz:"))
matriz = []
for i in range(n_linhas):
    linha = []
    for j in range(n_colunas):
        num = int(input("Digite o elemento da linha %d coluna %d: " % (i + 1, j + 1)))
        linha.append(num)
    matriz.append(linha)


def soma_diag_sec(n, matriz):
    """int,(matriz) -> none
    Recebe um inteiro n, que eh a ordem da matriz quadrada e a própia matriz.
    Calcula e imprime a soma dos elementos da diagonal secundaria."""
    soma = 0
    i = n
    while i > 0:
        for j in range(n):
            soma = soma + matriz[i - 1][j]
            i = i - 1
    print("")
    print("MATRIZ>>>", matriz)
    print("")
    print("A soma dos elementos da diagonal principal é:", soma_diag_princ(n, matriz))
    print("A soma dos elementos da diagonal secundária é:", soma)


def soma_diag_princ(n, matriz):
    """int, (matriz)-> int
    Recebe uma matriz quadrada e sua ordem. Calcula e retorna a soma dos
    elementos da diagonal principal"""
    soma = 0
    i = 0
    while i < n:
        for j in range(n):
            soma += matriz[i][j]
            i += 1
    return soma


soma_diag_sec(n, matriz)
fim = input("Tecle Enter para acabar")
