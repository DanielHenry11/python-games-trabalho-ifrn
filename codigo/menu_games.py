import random

def jogo_adivinhação():

    número_secreto = random.randint(1, 100) # Vai escolher um número entre 1 e 100
    tentativas = 0 # Aqui vai ficar armazenado quantas tentativas o teve até acerta

    print('Bem-vindo ao jogo de adivinhação!')
    print('Tente adivinhar o número que estou pensando, entre 1 e 100.')

    while True:
        palpite = input('Digite seu palpite: ') # O usuário vai digitar o seu palpite
        if not palpite.isdigit(): # Vai verificar se o que foi digitado é um número inteiro positivo
            print('Digite um número válido.')
            continue # Volta para o começo do loop

        palpite = int(palpite) # Converte o texto para número inteiro
        tentativas += 1 # Soma 1 às tentativas feitas

        if palpite == número_secreto:
            print(f'PARABÉNS! Você acertou após {tentativas} tentativas.')
            break # Sai do loop e o jogo acaba
        elif palpite < número_secreto:
            print('O número é maior.') # Dá uma dica que o número secreto é maior
        elif palpite > número_secreto:
            print('O número é menor.') # Dá uma dica que o número secreto é menor

def jogo_da_velha():
    # Cria o tabuleiro 3x3 com espaços vazios
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

    # Função para exibir o tabuleiro no terminal
    def mostrar_tabuleiro(tabuleiro):
        print("   0   1   2")  # Cabeçalho com os números das colunas
        for i in range(3):  # Para cada linha do tabuleiro
            # Mostra o número da linha e as casas separadas por |
            linha = f"{i}  {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]}"
            print(linha)
            if i < 2:  # Para as duas primeiras linhas, adiciona a linha separadora
                print("  ---+---+---")

    # Função que verifica se um jogador venceu
    def verificar_vitoria(tabuleiro, jogador):
        # Verifica se há alguma linha com 3 símbolos do jogador
        for linha in tabuleiro:
            if all(casa == jogador for casa in linha):
                return True
        # Verifica colunas
        for col in range(3):
            if all(tabuleiro[linha][col] == jogador for linha in range(3)):
                return True
        # Verifica a diagonal principal (de cima à esquerda até baixo à direita)
        if all(tabuleiro[i][i] == jogador for i in range(3)):
            return True
        # Verifica a diagonal secundária (de cima à direita até baixo à esquerda)
        if all(tabuleiro[i][2 - i] == jogador for i in range(3)):
            return True
        return False  # Se não encontrou nenhuma vitória

    # Função que verifica se o jogo empatou (tabuleiro cheio e sem vitória)
    def verificar_empate(tabuleiro):
        for linha in tabuleiro:
            if " " in linha:  # Se ainda tem espaço vazio, não é empate
                return False
        return True  # Tabuleiro cheio e sem vencedor

    jogador = 'X'  # Começa com o jogador 'X'

    while True:  # Loop principal do jogo
        mostrar_tabuleiro(tabuleiro)  # Mostra o tabuleiro
        print(f"\nVez do jogador {jogador}")  # Mostra de quem é a vez

        try:
            # Solicita ao jogador a linha e a coluna onde deseja jogar
            linha = int(input('Digite a linha (0, 1 ou 2): '))
            coluna = int(input('Digite a coluna (0, 1 ou 2): '))
        except ValueError:
            # Se o jogador digitar algo que não seja número
            print("Por favor, digite apenas números válidos.")
            continue  # Volta ao início do loop

        # Verifica se a posição digitada está dentro do tabuleiro
        if linha not in [0, 1, 2] or coluna not in [0, 1, 2]:
            print("Posição fora do tabuleiro. Tente novamente.")
            continue  # Volta ao início do loop

        # Verifica se a casa está vazia
        if tabuleiro[linha][coluna] == " ":
            # Marca a jogada no tabuleiro
            tabuleiro[linha][coluna] = jogador

            # Verifica se o jogador venceu
            if verificar_vitoria(tabuleiro, jogador):
                mostrar_tabuleiro(tabuleiro)  # Mostra o tabuleiro final
                print(f"\n🎉 Jogador {jogador} venceu!")
                break  # Encerra o jogo

            # Verifica se deu empate
            if verificar_empate(tabuleiro):
                mostrar_tabuleiro(tabuleiro)  # Mostra o tabuleiro final
                print("\n🤝 Empate!")
                break  # Encerra o jogo

            # Troca de jogador: se era X, vira O; se era O, vira X
            jogador = 'O' if jogador == 'X' else 'X'
        else:
            # A posição já está ocupada
            print("Essa posição já está ocupada! Tente novamente.")
            continue  # Volta ao início do loop

# Chama a função para iniciar o jogo
jogo_da_velha()