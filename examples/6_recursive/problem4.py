'''Problema 4 - RECURSIVA'''
'''Encontrar o maior valor de uma lista'''

tam = int(input('Digite o tamanho da lista: '))
lista=[]
for i in range(tam):
    num = int(input('Digite um numero para a lista: '))
    lista.append(num)
    
def maiorinteiro_aux(L, n):
    if n==1:
        return L[0]
    else:
        m=maiorinteiro_aux(L, n-1)
        if m>L[n-1]:
            return m
        else:
            return L[n-1]

def maiorinteiro(L):
    n = len(L)
    return maiorinteiro_aux(L, n)

print('O maior valor da lista L =',lista, 'eh', maiorinteiro(lista))