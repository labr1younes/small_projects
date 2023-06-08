import random

field = [ [1,2,3],
          [4,5,6],
          [7,8,9] ]

c_player = random.choice(["X","O"])

def print_field(fe):
    print("{} | {} | {}".format(fe[0][0],fe[0][1],fe[0][2]))
    print("----------")
    print("{} | {} | {}".format(fe[1][0],fe[1][1],fe[1][2]))
    print("----------")
    print("{} | {} | {}\n".format(fe[2][0],fe[2][1],fe[2][2]))

def current_role(pla):
    print("Is's [{}] Trun".format(pla))

def find(x):
    for i in range(3):
        for j in range(3):
            if x == field[i][j]:
                return i,j

def play(position):
    global c_player
    x ,y = find(position)
    if c_player == "X":
        field[x][y] = "X"
        c_player = "O"
    elif c_player == "O":
        field[x][y] = "O"
        c_player = "X"

def check_winner(f):
    for i in range(3):
        if f[i][0] == f[i][1] == f[i][2]:
            return f[i][0]

    for j in range(3):
        if f[0][j] == f[1][j] == f[2][j]:
            return f[0][j]
        
    if f[0][0] == f[1][1] == f[2][2]:
        return f[0][0]

    if f[0][2] == f[1][1] == f[2][0]:
        return f[0][2]

    return None

def is_tie(f):
    for i in f:
        for j in i:
            if isinstance(j, int):
                return False
    return True

def main():
    print_field(field)
    while True:
        print("It's the [{}] turn.".format(c_player))
        tmp = int(input("Pick a position : "))
        
        play(tmp)
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
