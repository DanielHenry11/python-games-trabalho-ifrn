import random  # Importa a biblioteca random para gerar números aleatórios
import time    # Importa a biblioteca time para usar pausas temporais (como o sleep)

# Função do jogo da adivinhação
def jogo_adivinhação():
    número_secreto = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100
    tentativas = 0  # Inicializa o contador de tentativas

    print('Bem-vindo ao jogo de adivinhação!')
    print('Tente adivinhar o número que estou pensando, entre 1 e 100.')

    while True:  # Loop até o jogador acertar
        palpite = input('Digite seu palpite: ')  # Recebe o palpite do jogador
        if not palpite.isdigit():  # Verifica se o palpite é um número
            print('Digite um número válido.')
            continue  # Volta para o início do loop

        palpite = int(palpite)  # Converte o palpite para inteiro
        tentativas += 1  # Incrementa o número de tentativas

        if palpite == número_secreto:  # Verifica se o palpite está correto
            print(f'PARABÉNS! Você acertou após {tentativas} tentativas.')
            break  # Encerra o jogo se acertar
        elif palpite < número_secreto:
            print('O número é maior.')  # Dica: o número secreto é maior
        else:
            print('O número é menor.')  # Dica: o número secreto é menor

# Função principal do jogo da velha, com opção contra a máquina
def jogo_da_velha(contra_maquina=False):
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]  # Cria um tabuleiro 3x3 vazio

    # Função para exibir o tabuleiro formatado
    def mostrar_tabuleiro(tabuleiro):
        print("   0   1   2")  # Cabeçalho das colunas
        for i in range(3):
            # Exibe cada linha com separadores verticais
            print(f"{i}  {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]}")
            if i < 2:
                print("  ---+---+---")  # Linhas divisórias

    # Função para verificar se um jogador venceu
    def verificar_vitoria(tab, jogador):
        # Verifica todas as linhas
        for linha in tab:
            if all(c == jogador for c in linha):
                return True
        # Verifica todas as colunas
        for col in range(3):
            if all(tab[linha][col] == jogador for linha in range(3)):
                return True
        # Verifica diagonal principal
        if all(tab[i][i] == jogador for i in range(3)):
            return True
        # Verifica diagonal secundária
        if all(tab[i][2 - i] == jogador for i in range(3)):
            return True
        return False  # Se não houver vitória

    # Função para verificar se houve empate
    def verificar_empate(tab):
        # Retorna True se todas as casas estiverem preenchidas
        return all(c != " " for linha in tab for c in linha)

    jogador = 'X'  # O jogador 'X' sempre começa

    while True:  # Loop principal do jogo
        mostrar_tabuleiro(tabuleiro)  # Mostra o estado atual do tabuleiro
        print(f"\nVez do jogador {jogador}")  # Indica de quem é a vez

        if contra_maquina and jogador == 'O':  # Se for a vez da máquina
            print("O computador está pensando...\n")  # Mensagem de espera
            time.sleep(1.5)  # Aguarda 1.5 segundos
            # Cria uma lista com todas as jogadas possíveis (casas vazias)
            jogadas_disponiveis = [(i, j) for i in range(3) for j in range(3) if tabuleiro[i][j] == " "]
            linha, coluna = random.choice(jogadas_disponiveis)  # Escolhe uma posição aleatória
            print(f"A máquina jogou na posição {linha}, {coluna}")  # Informa a jogada da máquina
        else:
            try:
                linha = int(input("Digite a linha (0, 1 ou 2): "))  # Recebe a linha do jogador
                coluna = int(input("Digite a coluna (0, 1 ou 2): "))  # Recebe a coluna do jogador
            except ValueError:
                print("Por favor, digite apenas números válidos.")  # Caso o jogador digite letras
                continue

            if linha not in [0, 1, 2] or coluna not in [0, 1, 2]:
                print("Posição inválida. Tente novamente.")  # Fora dos limites do tabuleiro
                continue

            if tabuleiro[linha][coluna] != " ":
                print("Essa posição já está ocupada!")  # Se a casa já estiver marcada
                continue

        tabuleiro[linha][coluna] = jogador  # Marca a jogada no tabuleiro

        if verificar_vitoria(tabuleiro, jogador):  # Verifica se o jogador venceu
            mostrar_tabuleiro(tabuleiro)  # Mostra o tabuleiro final
            if contra_maquina and jogador == 'O':
                print("\n🤖 A máquina venceu!")  # Vitória da máquina
            else:
                print(f"\n🎉 Jogador {jogador} venceu!")  # Vitória do jogador humano
            break

        if verificar_empate(tabuleiro):  # Verifica se todas as casas estão preenchidas
            mostrar_tabuleiro(tabuleiro)
            print("\n🤝 Empate!")  # Mensagem de empate
            break

        jogador = 'O' if jogador == 'X' else 'X'  # Alterna entre os jogadores

# Submenu para escolher o modo do jogo da velha
def menu_jogo_da_velha():
    print('\n== JOGO DA VELHA ==')  # Título do submenu
    print('1 - Modo 2 jogadores')  # Opção para jogar entre 2 pessoas
    print('2 - Modo contra a máquina')  # Opção para jogar contra o computador
    escolha = input('Escolha um modo: ')  # Recebe a escolha do jogador

    if escolha == '1':
        jogo_da_velha(contra_maquina=False)  # Chama o modo 2 jogadores
    elif escolha == '2':
        jogo_da_velha(contra_maquina=True)  # Chama o modo contra a máquina
    else:
        print('Opção inválida. Voltando ao menu principal.')  # Caso escolha inválida

# Intruções dos jogos
def ver_instrucoes():
    print("\n=== Instruções ===")
    print("Jogo da Velha:") # Instrução do jogo da velha
    print("- O tabuleiro é 3x3.")
    print("- Dois jogadores alternam jogadas ou jogam contra a máquina.")
    print("- Ganha quem alinhar 3 símbolos (X ou O).")
    print("\nJogo da Adivinhação:") # Instrução do jogo Adivinhação
    print("- Adivinhe um número entre 1 e 100.")
    print("- O jogo dá dicas se o número é maior ou menor.")

# Menu principal do programa
def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")  # Exibe o menu principal
        print("1 - Jogo da Adivinhação")  # Primeira opção
        print("2 - Jogo da Velha")  # Segunda opção
        print("3 - Ver intruções")  # Terceira opção
        print("4 - Sair")  # Quarta opção
        escolha = input("Escolha uma opção (1, 2, 3 ou 4): ")  # Entrada da escolha

        if escolha == '1':
            jogo_adivinhação()  # Inicia o jogo de adivinhação
        elif escolha == '2':
            menu_jogo_da_velha()  # Vai para o menu do jogo da velha
        elif escolha == '3':
            ver_instrucoes() # Vai para as instruções dos jogos
        elif escolha == '4':
            print('👋 Saindo do programa. Até logo!')  # Mensagem de saída
            break  # Encerra o loop e o programa
        else:
            print('Opção inválida. Tente novamente.')  # Caso digite algo errado

# Chama o menu principal para iniciar o programa
menu()