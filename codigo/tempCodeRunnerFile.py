def jogo_da_velha():
    tabuleiro = [[" " for i in range(3)] for i in range(3)]  # Cria a matriz 3x3

    def mostrar_tabuleiro(tabuleiro):
        for i in range(3):
            print(" | ".join(tabuleiro[i]))
            if i < 2:
                print("-" * 9)

    def verificar_vitoria(tabuleiro, jogador):
        for linha in tabuleiro:
            if all(casa == jogador for casa in linha):
                return True
        for col in range(3):
            if all(tabuleiro[linha][col] == jogador for linha in range(3)):
                return True
        if all(tabuleiro[i][i] == jogador for i in range(3)):
            return True
        if all(tabuleiro[i][2 - i] == jogador for i in range(3)):
            return True
        return False

    def verificar_empate(tabuleiro):
        for linha in tabuleiro:
            if " " in linha:
                return False
        return True

    jogador = 'X'

    while True:
        mostrar_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador}")

        linha = int(input('Digite a linha (0, 1 ou 2): '))
        coluna = int(input('Digite a coluna (0, 1 ou 2): '))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador

            if verificar_vitoria(tabuleiro, jogador):
                mostrar_tabuleiro(tabuleiro)
                print(f"Jogador {jogador} venceu!")
                break

            if verificar_empate(tabuleiro):
                mostrar_tabuleiro(tabuleiro)
                print("Empate!")
                break

            jogador = 'O' if jogador == 'X' else 'X'
        else:
            print("Essa posição já está ocupada! Tente novamente.")
            continue

# Chamada da função:
jogo_da_velha()