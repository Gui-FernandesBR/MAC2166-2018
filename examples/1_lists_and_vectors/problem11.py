'''Dada uma matriz quadrada de ordem 3, calcular e imprimir seu determinante'''
print('Algoritmo capaz de receber uma matriz 3x3, calcular e imprimir seu determinante utilizando a lei de Sarrus')
print('Alerta: utilize numeros inteiros')

matriz=[]
for i in range(3):
    linha=[]
    for j in range(3):
        elem=int(input('Digite o elemento da linha %d coluna %d: '%(i+1,j+1)))
        linha.append(elem)
    matriz.append(linha)
    
a= matriz[0][0]*matriz[1][1]*matriz[2][2]
b= matriz[0][1]*matriz[1][2]*matriz[2][0]
c= matriz[0][2]*matriz[1][0]*matriz[2][1]
d= matriz[2][0]*matriz[1][1]*matriz[0][2]
e= matriz[2][1]*matriz[1][2]*matriz[0][0]
f= matriz[2][2]*matriz[1][0]*matriz[0][1]
det=a+b+c-d-e-f

print('O determinante da matriz vale:', det)
fim=input('Tecle Enter para encerrar') 