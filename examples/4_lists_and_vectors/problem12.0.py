"""Faca um programa que permita gerar uma matriz em caracol"""
print("Codigo para gerar uma matriz em forma de caracol")
n = int(input('Digite a ordem da matriz: '))
matriz = []
for i in range(n):
    linha=[]
    for j in range(n):
        linha.append(' ')
    matriz.append(linha)
#Agora temos a matriz com as casas necessarias

if n%2==0:
    inicio_l = (n//2)-(1)    #indices onde se começa a plotar
    inicio_c = (n//2)-(1)
else:
    inicio_l = (n//2)
    inicio_c = (n//2)

direcao= 'D'
comp   =  2
for i in range(comp):
    matriz[inicio_l][inicio_c]=int(input('Digite o elemento da linha %d coluna %d: '%(inicio_l+1,inicio_c+1)))
    if i+1!=comp:
        inicio_c+=1                                        



    
i=1
comp=2
while i<=comp:
    matriz[inicio_l][inicio_c]=int(input('Digite o elemento da linha %d coluna %d: '%(inicio_l+1,inicio_c+1)))
    i+=1
    inicio_c+=1
    
print(matriz)

DIREITA=1
direcao=DIREITA
