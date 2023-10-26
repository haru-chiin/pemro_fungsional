import random

def create_board(width, height):
    return [['-' for _ in range(width)] for _ in range(height)]

def display_board(board, player_pos, goal_pos):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (i, j) == player_pos:
                print('A', end='')
            elif (i, j) == goal_pos:
                print('O', end='')
            else:
                print(board[i][j], end='')
        print()

def move(board, player_pos, move_direction):
    row, col = player_pos
    new_row, new_col = row, col

    if move_direction == 'w' and row > 0:
        new_row -= 1
    elif move_direction == 's' and row < len(board) - 1:
        new_row += 1
    elif move_direction == 'a' and col > 0:
        new_col -= 1
    elif move_direction == 'd' and col < len(board[0]) - 1:
        new_col += 1

    if (new_row, new_col) != player_pos:
        if board[new_row][new_col] == '-':
            board[new_row][new_col] = 'A'
        else:
            board[row][col] = '-'
            board[new_row][new_col] = 'A'
        player_pos = (new_row, new_col)

    return board, player_pos


def is_winner(player_pos, goal_pos):
    return player_pos == goal_pos

def play_game():

    while True:
        board = create_board(width, height)

        while True:
            try:
                player_pos = random.choice([(i, j) for i in range(height) for j in range(width)])
                goal_pos = random.choice([(i, j) for i in range(height) for j in range(width) if (i, j) != player_pos])
            except IndexError:
                print("Tidak cukup sel kosong untuk tujuan atau pemain.")
                return

            print("Selamat datang di permainan!")
            display_board(board, player_pos, goal_pos)

            num_retries = 3  
            for _ in range(num_retries):
                retry = input("Apakah Anda ingin mengacak papan lagi? (ya/tidak): ").lower()
                if retry == 'ya':
                    player_pos = random.choice([(i, j) for i in range(height) for j in range(width)])
                    goal_pos = random.choice([(i, j) for i in range(height) for j in range(width) if (i, j) != player_pos])
                    display_board(board, player_pos, goal_pos)
                else:
                    break

            while True:
                move_sequence = input("Masukkan urutan gerakan (w/a/s/d): ")
                for move_direction in move_sequence:
                    if move_direction in ['w', 'a', 's', 'd']:
                        board, player_pos = move(board, player_pos, move_direction)
                        # display_board(board, player_pos, goal_pos)
                        if is_winner(player_pos, goal_pos):
                            display_board(board, player_pos, goal_pos)
                            print("Anda menang!")
                            break
                    else:
                        print("Masukkan gerakan yang valid (w/a/s/d).")

                else:
                    display_board(board, player_pos, goal_pos)
                    print("Anda kalah. Anda harus mencapai tujuan dalam satu giliran.")
                    break
                break      
            break
        break



if __name__ == '__main__':
    while True :
        width = int(input("Masukkan lebar papan permainan: "))
        height = int(input("Masukkan tinggi papan permainan: "))
        play_game()
        play_again = input("Apakah Anda ingin mengulang permainan? (y/n): ")
        if play_again.lower() != 'y':
            break
