#Problema 4.1
'''Dadas as notas de um grupo de alunos, conte quantos alunos foram
aprovados ou nao, diga quantas recs'''
print("Insira as notas dos alunos e receba o numero de aprovacoes,recs, etc")
n=int(input("Digite o numero de alunos:"))
no_aprovados=0
no_rec=0
no_reprovados=0
no_excelentes=0
i=0
while i<n:
    nota=float(input("digite uma nota final:"))
    if nota>=5.0:
        no_aprovados+=1
        if nota>=8.0:
            no_excelentes+=1
    elif nota>=3:
        no_rec+=1
    else:
        no_reprovados+=1
    i=i+1
print("__________________________")
print("Total de alunos=",n)
print("Numero de alunos aprovados= ", no_aprovados)
print('Numero de alunos excelentes=', no_excelentes)
print('Numero de alunos reprovados=', no_reprovados)
print('Numero de alunos recuperaca=', no_rec)
fim=input('tecle enter para encerrar')
