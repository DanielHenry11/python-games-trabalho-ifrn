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

    tabuleiro = [[" " for _ in range(3)] for _ in range(3)] # Cria uma matriz 3x3 com espaços em branco representando o tabuleiro

    def mostrar_tabuleiro(tabuleiro): # Função para mostrar o tabuleiro na tela
        for linha in tabuleiro:
            print(" | ".join(linha)) # Junta os elementos da linha com " | " e imprimi
            print("-" * 9) # Imprime uma linha separadora
