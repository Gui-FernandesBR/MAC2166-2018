# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 16:20:54 2018

@author: Guilherme Fernandes Alves
"""
""" Podemos calcular uma aproximação da raiz quadrada de um número através de
uma série. A ideia deste método é devida a Isaac Newton, que propôs um método 
geral para encontrar zeros de funções, ou seja, números que quando aplicados na
função o resultado obtido é zero. O primeiro termo da série para achar a raiz 
quadrada de um número x é o próprio x"""

print("Algoritmo para calcular raiz quadradas através do método de Newton")
print("Aviso: este programa opera de maneira recursiva")

xi = x = float(input("Digite o numero que voce deseja extrair a raiz quadrada: "))
nive = int(input("Digite o grau de aproximacao: "))
if nive < 0:
    print("Escolha um grau positivo")
    print("Vamos tentar de novo")
    nive = int(input("Digite o grau de aproximacao: "))


def raiz_quadrada(primeiro, atual, n):  ## Metodo de Newton ##
    """
    (float, float, int) -> float
    Recebe um real x e um inteiro n e retorna o valor de x_n como aproximação
    para a raiz quadrada de x.
    """
    if n == 0:
        return atual
    else:
        return raiz_quadrada(primeiro, (atual + (primeiro / atual)) / 2, n - 1)


print(raiz_quadrada(x, xi, nive))
fim = input("tecle enter para encerrar o programa - obrigado")
