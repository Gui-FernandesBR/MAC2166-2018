"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Guilherme Fernandes Alves
  NUSP : 10774361
  Turma: 04 - engenharia civil
  Prof.: André Fujita

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma referência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
  
  Exemplo:
  - O algoritmo Quicksort foi baseado em
  http://wiki.python.org.br/QuickSort

  """

# !!!!! NÃO APAGUE NEM ALTERE NENHUM import !!!!!!
import random

# !!!!! PARA TESTAR O JOGO, USE VALORES MENORES, COMO 10 E 5, MAS
# VOLTE PARA O ORIGINAL ANTES DE ENTREGAR !!!!
COLUNA_MAXIMA = 56
LINHA_MAXIMA = 19

# !!!!! NÃO APAGUE NEM ALTERE NENHUMA CONSTANTE !!!!!
# CONSTANTES DE IMPRESSÃO NA TELA
CANHAO = "A"
NAVE = "V"
LASER_CANHAO = "^"
LASER_NAVE = "."
EXPLOSAO = "*"

# !!!!! NÃO APAGUE NEM ALTERE NENHUMA CONSTANTE !!!!!
# CONSTANTES DE AÇÕES DE MOVIMENTAÇÃO DOS OBJETOS NO JOGO
ATIRA = 3  # para tecla 'l' quando movimentar o canhão
ESQUERDA = -1  # para tecla 'e' quando movimentar o canhão
DIREITA = 1  # para tecla 'd' quando movimentar o canhão
BAIXO = -2

# !!!!! NÃO APAGUE NEM ALTERE NENHUMA CONSTANTE !!!!!
# CONSTANTES DE RESULTADO DO JOGO
VENCEU = True
PERDEU = False

# !!!!! NÃO APAGUE NEM ALTERE NENHUMA CONSTANTE !!!!!
# CONSTANTES DOS PONTOS RELACIONADOS A LASERS OU NAVES DESTRUÍDAS
PONTOS_ACERTOU_LASER = 1
PONTOS_ACERTOU_NAVE = 3

# !!!!! NÃO APAGUE NEM ALTERE NENHUMA CONSTANTE !!!!!
# OUTRAS CONSTANTES: SEMENTE DO GERADOR DE NÚMEROS ALEATÓRIOS E
# VALORES USADOS NA FUNÇÃO QUE MOVIMENTA AS NAVES
SEMENTE = 0
ATINGIU_ESQUERDA = -1
ATINGIU_DIREITA = 1
ATINGIU_EMBAIXO = -2


# !!!!! NÃO MODIFIQUE NADA NO main() !!!!!
# FUNÇÃO PRINCIPAL QUE SÓ LÊ A QUANTIDADE DE INIMIGOS DO TECLADO,
# PASSA O CONTROLE PARA A FUNÇÃO REAL DO JOGO E RECEBE COMO RETORNO A
# PONTUAÇÃO DO JOGADOR PARA IMPRIMIR NA TELA COM O RESULTADO DO JOGO
def main():
    random.seed(SEMENTE)

    quantidadeNaves = int(
        input(
            "Digite o numero de naves (inteiro maior que 1 e menor que %d): "
            % (COLUNA_MAXIMA - 3)
        )
    )

    resultado = joga(quantidadeNaves)

    if resultado[0] == VENCEU:
        print(">>> CONGRATULATIONS! Você venceu!")
    else:
        print(">>> GAME OVER! Você perdeu!")

    print(">>> Pontuação:", resultado[1])


# DEMAIS FUNÇÕES NECESSÁRIAS PARA O JOGO
# !!!!! SEU TRABALHO COMEÇA AQUI. COMPLETE TODAS AS FUNÇÕES !!!!!
# !!!!! MAS NÃO MODIFIQUE A ASSINATURA DE NENHUMA DELAS E NEM O QUE JÁ ESTÁ FEITO !!!!!


# Passo 0: função para imprimir a matriz do jogo. Ela precisa ser
# modificada para imprimir os '|' nas laterais direita e esquerda
def imprimeMatriz(matriz):
    """(matriz) -> None

    Imprime a matriz do jogo. Cada posição da matriz é um caracter e deve
    ser impresso exatamente com o valor dele."""
    for linha in matriz:
        print("|", end="")  # insere a parede da esquerda
        for position in linha:
            print(position, end="")
            i += 1
        print("|", end="")  # insere a parede da direita
        print("")  # pula uma linha


# Passo 1: função que cria todos os elementos na matriz do jogo (Deve
# ser chamada só no início do jogo)
def criaElementos(quantidadeNaves, matriz):
    """int, (matriz) -> None

    Recebe um inteiro com a quantidade de naves a serem criadas
    e a matriz de caracteres vazia para colocar os elementos no início do
    jogo: o canhão do jogador na linha de baixo e na coluna do meio e as
    naves na parte superior. As naves devem sempre ficar em pares (um em
    cima do outro) e separados pelos outros pares por uma coluna vazia.
    Por exemplo, se a quantidade de naves for 4, a parte superior da
    matriz tem que ficar assim:

    V V
    V V

    Se for 6 tem que ficar assim:

    V V V
    V V V

    Se for 5 tem que ficar assim:

    V V V
    V V
    """
    if quantidadeNaves % 2 == 0:  # se quantidadeNaves for par
        j = 0
        for i in range(quantidadeNaves // 2):
            matriz[0][i + j] = NAVE
            matriz[1][i + j] = NAVE
            j = j + 1
    else:  # se a quantidade de naves for impar
        j = 0
        for i in range((quantidadeNaves // 2) + 1):
            matriz[0][i + j] = NAVE
            j += 1
        j = 0
        for i in range(quantidadeNaves // 2):
            matriz[1][i + j] = NAVE
            j += 1
    matriz[LINHA_MAXIMA][COLUNA_MAXIMA // 2] = CANHAO  # Insere o canhao


# Passo 2: primeira função para mover algum elemento que emite lasers.
# Nesse caso para mover o canhão do jogador.
def moveCanhao(direcao, matriz):
    """int, (matriz) -> bool

    Recebe um inteiro com a direção (valores definidos em ESQUERDA e
    DIREITA) para mover o canhão do jogador (caracter definido em CANHAO)
    e a matriz de caracteres do jogo, para mover o canhão nessa direção.
    Ao mover tem que observar se atingiu algum laser de alguma nave (caso
    no qual tem que imprimir um EXPLOSAO no lugar). Nesse caso precisará
    informar que o canhão foi atingido pois a função retorna esse valor.

    Retorna:

    True se canhão do jogador foi atingido (False se não)

    Obs.: o movimento do canhão é cíclico quando ele se move além dos
    limites laterais da matriz do jogo."""

    destroyed = False  # devolve True se o canhao foi destruido
    if direcao == DIREITA and matriz[LINHA_MAXIMA][COLUNA_MAXIMA] == CANHAO:
        if matriz[LINHA_MAXIMA][0] == LASER_NAVE:
            matriz[LINHA_MAXIMA][COLUNA_MAXIMA] = " "
            matriz[LINHA_MAXIMA][0] = " "
            matriz[LINHA_MAXIMA][0] = EXPLOSAO
            destroyed = True
        else:
            matriz[LINHA_MAXIMA][COLUNA_MAXIMA] = " "
            matriz[LINHA_MAXIMA][0] = CANHAO
    else:
        moveu = False
        j = 0
        while j <= COLUNA_MAXIMA and not moveu:
            if (
                matriz[LINHA_MAXIMA][j] == CANHAO
                and matriz[LINHA_MAXIMA][j + direcao] != LASER_NAVE
            ):
                matriz[LINHA_MAXIMA][j] = " "
                matriz[LINHA_MAXIMA][j + direcao] = CANHAO
                moveu = True
            elif (
                matriz[LINHA_MAXIMA][j] == CANHAO
                and matriz[LINHA_MAXIMA][j + direcao] == LASER_NAVE
            ):
                matriz[LINHA_MAXIMA][j] = " "
                matriz[LINHA_MAXIMA][j + direcao] = EXPLOSAO
                destroyed = True
            j += 1
    return destroyed


# Passo 2: segunda função para mover algum elemento que emite lasers.
# Nesse caso para mover as naves.
def moveNaves(direcao, matriz):
    """int, (matriz) -> [bool, int, int]

    Recebe um inteiro com a direcao (valores definidos em ESQUERDA,
    DIREITA e BAIXO) para mover as naves (caracter definido em NAVE) e a
    matriz de caracteres do jogo, para mover as naves nessa direção. Ao
    mover tem que observar se chegou em algum extremo da matriz, se
    atingiu o canhão do jogador e se atingiu algum laser do jogador. No
    primeiro e no segundo caso precisa informar que isso aconteceu e no
    terceiro caso precisa atualizar a quantidade de naves atingidas
    porque a função retorna esses valores numa lista. No segundo caso tem
    que colocar o caracter definido em EXPLOSAO e no terceiro caso a nave
    tem que sumir da matriz.

    Retorna:

    [True se canhão do jogador foi atingido (False se não), limite atingido, quantidade de naves atingidas]

    Onde limite atingido tem os seguintes significados:

    - valor definido em ATINGIU_DIREITA se alguma nave após o movimento chegou em COLUNA_MAXIMA
    - valor definido em ATINGIU_ESQUERDA se alguma nave após o movimento chegou na coluna 0
    - valor definido em ATINGIU_EMBAIXO se alguma nave após o movimento chegou na linha LINHA_MAXIMA
    - 0 caso nenhuma das alternativas anteriores tenha acontecido

    Obs.: mesmo que a primeira nave verificada atinja o canhão ou atinja
    a linha mais baixa da matriz, tem que varrer a matriz **inteira** para
    atualizar a quantidade de naves atingidas antes de retornar"""

    navesAtingidas = 0  # salva o numero de naves atingidas
    lista_return = [" ", " ", " "]  # lista que será retornada
    destroyed = False

    if direcao == DIREITA:
        for i in range(LINHA_MAXIMA):
            for j in range(COLUNA_MAXIMA, -1, -1):
                if matriz[i][j] == NAVE and matriz[i][j + 1] == LASER_CANHAO:
                    matriz[i][j] = " "
                    matriz[i][j + 1] = " "
                    navesAtingidas += 1
                elif matriz[i][j] == NAVE and matriz[i][j + 1] != LASER_CANHAO:
                    matriz[i][j] = " "
                    matriz[i][j + 1] = NAVE
        for k in range(LINHA_MAXIMA):
            if matriz[k][COLUNA_MAXIMA] == NAVE:
                lista_return[1] = ATINGIU_DIREITA

    elif direcao == ESQUERDA:
        for i in range(LINHA_MAXIMA):
            for j in range(COLUNA_MAXIMA + 1):
                if matriz[i][j] == NAVE and matriz[i][j - 1] == LASER_CANHAO:
                    matriz[i][j] = " "
                    matriz[i][j - 1] = " "
                    navesAtingidas += 1
                elif matriz[i][j] == NAVE and matriz[i][j - 1] != LASER_CANHAO:
                    matriz[i][j] = " "
                    matriz[i][j - 1] = NAVE
        for k in range(LINHA_MAXIMA):
            if matriz[k][0] == NAVE:
                lista_return[1] = ATINGIU_ESQUERDA

    elif direcao == BAIXO:
        for i in range(LINHA_MAXIMA, -1, -1):
            for j in range(COLUNA_MAXIMA + 1):
                if matriz[i][j] == NAVE and matriz[i + 1][j] == LASER_CANHAO:
                    matriz[i][j] = " "
                    matriz[i + 1][j] = " "
                    navesAtingidas += 1
                elif matriz[i][j] == NAVE and matriz[i + 1][j] == CANHAO:
                    matriz[i][j] = " "
                    matriz[i + 1][j] = EXPLOSAO
                    destroyed = True
                elif matriz[i][j] == NAVE:
                    matriz[i][j] = " "
                    matriz[i + 1][j] = NAVE
        for k in range(COLUNA_MAXIMA + 1):
            if matriz[LINHA_MAXIMA][k] == NAVE:
                lista_return[1] = ATINGIU_EMBAIXO

    lista_return[0] = destroyed
    lista_return[2] = navesAtingidas
    return lista_return


# Passo 3: primeira função para emitir lasers. Nesse caso, para emitir
# um novo laser pelo canhão do jogador.
def emiteLaserCanhao(matriz):
    """(matriz) -> [int, int]

    Recebe a matriz do jogo e emite um novo laser atirado pelo jogador
    (caracter definido em LASER_CANHAO) uma posição acima da posição onde
    o canhão se encontra.  Ao emitir o laser já tem que observar: se
    atingiu alguma nave e se atingiu algum laser de alguma nave. Em todos
    esses casos o laser recém-emitido já tem que sumir da matriz (ele nem
    chega a ser impresso nesse caso) e tem que atualizar a quantidade de
    naves atingidas e de lasers atingidos pois a função retorna esses
    dois valores numa lista.

    Retorna:

    [quantidade de naves atingidas, quantidade de lasers atingidos]"""

    lasers_Atingidos = 0  # salva o numero de lasers atingidos
    navesAtingidas = 0  # salva o numero de naves atingidas
    lista_return = [" ", " "]

    for i in range(COLUNA_MAXIMA + 1):
        if matriz[LINHA_MAXIMA][i] == CANHAO:
            if matriz[LINHA_MAXIMA - 1][i] == LASER_NAVE:
                matriz[LINHA_MAXIMA - 1][i] = " "
                lasers_Atingidos += 1
            elif matriz[LINHA_MAXIMA - 1][i] == NAVE:
                matriz[LINHA_MAXIMA - 1][i] = " "
                navesAtingidas += 1
            else:
                matriz[LINHA_MAXIMA - 1][i] = LASER_CANHAO

    lista_return[0] = navesAtingidas
    lista_return[1] = lasers_Atingidos
    return lista_return


# Passo 3: segunda função para emitir lasers. Nesse caso para emitir
# novos lasers pelas naves.
def emiteLasersNaves(matriz):
    """(matriz) -> [bool, int]

    Recebe a matriz do jogo e emite lasers pelas naves (caracter definido
    em LASER_NAVE) uma posição abaixo da posição da nave que emitiu o
    laser. Ao emitir o laser já tem que observar: se atingiu o canhão do
    jogador (caso no qual tem que imprimir um EXPLOSAO no lugar) e se
    atingiu algum laser do jogador. Em todos esses casos, o laser
    recém-emitido já tem que sumir da matriz (ele nem chega a ser impresso
    nesse caso). No primeiro caso tem que informar que o canhão do jogador
    foi atingido e no segundo caso tem que atualizar a quantidade de
    lasers atingidos pois a função retorna esses dois valores numa lista.

    Para definir se uma nave deve ou não emitir laser, sorteie um
    número aleatório entre 0 e 1 (use a função random.randint para isso),
    inclusive. Se o resultado for 0, não emita o laser para aquela nave.
    Se o resultado for 1, emita. Essa verificação só deve ser feita para
    aquelas naves que não possuem nenhuma outra imediatamente abaixo e
    sempre na ordem da esquerda para a direita da matriz.

    Retorna:

    [True se canhão do jogador foi atingido (False se não), quantidade de lasers atingidos]

    Obs.1: mesmo que o primeiro laser emitido atinja o canhão, tem que
    varrer a matriz **inteira** para atualizar a quantidade de lasers
    atingidos antes de retornar"""

    destroyed = False
    lasers_atingidos = 0
    lista_return = [" ", " "]

    for i in range(LINHA_MAXIMA, -1, -1):
        for j in range(COLUNA_MAXIMA + 1):
            if matriz[i][j] == NAVE and matriz[i + 1][j] != NAVE:
                r = random.randint(0, 1)
                if matriz[i + 1][j] == LASER_CANHAO and r == 1:
                    matriz[i + 1][j] = " "
                    lasers_atingidos += 1
                elif matriz[i + 1][j] == CANHAO and r == 1:
                    matriz[i + 1][j] = EXPLOSAO
                    destroyed = True
                elif r == 1:
                    matriz[i + 1][j] = LASER_NAVE

    lista_return[0] = destroyed
    lista_return[1] = lasers_atingidos
    return lista_return


# Passo 4: primeira função para mover lasers. Nesse caso, para mover
# os lasers do jogador.
def moveLasersCanhao(matriz):
    """(matriz) -> [int, int]

    Recebe a matriz do jogo e move todos os lasers atirados pelo jogador
    (caracter definido em LASER_CANHAO) uma posição para cima na matriz.
    Ao mover tem que observar: se saiu do limite da matriz, se atingiu
    alguma nave e se atingiu algum laser de alguma nave. Em todos esses 3
    casos o laser movido tem que sumir da matriz. Nos dois primeiros
    casos tem que atualizar a quantidade de naves atingidas e de lasers
    atingidos pois a função retorna esses dois valores numa lista.

    Retorna:

    [quantidade de naves atingidas, quantidade de lasers atingidos]"""

    navesAtingidas = 0
    lasers_atingidos = 0
    lista_return = [" ", " "]

    for k in range(COLUNA_MAXIMA + 1):  # apaga os lasers que vao sair da matriz
        if matriz[0][k] == LASER_NAVE:
            matriz[0][k] = " "

    for i in range(1, LINHA_MAXIMA, 1):
        for j in range(COLUNA_MAXIMA + 1):
            if matriz[i][j] == LASER_CANHAO:
                if matriz[i - 1][j] == LASER_NAVE:
                    matriz[i][j] = " "
                    matriz[i - 1][j] = " "
                    lasers_atingidos += 1
                elif matriz[i - 1][j] == NAVE:
                    matriz[i][j] = " "
                    matriz[i - 1][j] = " "
                    navesAtingidas += 1
                else:
                    matriz[i - 1][j] = LASER_CANHAO
                    matriz[i][j] = " "
    lista_return[0] = navesAtingidas
    lista_return[1] = lasers_atingidos
    return lista_return


# Passo 4: segunda função para mover lasers. Nesse caso, para
# mover os lasers das naves.
def moveLasersNaves(matriz):
    """(matriz) -> [bool, int]

    Recebe a matriz do jogo e move todos os lasers atirados pelas naves
    (caracter definido em LASER_NAVE) uma posição para baixo na matriz.
    Ao mover tem que observar: se saiu do limite da matriz, se atingiu o
    canhão do jogador (caso no qual tem que imprimir um EXPLOSAO no lugar)
    e se atingiu algum laser do jogador. Em todos esses 3 casos, o laser
    movido tem que sumir da matriz. No segundo caso tem que informar que o
    canhão do jogador foi atingido e no terceiro caso tem que atualizar a
    quantidade de lasers atingidos pois a função retorna esses dois
    valores numa lista.

    Retorna:

    [True se canhão do jogador foi atingido (False se não), quantidade de lasers atingidos]

    Obs.: mesmo que o primeiro laser verificado atinja o canhão, tem que
    varrer a matriz **inteira** para atualizar a quantidade de lasers
    atingidos antes de retornar"""

    destroyed = False
    lasers_atingidos = 0
    lista_return = [" ", " "]
    for k in range(COLUNA_MAXIMA + 1):
        if matriz[LINHA_MAXIMA][k] == LASER_NAVE:
            matriz[LINHA_MAXIMA][k] = " "
    for i in range(LINHA_MAXIMA - 1, -1, -1):
        for j in range(COLUNA_MAXIMA + 1):
            if matriz[i][j] == LASER_NAVE:
                if matriz[i + 1][j] == CANHAO:
                    matriz[i][j] = " "
                    matriz[i + 1][j] = EXPLOSAO
                    destroyed = True
                elif matriz[i + 1][j] == LASER_CANHAO:
                    matriz[i + 1][j] = " "
                    matriz[i][j] = " "
                    lasers_atingidos += 1
                else:
                    matriz[i][j] = " "
                    matriz[i + 1][j] = LASER_NAVE
    lista_return[0] = destroyed
    lista_return[1] = lasers_atingidos
    return lista_return


# Passo 5: a função que de fato implementa o jogo segundo as regras do
# enunciado. Ela vai chamar toda as funções implementadas nos passos
# anteriores.
def joga(quantidadeNaves):
    """int -> [bool, int]

    Recebe um inteiro que representa a quantidade de naves, implementa de
    fato o jogo de acordo com as regras do enunciado e retorna uma lista
    com o resultado do jogo:

    [resultado, pontuacao]

    resultado é uma variável booliana que vale True se o jogador venceu ou
    False se o jogador perdeu.

    Para o jogador vencer:
    - O jogador precisa destruir todas as naves

    Para o jogador perder:
    - O jogador precisa ser atingido pelo tiro de alguma nave
    - Ou alguma nave precisa alcançar a linha LINHA_MAXIMA da matriz do jogo
    - Ou o jogador precisa ser atingido por alguma nave

    pontuacao é uma variável inteira que armazena a quantidade de pontos
    que o jogador fez. A pontuação é definida da seguinte forma:

    +PONTOS_ACERTOU_LASER pontos se o jogador consegue acertar 1 tiro em alguma nave
    +PONTOS_ACERTOU_NAVE  pontos se o jogador consegue acertar 1 tiro em algum tiro de alguma nave

    A ordem das ações no jogo é:
    - tiros anteriores do jogador se movem
    - imprime o estado do jogo na tela
    - usuário informa se quer atirar ou se mover e a ação escolhida é realizada
    - tiros anteriores das naves se movem
    - naves atiram (de acordo com o sorteio de números aleatórios)
    - naves se movem (de acordo com a rodada - se move apenas nas pares: direita, baixo, esquerda, baixo, direita, etc...

    Dentro de cada função de movimentação e de emissão de lasers é
    necessário verificar se houve colisões para aumentar a pontuação, para
    terminar o jogo ou para limpar a tela removendo os elementos que
    sumiram por terem passado do limite da tela (tiros que subiram demais
    e tiros que desceram demais)

    Sempre que o jogo terminar, deve imprimir o status final da
    matriz do jogo"""

    # Criação da matriz que manterá o estado do jogo.
    matriz = []
    for i in range(LINHA_MAXIMA + 1):
        matriz.append([" "] * (COLUNA_MAXIMA + 1))

    # Loop do jogo
    resultado = VENCEU
    fimDeJogo = False
    pontos = 0
    rodada = 1
    direcaoNaves = DIREITA
    segundaDirecao = 0
    criaElementos(quantidadeNaves, matriz)
    while not fimDeJogo:
        # complete o loop seguindo a ordem das ações explicada no
        # enunciado e no docstring desta função acima.
        t = moveLasersCanhao(matriz)
        pontos += PONTOS_ACERTOU_NAVE * t[0]
        pontos += PONTOS_ACERTOU_LASER * t[1]
        quantidadeNaves = quantidadeNaves - t[0]
        if quantidadeNaves == 0:
            fimDeJogo = True
            resultado = VENCEU
            imprimeMatriz(matriz)
            return [resultado, pontos]

        imprimeMatriz(matriz)

        play = input("’e’ para esquerda, ’d’ para direita e ’l’ para emitir laser:")
        if play == "e":
            direcao = ESQUERDA
            w = moveCanhao(direcao, matriz)
            if w == True:
                fimDeJogo = True
                resultado = PERDEU
                imprimeMatriz(matriz)
                return [resultado, pontos]
        elif play == "d":
            direcao = DIREITA
            w = moveCanhao(direcao, matriz)
            if w == True:
                fimDeJogo = True
                resultado = PERDEU
                imprimeMatriz(matriz)
                return [resultado, pontos]
        elif play == "l":
            y = emiteLaserCanhao(matriz)
            pontos += PONTOS_ACERTOU_NAVE * y[0]
            pontos += PONTOS_ACERTOU_LASER * y[1]
            quantidadeNaves = quantidadeNaves - y[0]
            if quantidadeNaves == 0:
                fimDeJogo = True
                resultado = VENCEU
                imprimeMatriz(matriz)
                return [resultado, pontos]

        z = moveLasersNaves(matriz)
        pontos += PONTOS_ACERTOU_LASER * z[1]
        if z[0] == True:
            fimDeJogo = True
            resultado = PERDEU
            imprimeMatriz(matriz)
            return [resultado, pontos]

        x = emiteLasersNaves(matriz)
        pontos += PONTOS_ACERTOU_LASER * x[1]
        if x[0] == True:
            fimDeJogo = True
            resultado = PERDEU
            imprimeMatriz(matriz)
            return [resultado, pontos]

        if rodada % 2 == 0:
            direcao = direcaoNaves
            if direcao == BAIXO:
                g = moveNaves(direcao, matriz)
                direcaoNaves = segundaDirecao
                pontos += PONTOS_ACERTOU_NAVE * g[2]
                quantidadeNaves -= g[2]
                if g[0] == True or g[1] == ATINGIU_EMBAIXO:
                    fimDeJogo = True
                    resultado = PERDEU
                    imprimeMatriz(matriz)
                    return [resultado, pontos]
                if quantidadeNaves == 0:
                    fimDeJogo = True
                    resultado = VENCEU
                    imprimeMatriz(matriz)
                    return [resultado, pontos]
            elif direcao == ESQUERDA:
                g = moveNaves(direcao, matriz)
                pontos += PONTOS_ACERTOU_NAVE * g[2]
                quantidadeNaves -= g[2]
                if g[1] == ATINGIU_ESQUERDA:
                    direcaoNaves = BAIXO
                    segundaDirecao = DIREITA
                if g[0] == True:
                    fimDeJogo = True
                    resultado = PERDEU
                    imprimeMatriz(matriz)
                    return [resultado, pontos]
                if quantidadeNaves == 0:
                    fimDeJogo = True
                    resultado = VENCEU
                    imprimeMatriz(matriz)
                    return [resultado, pontos]
            elif direcao == DIREITA:
                g = moveNaves(direcao, matriz)
                pontos += PONTOS_ACERTOU_NAVE * g[2]
                quantidadeNaves -= g[2]
                if g[1] == ATINGIU_DIREITA:
                    direcaoNaves = BAIXO
                    segundaDirecao = ESQUERDA
                if g[0] == True:
                    fimDeJogo = True
                    imprimeMatriz(matriz)
                    return [resultado, pontos]
                if quantidadeNaves == 0:
                    fimDeJogo = True
                    resultado = VENCEU
                    imprimeMatriz(matriz)
                    return [resultado, pontos]
        rodada += 1
    return [resultado, pontos]


if __name__ == "__main__":
    main()
