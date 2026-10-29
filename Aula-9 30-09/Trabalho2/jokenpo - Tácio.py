#Aluno: Tácio Ferreira Prado Filho

#Sobre o uso de IA: foi utilizado o auxilio de uma IA
#                   penas para ensinar como fazer algo, 
#                   código feito por mim.

#Assistente de IA: Github Copilot
#Prompts utilizados:
#how to clear terminal python ansi -> print("\033[H\033[2J", end="")
#How to use Try to validade input value -> saida com explicação sobre o funcionamento do Try para validar input

#função responsavel por "limpar o terminal" para manter a sensação de uma interface no terminal
def limpa_terminal():
    print("\033[H\033[2J", end="")

#Cabeçalho exibido antes do inicio do jogo
def cabecalhoInicial():
    limpa_terminal()
    print("     +---------------+")
    print("     |---JO KEN PO---|")
    print("     +---------------+")
    print("")

#Cabeçalho exibido durante o jogo
def cabecalhoJogo(jogador1, jogador2, pontosP1, pontosP2):
    limpa_terminal()
    print("     +---------------+")
    print("     |---JO KEN PO---|")
    print("     +---------------+\n")

    print("     ",jogador1,"VS",jogador2,"\n")
    print("Pontuação:")
    print(jogador1, pontosP1)
    print(jogador2, pontosP2,"\n")

    print("Jogadas: 1-Pedra  2-Papel  3-Tesoura")

#Tela exibida ao final do jogo, também valida o vencedor exibindo a respectiva mensagem
def telaFinal(jogador1, jogador2, pontosP1, pontosP2):
    limpa_terminal()
    print("     +---------------+")
    print("     |---JO KEN PO---|")
    print("     +---------------+")
    print("")
    print("Pontuação Final:")
    print(jogador1, pontosP1)
    print(jogador2, pontosP2,"\n")

    if(pontosP1 > pontosP2):
        print("Parabéns",jogador1,"Você venceu!")
    elif(pontosP1 < pontosP2):
        print("Parabéns",jogador2,"Você venceu!")
    else:
        print("Parabéns",jogador1,"e",jogador2,"Vocês empataram!")

#Funcao responsavel por ler e validar jogadas e avaliar a jogada adicionando um ponto ao vencedor 
def jogo(jogador1, jogador2):

    sair = False
    rodada = 1
    jogada = 1
    jogadaP1 = 0
    jogadaP2 = 0
    pontosP1 = 0
    pontosP2 = 0

    while(sair == False):
        cabecalhoJogo(jogador1, jogador2, pontosP1, pontosP2)

        #lendo e validando jogada do jogador1
        if(jogada == 1):
            while True:
                try:
                    jogadaP1 = int(input(jogador1+", Digite sua jogada: "))
                    
                    if jogadaP1 < 1 or jogadaP1 > 3:
                        cabecalhoJogo(jogador1, jogador2, pontosP1, pontosP2)
                        print("Jogada invalida! Digite um número entre 1 e 3.")
                        continue
                    break

                except ValueError:
                    cabecalhoJogo(jogador1, jogador2, pontosP1, pontosP2)
                    print("Jogada invalida! Digite um número entre 1 e 3.")
            
            jogada = 2

        #lendo e validando jogada do jogador 2
        if(jogada == 2):
            while True:
                try:
                    jogadaP2 = int(input(jogador2+", Digite sua jogada: "))

                    if jogadaP1 < 1 or jogadaP1 > 3:
                        cabecalhoJogo(jogador1, jogador2, pontosP1, pontosP2)
                        print("Jogada invalida! Digite um número entre 1 e 3.")
                        continue    
                    break

                except ValueError:
                    cabecalhoJogo(jogador1, jogador2, pontosP1, pontosP2)
                    print("Jogada invalida! Digite um número entre 1 e 3.")

            jogada = 1

        #jogada: pedra - *
        if(jogadaP1 == 1):
            #jogada: pedra - pedra
            if(jogadaP2 == 1):
                rodada += 1
            #jogada: pedra - papel
            elif(jogadaP2 == 2):
                pontosP2 += 1
                rodada +=1
            #jogada: pedra - tesoura
            else:
                pontosP1 +=1
                rodada +=1
        #jogada: papel - *
        elif(jogadaP1 == 2):
            #jogada: papel - pedra
            if(jogadaP2 == 1):
                pontosP1 += 1
                rodada +=1
            #jogada: papel - papel
            elif(jogadaP2 == 2):
                rodada += 1
            #jogada: papel - tesoura
            else:
                pontosP2 +=1
                rodada +=1
        #jogada: tesoura - *
        elif(jogadaP1 == 3):
            #jogada: tesoura - pedra
            if(jogadaP2 == 1):
                pontosP2 += 1
                rodada +=1
            #jogada: tesoura - papel
            elif(jogadaP2 == 2):
                pontosP1 +=1
                rodada += 1
            #jogada: tesoura - tesoura
            else:
                rodada +=1

        saida = input("Deseja continuar? S ou N:")

        if(saida == 'N' or saida == 'n'):
            sair = True
            telaFinal(jogador1, jogador2, pontosP1, pontosP2)

#Funcao principal que lê o nome dos jogadores e roda o jogo
def main():
    cabecalhoInicial()

    jogador1 = input("Digite o nome do jogador 1: ")
    jogador2 = input("Digite o nome do jogador 2: ")

    jogo(jogador1, jogador2)


main()