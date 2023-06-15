import random


def criar_matriz(linhas, colunas):
    matriz = []
    for _ in range(linhas):
        linha = [0] * colunas
        matriz.append(linha)
    return matriz


def mostrar_tabuleiro(tabuleiro):
    colunas = len(tabuleiro[0])
    print("  ", end="")
    for i in range(colunas):
        print(i, end=" ")
    print()
    for linha, valores in enumerate(tabuleiro):
        print(linha, end=" ")
        for valor in valores:
            print(f"[{valor}]", end=" ")
        print()


def main():
    print("Saaaalve irmãozinho, bem-vindo ao Batalha Naval do Falcão, João Pedro e Tarso")
    print("Rapaz voce ta jogando com o grande poderoso Gilberto")

    tabuleiro_player = criar_matriz(5, 10)
    tabuleiro_gilberto = criar_matriz(5, 10)

    print("\nSeu tabuleiro:")
    mostrar_tabuleiro(tabuleiro_player)

    navios_player = posicionar_navios_player(tabuleiro_player)
    navios_gilberto = posicionar_navios_gilberto(tabuleiro_gilberto)

    while True:
        print("\nSeu tabuleiro:")
        mostrar_tabuleiro(tabuleiro_player)
        print("Você tem essa quantidade de navios aí ó:", len(navios_player))

        ataque_player(tabuleiro_gilberto, navios_gilberto)
        if len(navios_gilberto) == 0:
            print("\nDesceu bala em todos os navios do Gilberto")
            print("humilhou o gilbertobas")
            break

        ataque_gilberto(tabuleiro_player, navios_player)
        if len(navios_player) == 0:
            print("\nGilberto te amassou")
            print("Você foi simplesmente destroçado pelo Gilberto")
            break


def posicionar_navios_player(tabuleiro):
    print("\nMete os navios aí rapa")
    navios = []
    tamanhos_navios = [5, 4, 4, 3, 2]

    for i, tamanho in enumerate(tamanhos_navios):
        print(f"Navio {i + 1} - {tamanho} casinhas")
        while True:
            linha = int(input(f"Digite a linha do navio {i + 1}: "))
            coluna = int(input(f"Digite a coluna do navio {i + 1}: "))

            if linha < 0 or linha >= 5 or coluna < 0 or coluna >= 10:
                print("Aí da não irmão")
                continue
            elif (linha, coluna) in navios or tabuleiro[linha][coluna] != 0:
                print("Aí não dá, já tem um navio aí ou está em cima de outro navio.")
                continue
            elif not verificar_tamanho_valido(tabuleiro, linha, coluna, tamanho):
                print("ih mano o navio não é desse tamanho aí não.")
                print(f"O navio {i + 1} tem {tamanho} casinhas ta ligado")
                continue
            else:
                break

        navios.append((linha, coluna))

        for j in range(tamanho):
            if tamanho > 1:
                tabuleiro[linha][coluna + j] = 1
            else:
                tabuleiro[linha][coluna] = 1

    mostrar_tabuleiro(tabuleiro)
    return navios


def verificar_tamanho_valido(tabuleiro, linha, coluna, tamanho):
    if coluna + tamanho <= len(tabuleiro[0]):
        for j in range(tamanho):
            if tabuleiro[linha][coluna + j] != 0:
                return False
    else:
        return False

    if linha + tamanho <= len(tabuleiro):
        for i in range(tamanho):
            if tabuleiro[linha + i][coluna] != 0:
                return False
    else:
        return False

    return True


def verificar_acerto(navios, linha, coluna):
    return (linha, coluna) in navios


def posicionar_navios_gilberto(tabuleiro):
    navios = []
    tamanhos_navios = [5, 4, 4, 3, 2]

    for tamanho in tamanhos_navios:
        linha = random.randint(0, 4)
        coluna = random.randint(0, 9)

        while not verificar_tamanho_valido(tabuleiro, linha, coluna, tamanho) or (linha, coluna) in navios:
            linha = random.randint(0, 4)
            coluna = random.randint(0, 9)

        navios.append((linha, coluna))

        for j in range(tamanho):
            if tamanho > 1:
                tabuleiro[linha][coluna + j] = 1
            else:
                tabuleiro[linha][coluna] = 1

    return navios


def ataque_player(tabuleiro_gilberto, navios_gilberto):
    print("\nSua vez")
    while True:
        linha = int(input("Manda a linha do ataque aí: "))
        coluna = int(input("Manda a coluna do ataque aí: "))
        if linha < 0 or linha >= 5 or coluna < 0 or coluna >= 10:
            print("Ih ta esquisito isso ai tenta de novo")
        else:
            break

    if verificar_acerto(navios_gilberto, linha, coluna):
        print("AEEEEEE DESCEU BALA NO HOME")
        tabuleiro_gilberto[linha][coluna] = 'X'
        navios_gilberto.remove((linha, coluna))
    else:
        print("Errou kkkkkkkkkkkk.")
        tabuleiro_gilberto[linha][coluna] = 'O'


def ataque_gilberto(tabuleiro_player, navios_player):
    print("\nHora do Gilberto meter bala em você")
    linha = random.randint(0, 4)
    coluna = random.randint(0, 9)

    if verificar_acerto(navios_player, linha, coluna):
        print("Gilberto acertou seu boboca")
        tabuleiro_player[linha][coluna] = 'X'
        navios_player.remove((linha, coluna))
    else:
        print("Gilberto errou kkkkkk ruinzão")
        tabuleiro_player[linha][coluna] = 'O'


if __name__ == "__main__":
    main()