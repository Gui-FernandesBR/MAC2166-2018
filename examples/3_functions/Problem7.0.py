""" Problema 7.0
    Decomponha um numero em fatores e diga as multiplicidades
"""
print('Algoritmo para decompor um numero em fatores primos')
def main():
    n=int(input("digite um numero:"))
    fator=2
    while n!=1:
        mult=0
        while n%fator==0:
            n=n/fator
            mult+=1
        if mult!=0:
            print("Fator %d, multiplicidade %d"%(fator,mult))
        fator+=1
main()
fim=input('tecle enter para encerrar')

        
