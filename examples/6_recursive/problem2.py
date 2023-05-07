'''Funções Recursivas'''
'''Problema 2'''
'''Calcular a série de Fibonacci'''

print('>>>> Código para encontrar elementos da sequencia Fibonacci <<<<<')
n=int(input('Digite a posicao do elemento que vc precisa saber: ' ))
def Fibo(n):
    if n<=1:
        return n
    else:
        return Fibo(n-1) + Fibo(n-2)
    
print('A sequencia Fibonacci recebe',Fibo(n),"na posicao numero %d"%(n))