import random

# Printing the Game Board
def print_field(fe):
    print("{} | {} | {}".format(fe[0][0], fe[0][1], fe[0][2]))
    print("----------")
    print("{} | {} | {}".format(fe[1][0], fe[1][1], fe[1][2]))
    print("----------")
    print("{} | {} | {}\n".format(fe[2][0], fe[2][1], fe[2][2]))

# Showing the current palyer 
def current_role(pla):
    print("It's [{}] Turn".format(pla))

# Finding the position in the Board
def find(x, field):
    for i in range(3):
        for j in range(3):
            if x == field[i][j]:
                return i, j
    return None, None

# Placing "X" or "O" on the board
def play(position, c_player, field):
    x, y = find(position, field)
    if c_player == "X":
        field[x][y] = "X"
        c_player = "O"
    elif c_player == "O":
        field[x][y] = "O"
        c_player = "X"
    return c_player, field

# Checking if there is a winner
def check_winner(field):
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2]:
            return field[i][0]
    for j in range(3):
        if field[0][j] == field[1][j] == field[2][j]:
            return field[0][j]   
    if field[0][0] == field[1][1] == field[2][2]:
        return field[0][0]
    if field[0][2] == field[1][1] == field[2][0]:
        return field[0][2]
    return None

# Checking if there is a tie
def is_tie(field):
    for i in field:
        for j in i:
            if isinstance(j, int):
                return False
    return True

# Checking if the number was provided is valid one 
def is_valid_number(x):
    if x.isdigit():
        number = int(x)
        if number in range(1, 10):
            return True
    return False

# Checking if the position is empty or not
def is_valid_position(x, field):
    a, b = find(int(x), field)
    if a == None or  b==None :
            return False
    return True

# Checking if we can play or not 
def is_valid_input(x, field):
    if is_valid_number(x):
        if is_valid_position(x, field):
            return True
        else:
            print("This position is already taken, choose another.\n")
            return False
    else:
        print("Invalid position, choose a number from 1 - 9.\n")
        return False

# The main game function
def main():
    # Our game borad
    field = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    c_player = random.choice(["X", "O"])

    print_field(field)
    while True:
        current_role(c_player)
        tmp = input("Pick a position: ")
        if is_valid_input(tmp, field):
            c_player, field = play(int(tmp), c_player, field)
            winner = check_winner(field)
            print_field(field)
            if winner:
                print("Player [{}] wins the game!".format(winner))
                break
            elif is_tie(field):
                print("It's a tie. No one won the game.")
                break

if __name__ == "__main__":
    main()
