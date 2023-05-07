""" Problema 9.1
    Dadas n notas de provas, calcular a sua média
    e o número de notas acima da media
"""
print("Algoritmo para calcular a media das notas")


def main():
    n = int(input("Digite o numero de notas: "))
    i = 0
    soma = 0
    x = 0
    lista = []
    acima = 0
    while i < n:
        nota = float(input("Digite uma das notas: "))
        lista.append(nota)
        soma = x + nota
        x = soma
        i = i + 1
    media = float(soma / n)
    print("A media das notas é", media)
    a = 0
    while a < n:
        if lista[a] > media:
            acima = acima + 1
        a += 1
    print("O numero de notas acima da media é:", acima)


main()
fim = input("tecle enter para acabar")
