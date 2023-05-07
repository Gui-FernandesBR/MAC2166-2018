"""Problema 3.2"""
"""Verificar se um numero eh triangular"""
print("Dado um numero inteiro, esse algoritmo verifica se ele eh triangular")
n = int(input("digite o valor de n:"))
i = 1
while i * (i + 1) * (i + 2) < n:
    i = i + 1
if i * (i + 1) * (i + 2) == n:
    print(">>> %d eh o produto %d %d %d" % (n, i, i + 1, i + 2))
    print("Portanto", n, "eh triangular")
else:
    print(("%d nao eh triangular") % (n))
fim = input("tecle enter para encerrar")
