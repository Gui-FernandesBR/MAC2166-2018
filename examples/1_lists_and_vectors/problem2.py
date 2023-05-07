#PROBLEMA 11.2
'''Escreva um programa que lê duas matrizes A(mxn) e B(nxp), calcula e 
imprime a matriz C=A.B (mxp)'''

def main():
    m=int(input("Digite o nº de linhas da matriz A: "))
    n=int(input("Digite o nº de colunas da matriz A:"))
    p=int(input("Digite o nº de colunas da matriz B:"))
    A=leia_matriz(m,n)
    B=leia_matriz(n,p)
    C=[]
    for k in range(m):
        linha=[]
        for i in range(p):
            soma=0
            for j in range(n):
                soma+=A[k][j]*B[j][i]
            linha.append(soma)
        C.append(linha)
    print('MATRIZ A>>>',A)
    print('MATRIZ B>>>',B)
    print('MATRIZ AxB=C>>>>>>>')
    for i in range(n):
        print("|", end='')
        for j in range (p):
            if j==p-1:
                print(C[i][j], end='')
            else:
                print(C[i][j], end=" ")
        print("|", end='')
        print('')
            
def leia_matriz(a,b):
    matriz=[]
    for i in range(a):
        linha=[]
        for j in range(b):
            num=int(input("Digite o numero da linha %d coluna %d: "%(i+1,j+1)))
            linha.append(num)
        matriz.append(linha)
    return(matriz)

main()
fim=input('tecle enter para acabar')