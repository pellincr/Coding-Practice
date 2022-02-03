import re
import random

filename = "C:\Dictionary\dictionary.txt"

wordList = ["Stein/M", "Carts/AU", "Craig/MS"]



#make_List_Upper: list-of-strings -> list-of-strings
#Purpose: to set the given list of strings to be entirely upper case
def make_List_Upper(los):
    res = []
    for word in los:
        res.append(word.upper())
    return res

#update_words: los num -> los
#purpose to make the given list of strings suitable to be used
def update_words(los, size):
    res = []
    for word in los:
            new_word = word[0:(word.find("/"))]
            if len(new_word) == size:
                res.append(new_word)
    return make_List_Upper(res)


#explode: string -> list-of-string
#purpose: turn the given string into a list of strings seperated by the letter
def explode(str):
    i = 0
    res = []
    while(i<len(str)):
        res.append(str[i:i+1])
        i+=1
    return res


#compare_word: string string-> string
#purpose: compares how close the guess word is to the answer word
def compare_word(answer, guess):
    correct_list = explode(answer)
    guess_list = explode(guess)
    res = []
    for letter in guess_list:
        if (letter in correct_list):
            if (answer.find(letter) == guess.find(letter)):
                res.append("+") #if the letter is in the right place
            else:
                res.append("*") #if the letter is in the wrong place but exists in the word
        else:
            res.append("-") #if the letter does not exist in the word
    return ' '.join(res)

#Currently Does not work if any word has a duplicate letter in it (ex. books, skies)
#How to make it work:
#1. Check to see if the letter exists in the answer word
#2. if it does, check to see if where the letter is in the guess word is correct or not
    #If it is correct put down a '+'
#3. If it is not correct,
        #check to see if the answer has it as a duplicate letter
        #If it does,
            #check to see if the guess has the letter in the correct spot later in the word
        #If it doesn't
            #place a '-'


#Wordle: list-of-string -> 
#purpose: the main function of the game
def Wordle(los):
    print("Welcome to Super Ultra Special Wordle (not affiliated with Wordle in the slightest)!")
    print("Here are the rules:")
    print("A '-' indicates the letter in the corresponding spot does not exist in the answer")
    print("A '*' indicates the letter in the corresponding spot does exist in the answer, but is currently in the wrong spot")
    print("A '+' indicates the letter in the corresponding spot is correct")
    size = int(input("What length would you like to try guessing?: "))
    goodList = update_words(los,size)
    r = random.randint(0,(len(goodList)-1))
    word_of_the_game = goodList[r]#randomly selects a full capital word from 
    attempts = 6 #number of tries a player gets in a game
    while(attempts>0):
        guess = input("Enter your guess: ").upper()
        print(compare_word(word_of_the_game, guess))
        if(compare_word(word_of_the_game, guess) == "+ + + + +"):
            print("You got the word!")
            break
        attempts-=1


#Tests

#test_make_List_Upper: ->
#purpose: to test the make_List_Upper function
def test_make_List_Upper():
    tlist = ["stein", "carts"]
    assert make_List_Upper(tlist) == ["STEIN", "CARTS"]

#test_update_words: ->
#purpose: to test the update_words function
def test_update_words():
    tlist = ["stein/M", 'carts/MS', "CRAIG/AU"]
    assert update_words(tlist, 5) == ["STEIN", "CARTS", "CRAIG"]


#test_explode: ->
#purpose: to test the eplode function
def test_explode():
    assert explode("Hello") == ["H","e","l","l","o"]


#test_compare_word: ->
#purpose: to test the compare word function
def test_compare_word():
    assert compare_word("STEIN", "STEIN") == "+ + + + +"
    assert compare_word("CARTS", "STEIN") == "* * - - -"
    #Duplicate Tests
    assert compare_word("ABCDA", "BCDAA") == "* * * * +"
    assert compare_word("ABCDE", "BCDAA") == "* * * * -"
    assert compare_word("")


if __name__ == "__main__":
    test_make_List_Upper()
    test_explode()
    test_compare_word()
    test_update_words()
    Wordle(wordList)
    print("All Test Succeeded!")