################Jogo_Pedra_Papel_Tesoura(JoKenPo)_by_Ezequiel_Felipe_Borgelt######################

# Importando as bibliotecas Necessárias
import os
from random import randint

# Criando a variavel que irá armazenar nossas opcoes randomicas
itens = ('Pedra', 'Papel', 'Tesoura')

# Recebendo o nome do Jogador
nome_jogador = input('Qual é o seu nome? ')
print(" ")

# Função que da as boas vindas
# Ja de inicio peço para limpar a tela


def dar_boas_vindas_personalizadas(nome):
    os.system("cls")
    print(f'{nome} Bem-Vindo(a) ao jogo de JoKenPo')


dar_boas_vindas_personalizadas(nome_jogador)

# Criando a variavel Escolha que fará o controle de permanecer ou sair do jogo quando precionar s.
escolha = ''
while escolha != 's':

    # O Robo vai jogar entre 0,1 e 2, por isso o randint de 0,2.
    robo = randint(0, 2)
    print('''\nEscolha uma das opções abaixo para jogar:
    [0] Pedra
    [1] Papel
    [2] Tesoura \n ''')

    # Questiona a escolha do Jogodor e armazena na variavel Jogador.
    jogador = int(input('Qual é a sua escolha? '))

    # Teste de condição para validar a opção escolhida pelo jogador e dar a opção de sair caso ele quiera antes mesmo de começar a jogar.
    while jogador != 0 and jogador != 1 and jogador != 2 and jogador != 5:
        jogador = int(
            input('Opção Inválida, Escolha novamente ou precione 5 para Sair. '))
    else:
        if jogador == 5:
            os.system("cls")
            print('\nObrigado por participar do Jogo.')
            break

        # Se não saiu do jogo, abaixo ja recebe as jogadas e apresenta na tela
        else:
            print('~' * 25)
            print('Você escolheu {}'.format(itens[jogador]))
            print('O Robo escolheu {}'.format(itens[robo]))
            print('~' * 25)
            print(" ")

            # Função que analisa as jogadas do Jogador e do Computador e mostra o resultado.
            def analisa_jogada():

                # Função quando o Robo escolher a opção Pedra.
                def robo_jogou_Pedra():
                    if robo == 0:  # Robo escolheu 0 (Pedra)
                        if jogador == 0:
                            print('Voce Empatou com o Robo')
                        elif jogador == 1:
                            print('***** Voce Venceu, Parabéns *****')
                        elif jogador == 2:
                            print('Voce perdeu, que pena, O Robo esta com Sorte.')
                robo_jogou_Pedra()

                # Função quando o Robo escolher a opção Papel.
                def robo_jogou_Papel():
                    if robo == 1:  # Robo escolheu 1 (Papel)
                        if jogador == 0:
                            print('Voce perdeu, que pena, O Robo esta com Sorte.')
                        elif jogador == 1:
                            print('Voce Empatou com o Robo')
                        elif jogador == 2:
                            print('***** Voce Venceu, Parabéns *****')
                robo_jogou_Papel()

                # Função quando o Robo escolher a opção Tesoura
                def robo_jogou_Tesoura():
                    if robo == 2:  # Robo escolheu 2 (Tesoura)
                        if jogador == 0:
                            print('***** Voce Venceu, Parabéns *****')
                        elif jogador == 1:
                            print('Voce perdeu, que pena, O Robo esta com Sorte.')
                        elif jogador == 2:
                            print('Voce Empatou com o Robo')
                robo_jogou_Tesoura()

            analisa_jogada()

            # Apos terminar a jogada, pergunto ao Jogador se ele deseja continuar ou prefere Sair do Jogo.
            escolha = input(
                f'\nVoce deseja continuar jogando? Precione S para Sair ou C para Continuar. ')
            if escolha == 's':
                os.system("cls")
                print('\nObrigado por participar do Jogo.')
            else:
                os.system("cls")
