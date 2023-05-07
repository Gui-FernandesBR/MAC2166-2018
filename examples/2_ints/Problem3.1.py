'''Problema 3.1'''
#Dado um número inteiro n, n>0, e um dígito d, 0<=d<=9.
#Determinar quantas vezes d ocorre em n.
print('Algoritmo que conta quantas vezes d aparece em n')
n=int(input("Digite o valor de n: "))
d=int(input("Digite o valor de d: "))
conta_digito=0
n_salvo=n
while n>0:
    dig=n%10
    n=n//10
    if dig==d:
        conta_digito=conta_digito+1
print("O digito",d,"ocorre",conta_digito,"vezes em", n_salvo)
fim=input("tecle enter para encerrar")
