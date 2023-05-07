"""Dada uma matriz m*n, calcule e imprima a sua matriz transposta"""

print(
    "Código capaz de receber uma matriz formada por numeros inteiros e imprimir sua transposta"
)
print("Alerta: recomenda-se utilizar apenas inteiros de um dígitos")
print("Reiterando: recomenda-se utilizar numeros entre -9 e +9")
print("")
n_linha = int(input("Digite o numero de linhas da matriz: "))
n_colunas = int(input("Digite o numero de colunas da matriz:"))
matriz = []
for i in range(n_linha):
    linha = []
    for j in range(n_colunas):
        num = int(input("Digite o elemento da linha %d coluna%d: " % (i + 1, j + 1)))
        linha.append(num)
    matriz.append(linha)

transposta = []
for l in range(n_colunas):
    linha = []
    for k in range(n_linha):
        linha.append(matriz[k][l])
    transposta.append(linha)

print("")
print("MATRIZ >>> ")
for i in range(n_linha):
    print("|", end="")
    for j in range(n_colunas):
        if j != n_colunas - 1:
            print(matriz[i][j], end=" ")
        else:
            print(matriz[i][j], end="")
    print("|", end="")
    print("")
print("")
print("TRANSPOSTA >>> ")
for i in range(n_colunas):
    print("|", end="")
    for j in range(n_linha):
        if j != n_linha - 1:
            print(transposta[i][j], end=" ")
        else:
            print(transposta[i][j], end="")
    print("|", end="")
    print("")

fim = input("Tecle Enter para acabar")
