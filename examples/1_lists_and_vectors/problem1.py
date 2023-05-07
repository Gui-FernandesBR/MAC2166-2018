"""
Deseja-se publicar o número de acertos de cada aluno em uma prova em forma
de testes. A prova consta de 30 questões, cada uma com cinco alternativas 
identificadas por A, B, C, D e E. Para isso são dados: 
    - o cartão gabarito; 
    - o número de alunos da turma; 
    - o cartão de respostas para cada aluno, contendo o seu número e suas
    respostas. 
"""

cart_gaba = []
resp_aluno = []

for i in range(30):
    cart_gaba.append(" ")
    resp_aluno.append(" ")

nota_aluno = []
no_alunos = int(input("Digite o numero de alunos que fizeram a prova:"))
for i in range(no_alunos):
    nota_aluno.append(0)
for j in range(30):
    certa = input("digite a reposta certa da questao %d:" % (j + 1))
    cart_gaba[j] = certa
for k in range(no_alunos):
    acertos_aluno = 0
    for l in range(30):
        aluno = input("digite a resposta do %dº aluno na questao %d:" % (k + 1, l + 1))
        resp_aluno[l] = aluno
    for m in range(30):
        if resp_aluno[m] == cart_gaba[m]:
            acertos_aluno += 1
    nota_aluno[k] = acertos_aluno

print("Quantidade de acertos de cada aluno:")
print(nota_aluno)
fim = input("tecle fim para acabar")
