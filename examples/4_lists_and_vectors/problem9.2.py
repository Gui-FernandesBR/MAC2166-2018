""" Problema 9.2
    Dados um inteiro n>0 e n lançamentos de uma roleta
    (números entre 0 e 36), calcular a frequência de
    cada valor
"""
print("Codigo para calcular a freq. de cada valor dos lancamentos de uma ROLETA")


def main():
    n = int(input("digite o numero de lançamentos:"))
    i = 0
    seq = [0] * 37
    while i < n:
        lance = int(input("digite um dos lançamentos:"))
        seq[lance] = seq[lance] + 1
        i += 1
    print(">>>", seq)
    for i in range(len(seq)):
        print(
            "frequencia do numero %d=%f, aparições de %d=%d"
            % (i, seq[i] / n, i, seq[i])
        )


main()
fim = input("tecle enter para encerrar")
