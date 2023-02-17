from funcoes import criarBoard, printBoard, verificaGanhador, getInputValido, verificaMovimento, fazMovimento
from minimax import movimentoIA


jogador = 0  # jogador 1
board = criarBoard()
ganhador = verificaGanhador(board)
while (not ganhador):
    printBoard(board)
    print()
    print("=-=-=-=-=")
    print()
    if (jogador == 0):
        i, j = movimentoIA(board, jogador)
    else:
        i = getInputValido("Digite a linha: ")
        j = getInputValido("Digite a coluna: ")

    if (verificaMovimento(board, i, j)):
        fazMovimento(board, i, j, jogador)
        jogador = (jogador + 1) % 2
    else:
        print("A posição informado já está ocupada")

    ganhador = verificaGanhador(board)

print("=-=-=-=-=")
print()
printBoard(board)
print()
print("Ganhador = ", ganhador)
print("=-=-=-=-=")
