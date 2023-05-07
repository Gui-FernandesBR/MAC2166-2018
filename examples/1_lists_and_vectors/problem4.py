"""Dada uma matriz real A com m linhas e n colunas e um vetor real V com n
elementos, determinar o produto de A por V."""
m = int(input("Digite o numero de linhas da matriz:"))
n = int(input("Digite o numero de colunas da matriz:"))
matriz = []
vetor = []
produto = []
for i in range(m):
    linha = []
    for j in range(n):
        elem = int(
            input(
                "Digite o elemento da matriz, LINHA=%d e COLUNA=%d :" % (i + 1, j + 1)
            )
        )
        linha.append(elem)
    matriz.append(linha)

for j in range(n):
    elem = int(input("Digite o elemento do vetor, LINHA=%d :" % (j + 1)))
    vetor.append(elem)

for k in range(m):
    soma_elem = 0
    elem = 0
    for l in range(n):
        soma_elem += matriz[k][l]
    elem = soma_elem * vetor[k]
    produto.append(elem)

print(matriz)
print(vetor)
print(produto)
acabar = input("Tecle fim para encerrar:")
