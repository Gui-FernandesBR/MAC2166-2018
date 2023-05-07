#PROBLEMA 5.3
''' Considerando a figura do bob esponja representada pelas inequacoes
    Verifique quais pontos estao dentro ou fora da area'''
print('Esse aqui eh o problema do bob esponja')
x_pos=x=float(input("Digite x:"))
y=float(input("Digite y:"))
if x<0:
    x_pos=-x
face = x_pos<5     and 0<y<8
boca = x_pos<=3    and 1<=y<=2
olho = 1<=x_pos<=4 and 4<=y<=7
iris = 2<x_pos<3   and 4<=y<=7
if iris or face and not(boca or olho):
    print("dentro")
else:
    print("fora")
fim=input("acabamos, tecle enter")

