import subprocess

def show_list():
    print("\n--------------------------------------")
    print('''Choose an action from the list :
             1) Shut Down
             2) Restart
             3) Sleep
             4) Cancel all 
             0) Exit program''')
    print("--------------------------------------")
    choise = input("Choise = ")
    return choise

def t2seconds ():
    hours = int(input("How many Hours , H = "))
    minuts = int(input("How many Minuts , M = "))
    seconds = int(input("How many Seconds , S = "))
    result = hours*60*60 + minuts*60 + seconds
    return result

def exct(fun):
    if fun != "/a" :
        tme = t2seconds()
        cmmnd = "shutdown {} /t {}".format(fun,tme)
        #print("cmd =========" , cmmnd)
        execute_cmd(cmmnd)
    else:
        cmmnd = "shutdown /a"
        #print("cmd =========" , cmmnd)
        execute_cmd(cmmnd)

def execute_cmd(cmd):
  """Executes a CMD command and returns the output of it."""
  process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
  output, err = process.communicate()
  print("result \n" ,output.decode("utf-8"))
  #print("\nerror \n " ,err.decode("utf-8"))

def app():
    usr_choise = show_list()
    match int(usr_choise):
        case 0 :
            print("exit")
            exit()
        case 1 :
            print("--[ Shut Down ]--")
            exct("/s")
            print("--[ Shut Down ]--")
        case 2 :
            print("--[ Restart ]--")
            exct("/r")
            print("--[ Restart ]--")
        case 3 :
            print("--[ Sleep ]--")
            exct("/h")
            print("--[ Sleep ]--")
        case 4 :
            print("--[ Cancel all ]--")
            exct("/a")
            
while True:
    app()
