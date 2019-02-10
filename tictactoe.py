board = [None] + list(range(1, 10))
WIN_COMBINATIONS = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),

    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),

    (1, 5, 9),
    (3, 5, 7),
]

def main():
    for player in 'XO' * 9:  # x starts, then o, then x, ... (max 9 moves each)
        draw()
        if is_game_over():
            break

        print("Player {0} pick your move".format(player))
        move = choose_move()
        board[move] = player
        print()

def draw():
    print(board[7], board[8], board[9])
    print(board[4], board[5], board[6])
    print(board[1], board[2], board[3])
    print()

def choose_move():
    while True:
        try:
            a = int(input())
            if a in board:
                return a
            else:
                print("\nInvalid move. Try again")
        except ValueError:
            print("\nThat's not a number. Try again")

def count_moves_done():
    count = 0
    for pos in board:
        if pos == "x" or pos == 'O':
            count += 1
    return count

def is_game_over():
    # loop over all win_combinations
    for win_combination in WIN_COMBINATIONS:
        # get the 3 coordinates of this win combination
        a,b,c = win_combination

        # if player has all 3 coordinates, he has won
        if board[a] == board[b] == board[c]:
            print("Player {0} wins!\n".format(board[a]))
            print("Congratulations!\n")
            return True

    total_moves_done = count_moves_done()
    if total_moves_done == 9:
        print("The game ends in a tie\n")
        return True


if __name__ == "__main__":
    main()
