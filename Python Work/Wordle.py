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
#purpose: compares how close string2 is to string1
#assumption: no duplicate letters in strings possible (ex. Hello, Goods, Trees, etc.)
def compare_word(string1, string2):
    correct_list = explode(string1)
    guess_list = explode(string2)
    res = []#accumulator where output is stored
    for letter in guess_list:
        if (letter in correct_list):
            if (string1.find(letter) == string2.find(letter)):
                res.append("+") #if the letter is in the right place
            else:
                res.append("*") #if the letter is in the wrong place but exists in the word
        else:
            res.append("-") #if the letter does not exist in the word
    return ' '.join(res)


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


if __name__ == "__main__":
    tlist = ["stein/MS"]
    test_make_List_Upper()
    test_explode()
    test_compare_word()
    test_update_words()
    Wordle(wordList)
    #print(len(update_words(wordList, 5))-1)
    print("All Test Succeeded!")