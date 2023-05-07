"""PROBLEMA 5.0"""
"""Contar quantos alunos ficaram de recuperação"""
print("Algoritmo para contar quantos alunos ficaram de recuperacao")
n = int(input("Digite o numero de alunos:"))
cont_rec = 0
i = 0
while i < n:
    nf = float(input("Digite a nota do %dº aluno:" % (i + 1)))
    if 3 <= nf and nf < 5:
        cont_rec += 1
    i += 1
print(cont_rec, "= numero de alunos que ficaram de rec")
fim = input("Digite 'fim' e tecle enter para encerrar")
