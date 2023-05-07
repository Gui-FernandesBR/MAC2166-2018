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
  Turma: 4    (eng. civil)
  Prof.: André Fujita

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma referência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
"""


def main(dificuldade, n):
    # parâmetros para os geradores congruentes lineares
    a = 22695477
    b = 1
    m = 2**32  # modulo
    x = 3  # semente

    # contadores
    g = 1
    z = 2
    k = 1  # indicador para o numero da partida
    estrela = str("*")  # string para barra de resultados
    score_jogador = 0  # pontuação do jogador
    score_maquina = 0  # pontuação da maquina
    lance10 = 0
    lance00 = 0
    lance11 = 0
    lance01 = 0
    anterior = 1  # apenas precisei definir a variável, o numero 1 é arbitrário

    # Definir o modo fácil
    while g <= z and dificuldade == 1 and k <= n:
        aleatorio = (a * x + b) % m
        x = aleatorio
        if x <= 2**31:
            computer_play = 0  # jogada da maquina
        else:
            computer_play = 1  # jogada da maquina
        jogador_play = int(input("Faca sua %da jogada:" % (k)))  # jogador
        if jogador_play == computer_play:
            print(
                "jogador = %d maquina = %d Maquina ganha!"
                % (jogador_play, computer_play)
            )
            score_maquina += 1  # maquina ganha um ponto
        else:
            print(
                "jogador = %d maquina = %d Jogador ganha!"
                % (jogador_play, computer_play)
            )
            score_jogador += 1  # jogador ganha um ponto

        # Imprimir o placar
        print("JOGADOR:", estrela * score_jogador)
        print("MAQUINA:", estrela * score_maquina)

        # Atualizar os contadores
        k += 1
        z += 1
        g += 1

        # usei ifs para o resultado final do jogo, achei melhor não colocar else
        if k > n and score_jogador > score_maquina:
            print("Voce venceu!")
        if k > n and score_jogador < score_maquina:
            print("A maquina venceu!")
        if k > n and score_jogador == score_maquina:
            print("Houve empate!")

    # Definir o modo difícil
    # utilizei vários if, eles estão "fora de ordem" mas funciona
    while g < z and dificuldade == 2 and k <= n:
        aleatorio = (a * x + b) % m
        x = aleatorio
        if x <= 2**31:
            aleatorio_play = 0
        else:
            aleatorio_play = 1
        g += 1

        if k > 2 and atual == 0:
            if lance10 > lance00:
                computer_play = 1
            if lance10 < lance00:
                computer_play = 0
            if lance10 == lance00:
                computer_play = aleatorio_play
        if k > 2 and atual == 1:
            if lance11 > lance01:
                computer_play = 1
            if lance11 < lance01:
                computer_play = 0
            if lance11 == lance01:
                computer_play = aleatorio_play

        if k > 2:
            jogador_play = int(input("Faca sua %da jogada:" % (k)))
            anterior = atual
            atual = jogador_play
            k += 1
            if jogador_play == computer_play:
                score_maquina += 1
                print(
                    "jogador = %d maquina = %d Maquina ganha!"
                    % (jogador_play, computer_play)
                )
            else:
                score_jogador += 1
                print(
                    "jogador = %d maquina = %d Jogador ganha!"
                    % (jogador_play, computer_play)
                )
            print("JOGADOR:", estrela * score_jogador)
            print("MAQUINA:", estrela * score_maquina)

        if k == 2:  # este é o if usado na segunda rodada
            computer_play = aleatorio_play
            jogador_play = int(input("Faca sua %da jodada:" % (k)))
            anterior = atual
            atual = jogador_play
            k += 1
            if jogador_play == computer_play:
                score_maquina += 1
                print(
                    "jogador = %d maquina = %d Maquina ganha!"
                    % (jogador_play, computer_play)
                )
            else:
                score_jogador += 1
                print(
                    "jogador = %d maquina = %d Jogador ganha!"
                    % (jogador_play, computer_play)
                )
            print("JOGADOR:", estrela * score_jogador)
            print("MAQUINA:", estrela * score_maquina)

        # logo abaixo, acontece o reajuste dos contadores de lance
        # a partir da terceira rodada, a cada rodada, um contador é alterado
        if k > 2 and anterior == 0 and atual == 0:
            lance00 += 1
        if k > 2 and anterior == 0 and atual == 1:
            lance10 += 1
        if k > 2 and anterior == 1 and atual == 0:
            lance01 += 1
        if k > 2 and anterior == 1 and atual == 1:
            lance11 += 1

        if k == 1:  # este é o if para a primeira rodada
            computer_play = aleatorio_play
            jogador_play = int(input("Faca sua %da jodada:" % (k)))
            atual = jogador_play
            # anterior=atual
            k += 1
            if jogador_play == computer_play:
                score_maquina += 1
                print(
                    "jogador = %d maquina = %d Maquina ganha!"
                    % (jogador_play, computer_play)
                )
            else:
                score_jogador += 1
                print(
                    "jogador = %d maquina = %d Jogador ganha!"
                    % (jogador_play, computer_play)
                )
            print("JOGADOR:", estrela * score_jogador)
            print("MAQUINA:", estrela * score_maquina)
        z += 1
        # 3 if para imprimir o vencedor
        if k > n and score_jogador > score_maquina:
            print("Voce venceu!")
        if k > n and score_jogador < score_maquina:
            print("A maquina venceu!")
        if k > n and score_jogador == score_maquina:
            print("Houve empate!")


if __name__ == "__main__":
    # usuário define a dificuldade do jogo e o numero de jogadas
    dificuldade = int(input("Escolha o tipo de jogo (1:fácil ou 2:difícil)"))
    n = int(input("Entre com o numero de jogadas:"))

    if dificuldade != 1 and dificuldade != 2:
        print("Dificuldade invalida")
    else:
        if n <= 0:
            print("Numero de jogadas invalido")
        else:
            main(dificuldade, n)
