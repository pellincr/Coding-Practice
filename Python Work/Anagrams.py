
#is_anagram: string string -> boolean
#Purpose: to determine if the given strings are anagrams of each other
def is_anagram(s1, s2):
    sl1 = string_to_list(s1)
    sl2 = string_to_list(s2)
    
    if len(sl1) == len(sl2):
        while(0<len(sl1)):
            if list_contains(sl1, sl2[0]):
                sl1.remove(sl2[0])
                sl2.remove(sl2[0])
            else:
                return False
        return True
    else:
        return False

#string_to_list: string -> list
#Purpose: to turn each element of the string into an element in a list
def string_to_list(str):
    res = []
    i = 0
    while(i < len(str)):
        res.append(str[i])
        i = i + 1
    return res

#list_contains: list string -> boolean
#Purpose: to determine if the given list contains the given string
def list_contains(lst, str):
    i = 0
    while(i<len(lst)):
        if lst[i] == str:
            return True
        i = i + 1
    return False

#Tests
def is_anagram_tests():
    assert is_anagram("bat", "tab") == True
    assert is_anagram("ab", "bat") == False
    assert is_anagram("abc", "abd") == False
    assert is_anagram("", "") == True
    assert is_anagram("race", "race") == True
    assert is_anagram("gotcha", "achogt") == True

def string_to_list_test():
    l1 = ["b","a","t"]
    assert string_to_list("bat") == l1
    l2 = ["b","a","b","y"]
    assert string_to_list("baby") == l2

def list_contains_test():
    l = ["b","a", "i", "l", "e", "d"]
    assert list_contains(l, "i") == True
    assert list_contains(l, "c") == False
    assert list_contains(l, "b") == True
    assert list_contains(l, "d") == True

if __name__ == "__main__":
    is_anagram_tests()
    string_to_list_test()
    list_contains_test()
    print("All tests have passed!")
    