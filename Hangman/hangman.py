import random
# the words tha will be using in our game 
words_list = ["dog","sun","camera","moon","no","mama","one","seven","yes"]
# we choose a word from the list by random
word = random.choice(words_list)
wrong = 6
tmp = word
guesses = ""

print("Hello, this is the Hangman Game ")
print("Your Word's length is [ {} ] letters".format(len(word)) )
print("You have [ {} ] worng guesses before you lose the game ".format(wrong))
# our main program 
while True:
    print("\n---------------------------------------\n")
    letter = input("--> Geuss the letter : ").lower()
    # we check if the letter is in the secret word 
    if letter in word:
        tmp = tmp.replace(letter,"")
        guesses += letter
        if len(tmp) == 0 :
            print("{{ You won the game }}")
            print("The word is [ {} ] ".format(word))
            break
        
        print("Your geuss is corect , [ {} ] left".format(len(tmp)))
        
    else:
        wrong -= 1
        if wrong == 0:
            print("{{ You lost the game }}")
            print("The word is [ {} ] ".format(word))
            break
        
        print("Your geuss is incorect , try again , you have [ {} ] attempts left".format(wrong))
    # printing the prgress 
    for char in word:
        if char in guesses:    
            print (char,end=","),    
        else:
            print ("_",end=",")
