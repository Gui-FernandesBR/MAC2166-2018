""" Problema 7.1
    Dado um numero n>0 e uma sequencia n de numeros inteiros
    maiores do que zero, determinar o máximo divisor comum
    entre eles
"""
print('>>> Algoritmo para determinar o MDC de uma sequencia <<<')
def main():
    n=int(input("digite o tamanho da seq.:"))
    mdc_atual=int(input("digite o 1º numero"))
    i=1
    while i<n:
        num=int(input("digite o %d numero:"%(i+1)))
        i+=1
        mdc_atual=mdc(mdc_atual,num)
    print("o mdc eh",mdc_atual)
    
def mdc(a,b):
    mdc=a
    while a%mdc!=0 or b%mdc!=0:
        mdc=mdc-1
    return mdc
main()
fim=input('tecle enter para encerrar')
