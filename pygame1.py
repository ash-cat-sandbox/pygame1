# hangman game
import random
import words
counter = 7
answer = ""
guessed_answer = []
answer_list = []
length = 0

def counter_down():
    global counter
    counter -= 1

def reset_counter():
    global counter
    counter = 7

def word():
    global answer
    answer = random.choice(words.word_list)
    if any(not c.isalpha() for c in answer):
        word()
    global length
    length = len(answer)
    print("Length of word is " + str(length))
    global guessed_answer 
    guessed_answer = ['_'] * length
    print(answer)
    global answer_list
    answer_list = ([*answer])
    print(answer_list)


# the player's guess function
def guessed(choice, answer, guessed_answer):
    updated = False
    for index, letter in enumerate(answer): #enumerate through the answer, if the c matches the l, update the guessed_answer list variable with the c at that particular index
        if choice == letter:
            guessed_answer[index] = choice
            updated = True

    return updated 


def askPlayer():
    if counter == 0:
        print("Oh no! Too many guesses, you lost partner\n New game starting!")
        new_game()
    print("\nGuesses remaining: " + str(counter))

    print(("\nWould you like to guess a letter or guess the word?\n" +
                   "Type g if you would like to guess a letter.\n" +
                   "Type w if you would like to guess the word.\n" +
                   "Type q if you would like to stop playing\n"))
     
    move = input()
    if move == "g":
        guess()
    elif move == "w":
        guess_Word()
    elif move == "q":
        exit()
    else:
        print("not a valid choice, please select a valid option")
        askPlayer()      
    
def guess_Word():
    global counter
    x = input("What do you think the word is? ")
    if x == answer:
        print("You did it! \nYou guessed the word " + answer)
        print("\nNew Game starting")
        new_game()
    else: 
        counter_down()
        print("Sorry, wrong guess. You have " + str(counter) + " guesses remaining")

        if counter <= 0:
            print("You lose. The word was " + answer)
            print("New Game starting")
            new_game()
        else:
            askPlayer()

    
def guess():

    global answer_list
    global guessed_answer

    print(answer_list)
    print("\nGuesses remaining: " + str(counter))
    

    while counter != 0:
        x = input("What letter would you like to guess? ")
        if x in answer_list: #if true,  then print the guessed string which is a joined list of the so far guessed answer
            guessed(x, answer, guessed_answer) 
            guessed_string = ''.join(guessed_answer)
            print(guessed_string)
            print("Correct! There is a " + x + " in the word")
            print(answer_list)
            print(guessed_answer)
            answer_list = answer_list
            if guessed_answer == answer_list:
                print("You did it! You guessed the word " + answer)
                print("New Game starting")
                new_game()
            askPlayer()
    
        #answer_list = remove_items(answer_list, x)
         
        
               
        else:
            if counter <= 0:
                print("Oh no! Too many guesses, you lost partner\n New game starting!")
                new_game()
            else:
                print("Nope! No " + x + " in the word")
                counter_down()
                print(str(counter) + " guesses remaining")
                askPlayer()
    
    

def remove_items(test_list, item): 
    # using list comprehension to perform the task 
    res = [i for i in test_list if i != item]   
    return res 

def new_game():
    print("New Game Started!")
    reset_counter()
    word()
    for i in range(length):
        print("_", end=" ")
    askPlayer()
    

new_game()  
