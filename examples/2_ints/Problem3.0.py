""" Problema 3.0
    Dada uma sequencia de numeros, contar quantos sao pares e quantos sao impares
"""
print("Codigo para contar quantos numeros de uma seq. sao pares e quantos sao impares")
n = int(input("digite o tamanho da sequencia:"))
conta_par = 0
conta_impar = 0
while n > 0:
    num = int(input("digite um num. da seq:"))
    n = n - 1
    if num % 2 == 0:
        conta_par = conta_par + 1
    else:
        conta_impar += 1
print(conta_par, "quantidade de numeros pares")
print(conta_impar, "quantidade de numeros impares")
fim = input("tecle fim para encerrar")
