tabuleiro = [
  [' ', ' ', ' '],
  [' ', ' ', ' '],
  [' ', ' ', ' '],
]

jogador = 'X'

def exibeTabuleiro():
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 5)

def jogada(linha, coluna):
    if (
        not 0 <= linha <= 2 or 
        not 0 <= coluna <= 2 or 
        tabuleiro[linha][coluna] != ' '
    ):
        print('Jogada inválida!')
        return jogador
    # if not 0 <= linha <= 2:
    #     print('Jogada inválida!')
    #     return jogador
    # if not 0 <= coluna <= 2:
    #     print('Jogada inválida!')
    #     return jogador
    # if tabuleiro[linha][coluna] != ' ':
    #     print('Jogada inválida!')
    #     return jogador
    tabuleiro[linha][coluna] = jogador
    # if jogador == 'X':
    #     return 'O'
    # else:
    #     return 'X'
    return 'O' if jogador == 'X' else 'X'
# jogador = jogada(1, 1)
# jogador = jogada(1, 2)
# jogador = jogada(2, 2)

# exibeTabuleiro()
while True:
    print(f'jogador da vez: {jogador}')
    try:
        linha = int(input('Digite a linha: '))
        coluna = int(input('Digite a coluna: '))
        jogador = jogada(linha, coluna)
    # except (ValueError, IndexError):
    #     print('Digite valores numéricos entre 0 e 2')
    except IndexError:
        print('Digite valores numericos entre 0 e 2')
    except ValueError:
        print('Os valores devem ser numeros inteiros')
    #     continue
    # jogador = jogada(linha, coluna)
    exibeTabuleiro()