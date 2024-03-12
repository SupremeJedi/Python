import chess

def print_board(board):
    print(board)

def main():
    board = chess.Board()

    while not board.is_game_over():
        print_board(board)
        move = input("Enter your move (in algebraic notation, e.g. e2e4): ")
        try:
            chess_move = chess.Move.from_uci(move)
            if chess_move in board.legal_moves:
                board.push(chess_move)
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid move format. Try again.")

    print("Game over. Result: " + board.result())

if __name__ == "__main__":
    main()