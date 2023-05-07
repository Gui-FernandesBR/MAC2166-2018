'''Faça um programa em Python que leia uma lista de n (sendo n>=1) números
reais e a coloca em ordem crescente, mostrando o resultado final'''#P2-2017

def encontra_menor(A,p):
    '''Devolve o índice do menor valor em A[p], A[p+1], ..., A[n]
    (sendo n a ultima posicao da lista A)'''
    imenor=p
    for i in range(p,len(A),1):
        if A[i]<A[imenor]:
            imenor=i
    return imenor

def main():
    n=int(input('Digite n (n>0): '))
    B=[]
    for i in range (n):
        x=float(input("Digite um número:"))
        B.append(x)
    pos=0
    while pos<n:
        m=encontra_menor(B,pos)     #m seria o indice do menor valor
        menor=B[m]                  #menor eh o menor valor
        B[m]=B[pos]
        B[pos]=menor
        pos=pos+1
    print("Lista ordenada:",B)

main()