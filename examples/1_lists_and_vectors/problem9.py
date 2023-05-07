'''6. Dada uma matriz  A mxn, imprimir o número de linhas e o número de colunas
nulas da matriz.'''
print("Código capaz de receber uma matriz e contar o numero de linhas ou colunas nulas")
n_linhas=int(input('Digite o numero de linhas da matriz: '))
n_colunas=int(input('Digite o numero de colunas da matriz: '))
matriz=[]
for i in range(n_linhas):
    linha=[]
    for j in range(n_colunas):
        elem=int(input("Digite o elemento da linha %d coluna %d: "%(i+1,j+1)))
        linha.append(elem)
    matriz.append(linha)

linhas_nulas=0
colunas_nulas=0

for i in range(n_linhas):
    tudo_zero=True
    for j in range(n_colunas):
        if matriz[i][j]!=0:
            tudo_zero=False
    if tudo_zero:
        linhas_nulas+=1

for j in range (n_colunas):
    tudo_zero=True
    for i in range(n_linhas):
        if matriz[i][j]!=0:
            tudo_zero=False
    if tudo_zero:
        colunas_nulas+=1

print("MATRIZ>>>",matriz)
print("O Numero de linhas nulas da matriz é: ", linhas_nulas)
print('O numero de colunas nulas da matriz é: ', colunas_nulas)
fim=input("tecle enter para encerrar:")