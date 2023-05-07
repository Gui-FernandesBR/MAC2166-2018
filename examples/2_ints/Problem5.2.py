#Problema 5.2
'''Dado um numero, verifique se ele tem dois digitos adjacentes iguais'''
print('Algoritmo que verifica se um numero tem dois digitos adjacentes iguais')
n_salvo=n=int(input("Digite um numero: "))
anterior=n%10
n=n//10
adj_iguais=False
while n>0 and not adj_iguais:
    atual=n%10
    if atual==anterior:
        adj_iguais=True
    anterior=atual
    n=n//10
if adj_iguais:
    print(n_salvo,"tem dois digitos",atual,"adjacentes")
else:
    print(n_salvo,"nao tem dois digitos adjacentes iguais")
fim=input("acabamos, tecle enter")
