'''Dada uma seqüência de n números inteiros, imprimi-la
na ordem inversa à da leitura. '''

lista_normal=[]
tamanho=int(input("digite o tamanho da lista:"))
for i in range(tamanho):
    item=int(input("digite o item de indice %d:"%(i)))
    lista_normal.append(item)

for j in range(tamanho-1,-1,-1 ):
    print(lista_normal[j], end=" ")
acabar=input("tecle enter para acabar:")