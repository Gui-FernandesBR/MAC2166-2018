''' Problema de criar uma reta na imagem'''
''' Dada as coordenadas (x1,y1) e (x2,y2) das extremidades de um segmento de reta
e uma matriz representando uma imagem em tons de cinza, faça uma função recursiva
que desenha o segmento de reta na imagem com um valor de intensidade fornecido'''

def desenha_reta(matriz,x1,y1,x2,y2,val):
    if abs(x2-x1)<=1 and abs(y2-y1)<=1:
        matriz[int(y1+0,5)][int(x1+0,5)] = val
        matriz[int(y2+0,5)][int(x2+0,5)] = val
    else:
        xm = (x1+x2)//2
        ym = (y1+y2)//2
        desenha_reta(matriz,x1,y1,xm,ym,val)
        desenha_reta(matriz,xm,ym,x2,y2,val)
        
