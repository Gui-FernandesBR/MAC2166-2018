''' ARQUIVOS DE TEXTO '''
''' PROBLEMA 2.1 '''
''' Faca um programa que gera uma imagem em tons de cinza em formato .pgm 
    utilizando o padrao gerado no item anterior (molduras concentricas), usando
    zero (preto) como v1 e 255(branco) como v2'''

def cria_matriz(n, p):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            if i==0 or j == 0 or j == n-1 or i ==n-1:
                linha.append(p)
            else:
                linha.append(' ')
        matriz.append(linha)
    matriz[n//2][n//2] = 0
    return matriz

def imprime_matriz(M):
    for i in range(len(M)):
        print("|", end=' ')
        for j in range(len(M[0])):
            print (M[i][j], end=' ')
        print("|", end='')
        print('')
        
def molduras_concentricas(n, v1, v2):
    M = cria_matriz (n, 0)
    for i in range (n):
        for j in range(n):
            dh = n//2 -j
            if dh < 0:
                dh = -dh
            dv = n//2 -i
            if dv < 0 :
                dv = -dv
            if dh>dv:
                if dh %2 ==0:
                    M[i][j]= v1
                else:
                    M[i][j]=v2
            else:
                if dv % 2 == 0:
                    M[i][j] = v1
                else:
                    M[i][j] = v2
    return M

def grava_PGM(M):
    ''' MARCELOOOOOOOOOOOOOO, essa aqui eh a funcao pra salvar imagem.
        Me pergunta oq vc não entender. Não é só copiar no ep3, mas eh
        o mesmo esquema'''
    arquivo = open("fig01.pgm",'w')
    arquivo.write('P2\n')
    m = len(M)
    n = len(M[0])
    arquivo.write('%d %d\n'%(n, m))
    arquivo.write('255\n')
    for i in range(m):
        for j in range(n):
            arquivo.write('%3d'%(M[i][j]))
        arquivo.write('\n')
    arquivo.close()
    
def main():
    n = int(input('Digite a a ordem da matriz (numero impar): '))
    M = molduras_concentricas(n, 0, 255)
    grava_PGM(M)
    imprime_matriz(M)
main()
a = open('fig01.pgm','r')
b = str(a.read())

print(b)
