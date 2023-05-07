# PROBLEMA 5.1
""" Dados um número inteiro n, n>0, e uma sequencia com n numeros
    inteiros. Verificar se a sequencia esta em ordem crescente
"""
print("Algoritmo para verificar se os numeros estão em ordem crescente")
n = int(input("Digite o tamanho da seq.: "))
crescente = True
anterior = int(input("Digite um numero: "))
i = 1
while i < n and crescente:
    atual = int(input("Digite um numero: "))
    if anterior >= atual:
        crescente = False
    anterior = atual
    i = i + 1
if crescente:
    print("Está em ordem crescente")
else:
    print("Não está em ordem crescente")
pronto = input("tecle enter para encerrar o programa, obrigado")
