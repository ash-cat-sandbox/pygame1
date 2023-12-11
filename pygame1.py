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
    
def guess_Word():
    global counter
    x = input("What do you think the word is? ")
    if x == answer:
        print("You did it! \nYou guessed the word " + answer)
        print("\nNew Game starting")
        new_game()
    elif x != answer:
        print("Sorry, wrong guess")
        counter_down()
        if counter <= 0:
            print("You lose. The word was " + answer)
            print("New Game starting")
            new_game()
    
def guess():

    '''Originally, I had in range, and x would automatically decrease, which is why I couldn't figure out why it was decreasing each go around
    needed to fix it using while'''
    global answer_list
    global guessed_answer

    print(answer_list)
    print("Guesses remaining: " + str(counter))
    

    while counter != 0:
        x = input("What letter would you like to guess? ")
        if guessed(x, answer, guessed_answer): #if true,  then print the guessed string which is a joined list of the so far guessed answer
            guessed_string = ''.join(guessed_answer)
            print(guessed_string)
    
    
    
        

       
        #answer_list = remove_items(answer_list, x)
            

            #put x in the index of answer list but have everything else removed
            
        print("Correct! There is a " + x + " in the word")
        print(answer_list)
        print(guessed_answer)
        answer_list = answer_list

        if not answer_list:
            print("You did it! You guessed the word " + answer)
            print("New Game starting")
            new_game()
               
        else:
            if counter <= 0:
                print("Oh no! Too many guesses, you lost partner\n New game starting!")
                new_game()
            else:
                print("Nope! No " + x + " in the word")
                counter_down()
                print(str(counter) + " guesses remaining")
                askPlayer()
    
    if counter == 0:
        print("Oh no! Too many guesses, you lost partner\n New game starting!")
        new_game()

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
