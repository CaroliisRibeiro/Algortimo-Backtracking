import sys


def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('| ' + ' | '.join(linha) + ' |')
        
    print()
    
    
def movimento_valido(tabuleiro, linha, coluna):
    return (
        0 <= linha < len(tabuleiro)
        and 0 <= coluna < len(tabuleiro[0])
        and tabuleiro[linha][coluna] == ' '
    )

def chegou_destino(linha, coluna):
    return linha == 0 and coluna == 3



def proximo_movimento(tabuleiro, linha_atual, coluna_atual, profundidade):
    if chegou_destino(linha_atual, coluna_atual):
        return linha_atual, coluna_atual, profundidade

    melhor_profundidade = sys.maxsize
    melhor_linha, melhor_coluna = linha_atual, coluna_atual

    direcoes = [(0,1), (0,-1), (-1,0), (1,0)]

    for dx, dy in direcoes:
        nova_linha = linha_atual + dx
        nova_coluna = coluna_atual + dy

        if movimento_valido(tabuleiro, nova_linha, nova_coluna):
            tabuleiro[nova_linha][nova_coluna] = '*'
            _, _, profundidade_atual = proximo_movimento(
                tabuleiro, nova_linha, nova_coluna, profundidade + 1
            )

            if profundidade_atual < melhor_profundidade:
                melhor_linha, melhor_coluna = nova_linha, nova_coluna
                melhor_profundidade = profundidade_atual

            tabuleiro[nova_linha][nova_coluna] = ' '  # desfaz o passo (backtrack)

    return melhor_linha, melhor_coluna, melhor_profundidade



def main():
    tabuleiro = [
        [' ', ' ', ' ', ' '],
        [' ', 'X', 'X', ' '],
        [' ', 'X', 'X', ' '],
        ['*', ' ', ' ', 'X'],
    ]

    linha_atual, coluna_atual = 3, 0
    mostrar_tabuleiro(tabuleiro)

    while not chegou_destino(linha_atual, coluna_atual):
        nova_linha, nova_coluna, profundidade = proximo_movimento(tabuleiro, linha_atual, coluna_atual, 0)

        if profundidade == sys.maxsize:
            print("Não há caminho possível.")
            return

        linha_atual, coluna_atual = nova_linha, nova_coluna
        tabuleiro[linha_atual][coluna_atual] = '*'
        mostrar_tabuleiro(tabuleiro)

main()
