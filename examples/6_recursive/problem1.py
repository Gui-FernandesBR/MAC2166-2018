'''Funções Recursivas'''
'''Problema 1'''
'''Calcular o fatorial de um numero'''

print("Código que calcula o fatorial de um numero de maneira recursiva")
n = int(input('Digite o numero para o qual se deseja calcular o fatorial: '))
def fatorial(n):
    if n==0:
        return 1
    else:
        return n*fatorial(n-1)
print('O valor de %d fatorial é:'%(n), fatorial(n))