''' Problema 2.2
    Calcule n elevado a k
'''
print('Algoritmo que calcula n elevado a k')
n=int(input("digite o valor de n: "))
k=int(input("digite o valor de k: "))
pot=1
i=0
while i<k:
    pot=pot*n
    i=i+1
print("o valor de %d elevado a %d eh %d"%(n,k,pot))
fim=input("tecle fim para acabar")
