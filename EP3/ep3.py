# -*- coding: UTF-8 -*-
"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP,
  DECLARO QUE SOU A ÚNICA PESSOA AUTORA E RESPONSÁVEL POR ESSE PROGRAMA.
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E, PORTANTO, NÃO CONSTITUEM ATO DE DESONESTIDADE ACADÊMICA,
  FALTA DE ÉTICA OU PLÁGIO.
  DECLARO TAMBÉM QUE SOU A PESSOA RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE NÃO DISTRIBUÍ OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Guilherme Fernandes Alves
  NUSP : 10774361
  Turma: 04 - Engenharia Civil
  Prof.: André Fujita
"""

# **********************************************************
# **                 INÍCIO DA PARTE 1                    **
# **********************************************************

def calcula_id(matriz):
    """ Retorna o valor de identificação de uma matriz computada pelo
    algoritmo adler32

    A função :func:'calcula_id' computa um identificador para uma matriz
    usando a seguinte versão adaptada do algoritmo de espalhamento Adler32:

        - A = 1 + matriz[0][0] + matriz[0][1] +...+ matriz[m-1][n-1] MOD 65521,
            onde m é o número de linhas e n é o número de colunas da matriz
        - B = (1 + matriz[0][0]) + (1 + matriz[0][0]+matriz[0][1]) + ... +
          (1 + matriz[0][0] + matriz[0][1] + ... + matriz[m-1][n-1]) MOD 65521
        - retorna B * (2**16) + A


    :param matriz: Uma matriz de inteiros
    :type matriz: <class 'list'>
    :return identificador: O identificador inteiro da matriz computado segundo
        a nossa versão adaptada do Adler32
    :rtype: <class 'int'>

    :Examples:

    >>> matriz_A = [[0,1,2], [3,4,5]]
    >>> matriz_B = [[3,4,5], [0,1,2]]
    >>> matriz_C = [[0,1], [1,0]]
    >>> matriz_D = [[1,0,2], [3,4,5]]
    >>> calcula_id(matriz_A)
    2686992
    >>> calcula_id(matriz_B)
    4456464
    >>> calcula_id(matriz_C)
    589827
    >>> calcula_id(matriz_D)
    2752528

    .. seealso::
        Consulte o enunciado para um exemplo mais detalhado.
    """
    n_linhas = len(matriz)
    n_colunas= len(matriz[0])
    ### valores iniciais das somas que serao usadas para encontrar A e B ###
    soma_A = 1
    soma_B = n_linhas * n_colunas
    ### Agora vamos para a parte boa ###
    k= n_linhas * n_colunas
    for i in range (n_linhas):
        for j in range(n_colunas):
            soma_A += matriz[i][j]
            soma_B += k * matriz[i][j]
            k=k-1
    A = soma_A % 65521
    B = soma_B % 65521  
    ### Falta somente fazer o retorno ###
    C = (B*(2**16))+A
    return C
# ----------------------------------------------------------
# --                  FIM DA PARTE 1                      --
# ----------------------------------------------------------

# **********************************************************
# **                 INÍCIO DA PARTE 2                    **
# **********************************************************

def carrega_identificador(nome_arquivo):
    """ Carrega o identificador de uma imagem presente em um arquivo.

    A função :func:'carrega_identificador' abre um arquivo de nome
    'nome_arquivo' presente na mesma pasta que o programa ep3.py, lê sua
    primeira linha e retorna o inteiro representando o identificador  
    presente nessa linha.

    :param nome_arquivo: String com o nome do arquivo com o identificador
    :type nome_arquivo: <class 'str'>
    :return identificador: Inteiro contendo identificador 
    :rtype: <class 'int'>

    :Example:

    >>> identificador = carrega_identificador('img01.adler32')
    >>> print(identificador)
    297286
    

    .. note::
        Embora pelas regras da disciplina você possa assumir que o arquivo
        'nome_arquivo' está presente na mesma pasta do programa ep3.py,
        boas práticas de programação sugerem que para escrita e leitura de
        arquivos, você sempre deve verificar à existência/permissões.
        Com relação ao identificador, você pode assumir que o arquivo contém
        um identificador válido na primeira linha.
    """
    adler = open(nome_arquivo,'r')   ### aqui abrimos o arquivo .adler32 ###
    ### Esse for serve para ler o arquivo aberto ###
    for linha in adler:
        b = linha.strip()
        code = int(b)
        break
    adler.close()   ### agora fechamos o arquivo e retornamos o codigo ###
    return code

def carrega_imagem(nome_imagem):
    """ Carrega do arquivo 'nome_imagem' uma imagem em formato PGM do tipo P2 e
    retorna à imagem em formato de matriz de pixels.

    A função :func:'carrega_imagem' lê uma imagem em formato PGM do tipo P2
    presente em um arquivo na mesma pasta do programa ep3.py e retorna uma
    matriz de inteiros de tamanho N-por-M, onde N é a altura da imagem, e M é
    largura da imagem, ambos medidos em pixels e obtidos através do cabeçalho
    da imagem.

    :param nome_imagem: String com o nome de imagem na mesma pasta de ep3.py
    :type nome_imagem: <class 'str'>
    :return matriz: Matriz de inteiros representando os pixels da imagem
    :rtype: <class 'list'>

    :Example:

    >>> A = carrega_imagem('imagem.pgm')
    >>> print(A)
    [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

    .. seealso::
        Vide enunciado para uma explicação mais detalhada acerca do formato PGM
    .. note::
        Você pode assumir que a imagem está no formato correto e que o valor
        da intensidade de cada pixel é um inteiro entre 0 e 255 (inclusive).
    """
    arquivo = open(nome_imagem,'r')       ### Apenas abre o arquivo ###
    c = str('')   ### utilizei esse c para ir salvando as linhas do arquivo ###
    for linha in arquivo:
        l = str(linha)
        if len(l)>0:
            c = c+l
    arquivo.close()  
    ##################################################################
    ### Presta atencao no truque pra tranformar a string em matriz ###
    matriz = []     ### matriz que sera retornada ###
    linha  = []      ### vai salvar uma linha da matriz ###
    ch = ''         ### vai salvar um numero em formato de srting ###
    ##########################################################################
    ### soh precisamos pegar os caracteres da matriz, nao precisamos das    ##
    ### especificacoes anteriores. Entao vamos procurar o indice onde comeca## 
    ### a matriz dentro do arquivo e salva-lo em ->comeco                   ##
    i = 0
    ainda_nao = True
    while i<len(c) and ainda_nao:
        if c[i] == '2' and c[i+1]=='5' and c[i+2]=='5':
            comeco = i+4
            ### comeco eh o indice onde aparece o 1o elem para a matriz ###
            ainda_nao = False
        i+=1
    ### Eu optei por nao usar o break ###
    ### O proximo for vai servir para colocar os numeros dentro da matriz ###
    for i in range(comeco,len(c)):
        if c[i]=='\n':
            if ch!='':
                linha.append(int(ch))
                ch = ''
            matriz.append(linha)
            linha=[]
        elif c[i]== ' ' or c[i]=='' and ch!=' ':
            linha.append(int(ch))   ### aqui convertemos as string para int ###
            ch = ''
        elif c[i]!=' ' and c[i]!='\n' and c[i]!='':
            ch += c[i]      ### aqui eu usei a CONCATERNACAO
    ### agora soh falta retornar a matriz ###
    return matriz

def salva_imagem(nome_arquivo, matriz):
    """ Cria (se não existir) e escreve a imagem representada pela matriz no
    arquivo de nome nome_arquivo no formato PGM (tipo 2).

    A função :func:'salva_imagem' recebe uma matriz de inteiros (0-255)
    representando uma imagem em tons de cinza e salva essa imagem no arquivo
    'nome_arquivo' no formato Portable GrayMap (PGM) do tipo P2 na mesma pasta.


    :param nome_arquivo: String contendo o nome de um arquivo (ex.'imagem.ppm')
    :param matriz: Matriz de inteiros representando uma imagem em tons de cinza
    :type nome_arquivo: <class 'str'>
    :type matriz: <class 'list'>

    :Example:

    >>> M = carrega_imagem('imagem.pgm')
    >>> print(M)
    [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    >>> M[0][0] = 255
    >>> print(M)
    [[255, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    >>> salva_imagem('nova_imagem.pgm', M)

    .. seealso::
        Consulte o enunciado para informações específicas do formato PGM tipo 2
    """
    portable_GrayMap = open(nome_arquivo,'w')   # abre ou cria o arquivo.pgm #
    ### 1o escrevi o cabecalho ###
    portable_GrayMap.write('P2\n')
    m = len(matriz)
    n = len(matriz[0])
    portable_GrayMap.write('%d %d\n'%(n, m))
    portable_GrayMap.write('255\n')
    ### Agora posso escrever os elementos da matriz ###
    for i in range(m):
        for j in range(n):
            if matriz[i][j]!='':
                if j!=(n-1):
                    portable_GrayMap.write('%d '%(matriz[i][j]))
                else:
                    portable_GrayMap.write('%d'%(matriz[i][j]))
        portable_GrayMap.write('\n')
    portable_GrayMap.close()    # fecha o arquivo #

def carrega_transformações(nome_arquivo):
    """Carrega transformações de um arquivo de texto.

    A função :func:'carrega_transformações' recebe uma string com o nome de um
    arquivo presente na mesma pasta do programa ep3.py que contém as matrizes
    de transformação.
    Neste arquivo:

        - A primeira linha representa o número total de transformações
        - Todas as outras linhas trazem ou transformações ou comentários

    Uma linha começando com # indica um comentário e deve ser ignorada.
    Todas as outras linhas representam matrizes 2-por-3 de modo que a matriz
    inteira está representada em uma única linhado arquivo e cada elemento da
    matriz é separado por um (ou mais) espaços.
    O exemplo abaixo mostra o conteúdo de um possível arquivo de transformações

    **Exemplo de arquivo de transformações**:
    2
    # Meu conjunto de transformações
    # transformação identidade
    1 0 0 0 1 0
    # espelhamento
    -1 0 0 0 -1 0


    :param nome_arquivo: String com nome de um arquivo texto contendo as
        transformações
    :type nome_arquivo: <class 'str'>
    :return lista: Uma lista de matrizes de transformação
    :rtype: <class 'list'>

    :Example:

    >>> transformações = carrega_transformações('duas_transformações.txt')
    >>> print(transformações)
    [[[1, 0, -20], [0, 1, -20]], [[1, 0, 0], [0, 1, 0]]]

    .. seealso::
        Veja o enunciado para maiores detalhes da estrutura desse arquivo.
    .. note::
        Você pode considerar que o arquivo de transformações só contém os
        três tipos de linhas mencionados (número total de transformações,
        comentários e transformações), você não precisa tratar outros formatos.
    """
    abre = open(nome_arquivo,"r")
    ### Foi aqui que eu usei o .read, fiz isso para ganhar tempo, mas eu ### 
    ### provei que eu sei fazer do jeito dificil la na linha 168         ###
    b = abre.read()
    M = []
    linha =[]
    tam = len(b)
    for i in range(tam):
        if b[i]=='\n':
            M.append(linha)
            linha = []
        else:
            linha.append(b[i])
            
    num_tsf = int(M[0][0])   # variavel que salva o num de transformacoes #
    A =[]   # 1o tem que tirar as linhas de comentario da matriz #
    tam = len(M)
    for i in range(1,tam):
        if M[i][0]!='#':
            A.append(M[i])    
    
    B =[]   # Agora teremos que buscar a matriz sem espacos #
    tam = len(A)
    for i in range(tam):
        lista =[]
        numero=''
        for j in range(len(A[i])):
            if A[i][j]==' ' or A[i][j]=='':
                lista.append(int(numero))
                numero = ''
            else:
                numero += A[i][j]
        lista.append(int(numero))
        B.append(lista)
        
    matriz =[''] * num_tsf  ## UFA, finalmente a matriz final ##
    tam = len(matriz)
    for i in range(tam):
        fatia1 = []
        fatia2 = []
        for j in range(len(B[0])):
            if j<3:
                fatia1.append(B[i][j])
            else:
                fatia2.append(B[i][j])
        matriz[i] = [fatia1,fatia2]
    ### Agora eh soh retornar a matriz ###
    return matriz

# ----------------------------------------------------------
# --                  FIM DA PARTE 2                      --
# ----------------------------------------------------------

# **********************************************************
# **                 INÍCIO DA PARTE 3                    **
# **********************************************************

def transforma(matriz, transformação):
    """ Devolve uma transformação geométrica linear da matriz.

    A função :func:'transforma' recebe uma matriz de pixels e uma transformação
    afim representada matricialmente e retorna a matriz transformada, **sem**
    modificar a matriz original.


    :param matriz: Matriz representando imagem em tons de cinza (0-255)
    :param transformação: Matriz 2-por-3 representando transformação linear
    :type matriz: <class 'list'>
    :type transformação: <class 'list'>
    :return matriz_transformada: Matriz resultado da transformação aplicada
        sobre todos os pontos
    :rtype: <class 'list'>

    :Example:

    >>> matriz1 = [[1, 2, 3], [4, 5, 6]]
    >>> print(matriz1)
    [[1, 2, 3], [4, 5, 6]]
    >>> translação_diagonal_por_1_pixel = [[1, 0, 1], [0, 1, 1], [0, 0, 1]]
    >>> matriz2 = transforma(matriz1, translação_diagonal_por_1_pixel)
    >>> print(matriz1)
    [[1, 2, 3], [4, 5, 6]]
    >>> print(matriz2)
    [[6, 4, 5], [3, 1, 2]]

    .. seealso::
        Vide enunciado para maiores exemplos da aplicação dessa transformação

    .. note::
        Você pode assumir que só serão utilizadas transformações inversíveis
        cujos coeficientes são inteiros.
    """
    Tr = transformação    ## Usei o Tr pra diminuir o nome da variavel lista ##
    n_linhas  = len(matriz)
    n_colunas = len(matriz[0])
    matriz_transformada=[]  #matriz que sera retornada
    for i in range(n_linhas):
        linha=[]
        for j in range(n_colunas):
            linha.append('')
        matriz_transformada.append(linha)
    ### Ate aqui soh criei a matriz com espacos vazios, agora vou preenche-la #
    for y in range(n_linhas):
        for x in range(n_colunas):
            sx = (x * Tr[0][0]) + (y * Tr[0][1]) + Tr[0][2]
            sy = (x * Tr[1][0]) + (y * Tr[1][1]) + Tr[1][2]
            x_linha = sx % n_colunas
            y_linha = sy % n_linhas
            matriz_transformada[y_linha][x_linha] = matriz[y][x]
    ### Os nomes das variaveis x e y podem confundir um ouco, mas estava assim
    ### no enunciado
    return matriz_transformada

# ----------------------------------------------------------
# --                  FIM DA PARTE 3                      --
# ----------------------------------------------------------

# **********************************************************
# **                 INÍCIO DA PARTE 4                    **
# **********************************************************

def busca(matriz, transformações, identificação, max_transfs):
    """ Busca imagem com identificação dada usando no máximo um conjunto de
    max_transfs transformações.

    A função :func:'busca' recebe uma matriz representando uma imagem
    monocromática, uma lista de transformações possíveis, um identificador
    correspondente à dispersão criptográfica da imagem original e o valor do
    número máximo de transformações em sequencia à serem realizadas sobre à
    matriz nessa busca e devolve:

        - A matriz da imagem original (caso encontrada) OU
        - None (caso contrário)

    :param matriz: Uma matriz de inteiros representando uma imagem
    :transformações: Uma lista de matrizes de transformação
    :identificação: Uma string com o identificador da imagem original
    :max_transfs: Número máximo de sequencias de transformações à testar
    :type matriz: <class 'list'>
    :type transformações: <class 'list'>
    :type identificação: <class 'str'>
    :type max_transfs: <class 'int'>
    :return resultado: Matriz com imagem restaurada ou None se ela não for
        encontrada.
    :rtype: <class 'list'> OU <class 'NoneType'>

    :Example:

    >>> original = [[1,2,3], [4,5,6], [7,8,9]]
    >>> identificador = calcula_id(imagem)
    >>> print(identificador)
    11403310
    >>> nova = transforma(imagem, [[1,0,1], [0,1,0]]) # Aplica desloc em eixo x
    >>> print(nova)
    [[3, 1, 2], [6, 4, 5], [9, 7, 8]]
    >>> nova2 = transforma(nova, [[1,0,1], [0,1,1]]) # Aplica Desloc x+1 e y+1
    >>> print(nova2)
    [[8, 9, 7], [2, 3, 1], [5, 6, 4]]
    >>> transfs = [[[1,0,-1], [0,1,0]], [[1,0,-1],[0,1,-1]], [[1,0,1],[0,1,1]]]
    >>> resultado = busca(nova2, transfs, identificador, 2)
    >>> print(resultado)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> resultado2 = busca(nova2, transfs, identificador, 1)
    >>> print(resultado2)
    None
    """ 
    ### Funcao igualzinha a do enunciado, pra nao dar problema ###
    if calcula_id(matriz) == identificação:
        return matriz
    elif max_transfs == 0:
        return None
    for T in transformações:
        N = transforma(matriz, T)
        R = busca(N, transformações, identificação, max_transfs-1)
        if R!= None:
            return R
    return None

# ----------------------------------------------------------
# --                  FIM DA PARTE 4                      --
# ----------------------------------------------------------

# **********************************************************
# **                 INÍCIO DA PARTE 5                    **
# **********************************************************

def main():
    """ Aqui você deve implementar à interface de comunicação com o usuário

    Sua interface deve (necessariamente nessa ordem):
        1. Escrever uma mensagem de identificação do autor e descrição do programa.
        2. Solicitar ao usuário que digite o nome do arquivo da imagem transformada.
        3. Solicitar ao usuário que digite o nome do arquivo contendo o identificador.
        4. Solicitar ao usuário que digite o nome do o arquivo com as transformações.
        5. Solicitar ao usuário que digite o nome do arquivo no qual será salva a imagem restaurada (se encontrada).
        6. Informar se a busca foi exitosa ou não.

    :Example:

    >>> $ python3 ep3.py
    *****************************
    *** Programa desfaz vírus ***
    *****************************

    Autor: Denis Mauá
    NUSP: 3730790

    Entre com o nome do arquivo contendo imagem transformada: img00.pgm
    Entre com o nome do arquivo contendo o identificador da imagem original: img00.adler
    Entre com o nome do arquivo contendo as transformações disponíveis: transformações00.txt
    Entre com o nome do arquivo onde a imagem original deve ser salva: resultado00.pgm
    Entre com o número máximo de transformações: 2

    Tentando restaurar imagem 'img00.pgm'... Falhou!

    Não foi possível encontrar uma imagem com o identificador 870647247 utilizando uma sequência de no máximo 2 transformações em 'transformações00.txt'!

    Você pode tentar aumentar o número máximo de transformações ou mudar o arquivo de transformações.

    >>> $ python3 ep3.py
    *****************************
    *** Programa desfaz vírus ***
    *****************************

    Autor: Denis Mauá
    NUSP: 3730790

    Entre com o nome do arquivo contendo imagem transformada: img01.pgm
    Entre com o nome do arquivo contendo o identificador da imagem original: img01.adler
    Entre com o nome do arquivo contendo as transformações disponíveis: transformações.txt
    Entre com o nome do arquivo onde a imagem original deve ser salva: resultado01.pgm
    Entre com o número máximo de transformações: 6

    Tentando restaurar imagem 'img01.pgm'... Pronto!

    Imagem com o identificador 870647247 salva em 'resultado01.pgm'!

    .. seealso::
        Consulte o enunciado para mais exemplos.
    """
    print('*****************************')
    print('*** Programa desfaz vírus ***')
    print('*****************************')
    print('')
    print('Autor: Guilherme Fernandes Alves')
    print('NUSP: 10774361')
    print("Vish, seus alunos te enviaram um virus que estraga imagens???")
    print("NÃO SE PREOCUPE, vamos consertar o seu problema")
    arq_img = input('Digite o nome do arquivo contendo a imagem transformada: ')
    arq_code= input('Digite o nome do arquivo contendo o identificador da imagem original : ')
    arq_tfsm= input('Digite o nome do arquivo contendo as transformações disponíveis : ')
    img_orig= input('Digite o nome do arquivo onde a imagem original deve ser salva : ')
    max_tran= int(input('Escolha o número máximo de transformações : '))
    identificação = carrega_identificador(arq_code)
    matriz = carrega_imagem(arq_img)
    transformações = carrega_transformações(arq_tfsm)
    print('Tentando restaurar imagem',arq_img,'. . . ')
    B = busca(matriz,transformações,identificação,max_tran)
    if B == None:
        print('Não foi possível reconstruir uma imagem com o identificador %d utilizando uma sequência de no máximo %d transformações em'%(identificação, max_tran), arq_tfsm,'!')
        salva_imagem(img_orig,B)
        print('Mesmo assim, copiamos a sua imagem para', img_orig)
        print('Você pode tentar aumentar o número máximo de transformações ou mudar o arquivo de transformações.')
    else:
        print('PRONTO!')
        salva_imagem(img_orig,B)
        print('Imagem com o identificador %d salva em'%(identificação),img_orig,'!')
        
        
# ----------------------------------------------------------
# --                  FIM DA PARTE 5                      --
# ----------------------------------------------------------

if __name__ == "__main__":
    main()
