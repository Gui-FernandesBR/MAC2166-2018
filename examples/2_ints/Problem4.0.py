# Problema 4.0
""" Dado o número n>0 de alunos e notas, que são números reais entre 0 e 10,
    calcule a média das notas dos alunos"""
n = int(input("digite o número de alunos: "))
soma = 0
cont = 0
while cont < n:
    nota = float(input("digite a nota do %dº aluno: " % (cont + 1)))
    cont = cont + 1
    soma = soma + nota
media = soma / n
print("A media das notas eh:", media)
fim = input("tecle enter pra fechar o programa")
