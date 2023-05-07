#Vamos decompor a**n em (a**(n/2))*(a**(n/2))
print('Vamos decompor a**n em (a**(n/2))*(a**(n/2))')
base=int(input('Digite a base: '))
expoente=int(input('Digite o expoente:'))
n=expoente/2
print('Podemos decompor %d elevado a %d em:'%(base, expoente),base**n,'*',base**n)
fim=input('tecle enter para encerrar')