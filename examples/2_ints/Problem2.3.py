''' Problema 2.3
    Calcular n fatorial
'''
print('Algoritmo para calcular n fatorial')
n=int(input("Digite o valor de n: "))
fat=1
i=2
while i<= n:
    fat=fat*i
    i=i+1
print("o valor de %d! eh %d"%(n,fat))
fim=input("tecle enter para encerrar")
