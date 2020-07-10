#num_of: string -> string
#purpose: determines the number of vowels and consonants in a given string
def num_of(st):
    cons = 0
    vow = 0
    for letter in st:
        if is_vowel(letter):
            vow = vow + 1
        if is_consonant(letter):
            cons = cons + 1
    svow = str(vow)
    scons = str(cons)
    return "#Of Vowels: " + svow + "/n#Of Consonants: " + scons

#is_vowel: string -> boolean
#purpose: to determine if the given string is a vowel
def is_vowel(letter):
    l = letter.lower()
    return l == "a" or l == "e" or l == "i" or l == "o" or l == "u"

#is_consonant: string -> boolean
#purpose: to determine if the given string is a consonant
def is_consonant(letter):
    l = letter.lower()
    return not(is_vowel(l)) and not(l == " ") and not(l == ".")

#Tests
def is_vowel_tests():
    assert is_vowel("a") == True
    assert is_vowel("e") == True
    assert is_vowel("i") == True
    assert is_vowel("o") == True
    assert is_vowel("u") == True
    assert is_vowel(" ") == False
    assert is_vowel("b") == False
    assert is_vowel(".") == False

def is_consonant_tests():
    assert is_consonant("b") == True
    assert is_consonant(" ") == False
    assert is_consonant("c") == True
    assert is_consonant("h") == True
    assert is_consonant(".") == False

def num_of_tests():
    assert num_of("Hello world.") == "#Of Vowels: 3/n#Of Consonants: 7"
    assert num_of("aeiouaeioub") == "#Of Vowels: 10/n#Of Consonants: 1"

if __name__ == "__main__":
    is_vowel_tests()
    is_consonant_tests()
    num_of_tests()
    print("All tests have passed!")