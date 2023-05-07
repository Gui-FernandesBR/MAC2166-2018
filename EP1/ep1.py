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
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
"""


dific=int(input("Escolha o tipo de jogo (1:facil; 2:dificil)"))    #dificuldade do jogo
n=int(input("Entre com o numero de jogadas:"))                      #numero de jogadas
'''parametros para os geradores congruentes lineares'''
a=22695477
b=1
m=2**32           #modulo
x=3               #semente
'''contadores'''
g=1               
z=2
k=1               #indicador para o numero da partida
estrela=str("*")  #string para barra de resultados
pont_jogador=0    #pontuação do jogador
pont_maquina=0    #pontuação da maquina
lance10=0
lance00=0
lance11=0
lance01=0
anterior=10       #apenas precisei definir a variavel, o numero 10 não será utilizado

'''easy_way'''
while g<=z and dific==1 and k<=n:      
    num_aleat=(a*x+b)%m
    x=num_aleat
    if x<=2**31:
        computer_play=0     #jogada da maquina
    else:
        computer_play=1     #jogada da maquina
    jogador_play=int(input("Faca sua %da jogada:"%(k)))     #jogada do jogador 
    if jogador_play==computer_play:
        print("jogador = %d maquina = %d Maquina ganha!"%(jogador_play,computer_play))    
        pont_maquina+=1                         #maquina ganha um ponto
    else:
        print("jogador = %d maquina = %d Jogador ganha!"%(jogador_play,computer_play))     
        pont_jogador+=1                         #jogador ganha um ponto
    print("JOGADOR:",estrela*pont_jogador)      #placar
    print("MAQUINA:",estrela*pont_maquina)      #placar
    k+=1
    z+=1
    g+=1
    #3 if para o reultado final do jogo, achei melhor não colocar else
    if k>n and pont_jogador>pont_maquina:
        print("Voce venceu!")
    if k>n and pont_jogador<pont_maquina:
        print("A maquina venceu!")
    if k>n and pont_jogador==pont_maquina:
        print("Houve empate!")

'''hard_way'''  #utilizei varios if, eles estão "fora de ordem" mas, se seguir o caminho certo, no fim o resultado é o mesmo
while g<z and dific==2 and k<=n:
    num_aleat=(a*x+b)%m
    x=num_aleat
    if x<=2**31:
        aleat_play=0
    else:
        aleat_play=1
    g+=1

    if k>2 and atual==0:
        if lance10>lance00:
            computer_play=1
        if lance10<lance00:
            computer_play=0
        if lance10==lance00:
            computer_play=aleat_play
    if k>2 and atual==1:
        if lance11>lance01:
            computer_play=1
        if lance11<lance01:
            computer_play=0
        if lance11==lance01:
            computer_play=aleat_play          
        
    if k>2:
        jogador_play=int(input("Faca sua %da jogada:"%(k)))
        anterior=atual
        atual=jogador_play
        k+=1
        if jogador_play==computer_play:
            pont_maquina+=1
            print("jogador = %d maquina = %d Maquina ganha!"%(jogador_play,computer_play))
        else:
            pont_jogador+=1
            print("jogador = %d maquina = %d Jogador ganha!"%(jogador_play,computer_play))
        print("JOGADOR:",estrela*pont_jogador)
        print("MAQUINA:",estrela*pont_maquina)

    if k==2:        #este é o if usado na segunda rodada
        computer_play=aleat_play
        jogador_play=int(input("Faca sua %da jodada:"%(k)))
        anterior=atual
        atual=jogador_play
        k+=1
        if jogador_play==computer_play:
            pont_maquina+=1
            print("jogador = %d maquina = %d Maquina ganha!"%(jogador_play,computer_play))
        else:
            pont_jogador+=1
            print("jogador = %d maquina = %d Jogador ganha!"%(jogador_play,computer_play))
        print("JOGADOR:",estrela*pont_jogador)
        print("MAQUINA:",estrela*pont_maquina)
    #logo abaixo, acontece o reajuste dos contadores de lance
    #a partir da terceira rodada, a cada rodada, um contador é alterado
    if k>2 and anterior==0 and atual==0:
        lance00+=1
    if k>2 and anterior==0 and atual==1:
        lance10+=1
    if k>2 and anterior==1 and atual==0:
        lance01+=1
    if k>2 and anterior==1 and atual==1:
        lance11+=1    
            
    if k==1:        #este é o if para a primeira rodada
        computer_play=aleat_play
        jogador_play=int(input("Faca sua %da jodada:"%(k)))
        atual=jogador_play
        #anterior=atual
        k+=1
        if jogador_play==computer_play:
            pont_maquina+=1
            print("jogador = %d maquina = %d Maquina ganha!"%(jogador_play, computer_play))
        else:
            pont_jogador+=1
            print("jogador = %d maquina = %d Jogador ganha!"%(jogador_play, computer_play))
        print("JOGADOR:",estrela*pont_jogador)
        print("MAQUINA:",estrela*pont_maquina)
    z+=1
    #3 if para imprimir o vencedor
    if k>n and pont_jogador>pont_maquina:
        print("Voce venceu!")
    if k>n and pont_jogador<pont_maquina:
        print("A maquina venceu!")
    if k>n and pont_jogador==pont_maquina:
        print("Houve empate!")
