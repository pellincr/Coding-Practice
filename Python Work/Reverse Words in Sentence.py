#reverse_sentence_words: string -> string
#purpose: to reverse the words in the given sentence without reverseing the sentence
def reverse_sentence_words(string):
    temp = string.split()
    i = 0
    res = []
    while (i<len(temp)):
        res.append(reverse(temp[i]))
        i+=1
    return list_to_string(res)

#reverse: string -> string
#purpose: to reverse the given string
def reverse(string):
    i = len(string)-1
    res = ""
    while(i>=0):
        res+=string[i:i+1]
        i-=1
    return res

#list_to_string: list-of-strings -> string
#purpose: converts the given list to a string
def list_to_string(li):
    return " ".join([str(elem) for elem in li])


#Tests
def reverse_Test():
    assert reverse("abc") == "cba"
    assert reverse("") == ""
    assert reverse("Hello") == "olleH"

def reverse_sentence_words_Test():
    assert reverse_sentence_words("Hello World") == "olleH dlroW"
    assert reverse_sentence_words("") == ""
    assert reverse_sentence_words("Hello") == "olleH"

def list_to_string_Test():
    assert list_to_string(["Hello", "World"]) == "Hello World"
    assert list_to_string(["a"]) == "a"
    assert list_to_string([]) == ""


if __name__ == "__main__":
    reverse_Test()
    reverse_sentence_words_Test()
    list_to_string_Test()
    print("All Tests Have Passed!")