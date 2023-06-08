feild = [ [1,2,3],
          [4,5,6],
          [7,8,9] ]

c_player = "X"

def print_feild(fe):
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
            if x == feild[i][j]:
                return i,j

def play(position):
    global c_player
    x ,y = find(position)
    if c_player == "X":
        feild[x][y] = "X"
        c_player = "O"
    elif c_player == "O":
        feild[x][y] = "O"
        c_player = "X"

def check(f):
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

    return "Tie"

def main():
    print_feild(feild)
    plays = 0
    while True:
        tmp = int(input("Pick a position : "))
        play(tmp)
        plays += 1
        winner = check(feild)
        print_feild(feild)
        if winner == -1 and plays==9 :
            print("Its a Tie , nom one wone the game")
            break
        

if __name__ == "__main__":
    main()
