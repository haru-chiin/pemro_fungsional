import random

def generate_positions(height, width):
    return random.randint(0, height-1), random.randint(0, width-1)

def print_board(board):
    for row in board:
        print(' '.join(row))

def initialize_board(height, width):
    board = [['-' for _ in range(width)] for _ in range(height)]
    player_row, player_col = generate_positions(height, width)
    goal_row, goal_col = generate_positions(height, width)
    
    while (player_row, player_col) == (goal_row, goal_col):
        goal_row, goal_col = generate_positions(height, width)
    
    board[player_row][player_col] = 'A'
    board[goal_row][goal_col] = 'O'
    return board, (player_row, player_col), (goal_row, goal_col)

def move(board, position, move):
    row, col = position
    if move == 'w' and row > 0:
        row -= 1
    elif move == 's' and row < len(board) - 1:
        row += 1
    elif move == 'a' and col > 0:
        col -= 1
    elif move == 'd' and col < len(board[0]) - 1:
        col += 1
    return row, col

def is_game_won(player_position, goal_position):
    return player_position == goal_position

def is_game_lost(player_position, obstacle_positions):
    return player_position in obstacle_positions

def play_game(height, width):
    board, player_position, goal_position = initialize_board(height, width)
    obstacle_positions = {tuple(position) for position in board for row in position if row == 'X'}

    print("Selamat datang di permainan!")
    print_board(board)

    while True:
        move_input = input("Pilih gerakan (w/a/s/d): ")
        if move_input not in ['w', 'a', 's', 'd']:
            print("Masukan tidak valid. Gunakan 'w', 'a', 's', atau 'd' untuk bergerak.")
            continue

        player_position = move(board, player_position, move_input)
        print_board(board)

        if is_game_won(player_position, goal_position):
            print("Anda menang!")
            break
        elif is_game_lost(player_position, obstacle_positions):
            print("Anda kalah!")
            break

if __name__ == "__main__":
    while True:
        height = int(input("Masukkan tinggi papan: "))
        width = int(input("Masukkan lebar papan: "))
        play_game(height, width)
        
        play_again = input("Apakah Anda ingin mengulang permainan? (y/n): ")
        if play_again.lower() != 'y':
            break






