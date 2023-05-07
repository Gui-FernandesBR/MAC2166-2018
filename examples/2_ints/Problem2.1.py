'''Problema 2.1
   Calculo da soma de varios numeros
'''
print("Digite varios numeros e, por fim, digite o zero para que o programa some")
num=int(input("digite um numero:"))
soma=0
while num!=0:
   soma=soma+num
   num=int(input("digite um numero:"))
print("a soma eh",soma)
fim=input("tecle fim para acabar")
