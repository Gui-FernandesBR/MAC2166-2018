""" Buscas """
''' Problema 1 - busca com sentinela'''
''' Faça uma função que, dada uma coleção de n>0 valores inteiros, em uma lista
    L, e um inteiro x, testa se x pertence a lista '''

print('Algoritmo para buscar um numero em uma lista')
tam = int(input("Digite o tamanho da lista: "))
L = []
for i in range(tam):
    elem = int(input("Digite o %do elemento da lista: "%(i+1)))
    L.append(elem)

jogada = int(input('Escolha o metodo de busca (1- busca convencional; 2- busca por sentinela): '))
x = int(input("Digite o numero que vc deseja buscar: "))

def pertence_normal(x,L):
    ''' função que verifica se um numero x está em uma lista L
        essa função eh pouco eficiente para listas grandes d+'''
    n = len(L)
    i = 0
    while i<n:
        if L[i]==x:
            return True
        i+=1
    return False

def pertence_sentinela(x,L):
    ''' função que busca por um numero em uma lista utilizando um metodo de
        busca por sentinela
        - O metodo de busca por sentinela consiste em pegar o numero que se
        procura e enfiar ele no fim da lista, assim basta ir procurando o
        numero pela lista e salvar '''
    n = len(L)
    i = 0
    L.append(x)
    while L[i]!= x:
        i+=1
    L.pop()     ### Retira o ultimo elemento de uma lista
    if i == n:
        return False
    else:
        return True
if jogada == 2:
    if pertence_sentinela(x,L):
        print('A busca por sentinela indicou que o numero %d APARECE na lista informada'%(x))
    else:
        print('A busca por sentinela indicou que o numero %d NÃO aparece na lista informada'%(x))        
else:
    if not pertence_normal(x,L):
        print('A busca convencional indicou que o numero %d NÃO aparece na lista informada'%(x))
    else:
        print('A busca convencional indicou que o numero %d APARECE na lista informada'%(x))

        
