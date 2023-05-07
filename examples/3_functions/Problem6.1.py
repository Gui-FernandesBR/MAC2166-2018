'''Problema 6.1'''
'''Programe para que verifique se um numero eh soma de dois primos ou nao'''
print('Algoritmo para verificar se um numero eh ou nao soma de dois primos')
def primo(n):
    """(int)->bool
        Recebe um número n e retorna True se n é primo e False em caso contrário
    """
    eh_primo=True
    div=2
    while div<n and eh_primo:
        if n%div==0:
            eh_primo=False
        div+=1
    return eh_primo

def main():
    """ Recebe um inteiro n e diz,
        para cada número entre 1 e n se o tal numero é ou não soma de dois
        primos
    """
    n=int(input("Digite n:"))
    i=1
    while i<=n:
        j=2
        eh_soma=False
        while j<i and not eh_soma:
            if primo (j) and primo (i-j):
                eh_soma=True
                p=j
                q=i-j
            j+=1
        i+=1
    if eh_soma:
        print(">>> %d eh soma dos primos, %d e %d"%(n,p,q))
    else:
        print(">>> %d não eh soma de primos"%(n))
main()
fim=input("tecle enter para encerrar")
