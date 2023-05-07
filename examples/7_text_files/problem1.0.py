''' ARQUIVOS DE TEXTO '''
''' PROBLEMA 1 '''
''' Faca um programa em python que leia uma planilha no formato csv, onde o
    caractere separador eh o ponto e virgula (;), em uma matriz e que gere um
    novo arquivo tab contendo a planilha separada por tabulacao '''

def main():
    arquivo = open("notas.csv",'r')
    matriz = []
    for linha in arquivo:
        l = linha.strip()
        if len(l) > 0:
            palavras = l.split(";")
            matriz.append(palavras)
    arquivo.close()
    arquivo = open('notas.tab','w')
    n = len(matriz)
    m = len(matriz[0])
    for i in range (n):
        for j in range (m-1):
            arquivo.write(matriz[i][j])
            arquivo.write('\t')
        arquivo.write(matriz[i][m-1])
        arquivo.write('\n')
    arquivo.close
main()