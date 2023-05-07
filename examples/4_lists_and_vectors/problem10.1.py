""" Problema 10.1
    Dados um numero inteiro n e uma sequencia
    com n numeros reais, conta e imprime o numero
    de vezes que cada elemento ocorre na sequencia
"""
print('Algoritmo para contar o numero de aparicoes de cada inteiro da lista na propia lista')
def main():
    n=int(input('Digite o valor de n: '))
    lista_numeros=[]
    n_ocorrencias=[]
    for i in range(n):
        x = int(input('Digite um numero: '))
        j = insira_novo(x,lista_numeros)
        if j>len(n_ocorrencias)-1:
            n_ocorrencias.append(1)
        else:
            n_ocorrencias[j]+=1
    print('>>>', lista_numeros)
    for k in range(len(lista_numeros)):
        print('O numero %d aparece %d vezes na lista'%(lista_numeros[k],n_ocorrencias[k]))

def insira_novo(item,lista):
    n=len(lista)
    for i in range(n):
        if item==lista[i]:
            return i
    lista.append(item)
    return n
main()
fim=input('tecle enter para encerrar')
