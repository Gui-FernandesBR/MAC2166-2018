""" Buscas """
''' Problema 2.0 '''
''' Faça uma fuunção que desempenha o mesmo papel das funcoes do problema1
    porem utilizando a busca binaria
    - A busca binaria consiste em ir quebrando a lista no meio e seguindo a
    busca pelo lado onde o numero pode estar. Eh evidente que a busca binaria
    so funciona corretamente com listas ordenadas em ordem crescente
'''
print('Algoritmo da busca binária, ela busca um numero em uma lista')

def troca(L,i,j):
    ''' Funcao que recebe um lista (L) e dois inteiros ("i" e "j"), troca os
    elementos das posicoes L[i] e L[j] '''
    tmp = L[i]
    L[i]= L[j]
    L[j]= tmp
    
def ordenacao_bolha(L):     ### booble-sort ###
    ''' Função que ordena uma lista utilizando a estratégia do booble-sort
        esta estratégia consiste em um puxando os maiores numeros para o
        fim da lista, de forma que uma hora esta estará ordenada. Não se assust,
        não eh algo aleatorio, eh algo pensado
    '''
    n = len(L)
    houveTroca = False
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if L[j]>L[j+1]:
                troca(L,j,j+1)
                houveTroca = True
            if not houveTroca:
               break
    return L

def busca_binaria(x,L):
    ''' Função que aplica a busca binária em uma lista'''
    n = len(L)
    inic = 0
    fim = n-1
    while inic <= fim:
        meio = (inic + fim)//2
        if x==L[meio]:
            return True
        elif x>L[meio]:
            inic = meio-1
    return False

def binaria_recursiva(x, L, inic, fim):
    ''' Função de busca_binária recursiva'''
    meio = (inic+fim)//2
    if inic > fim:
        return False
    elif x == L[meio]:
        return True
    elif x > L[meio]:
        return binaria_recursiva(x,L,meio-1,fim)
    else:
        return binaria_recursiva(x, L, inic, meio-1)
#######################################################################
tam = int(input('Digite o tamanho da lista: '))
lista = []
for i in range(tam):
    num = int(input('Digite o %do numero da lista: '%(i+1)))
    lista.append(num)
    
lista = ordenacao_bolha(lista)
x = int(input('Digite o numero que vc deseja buscar:'))
jogada = int(input('Escolha o metodo de busca (1- busca binária convencional; 2- busca bináriare recursiva): '))

if jogada == 2:
    R = binaria_recursiva(x, lista, 0, tam-1)
    if R:
        print('A busca binária diz que o numero',x,'PERTENCE à lista')
    else:
        print('A busca binária diz que o numero',x,'NÃO pertence à lista')
else:
    R = busca_binaria(x,tam-1)
    if R:
        print('A busca convencional diz que o numero',x,'PERTENCE à lista!')
    else:
        print('A busca convencional diz que o numero',x,'NÃO pertence à lista')
