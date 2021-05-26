#if_complete: str str -> boolean
#purpose: to determine if the second string is a proper word that can be built from the first string
def if_complete(str1, str2):
    ls1 = len(str1) #length of str1
    ls2 = len(str2) #length of str2
    if(ls1>ls2):
        return False
    else:
        return str1 == str2[0:ls1]


#autocomplete: string (listof strings) -> (listof strings)
#purpose: to determine which strings in the given list of strings would be able to properly continue off of the base
#         input string
def autocomplete(s, lostr):
    res = []
    for str in lostr:
        if(if_complete(s,str)):
            res.append(str)
    return res

#test_if_complete: ->
#purpose: tests the if_complete function
def test_if_complete():
    assert(if_complete("de","deer")) == True
    assert(if_complete("de","dog")) == False
    assert(if_complete("deer","de")) == False #Not in the correct input order

#test_autocomplete: ->
#purpose: to test the autocomplete function
def test_autocomplete():
    assert(autocomplete("de",["deer","deal","dog"])) == ["deer","deal"]
    assert(autocomplete("m", ["main","hello","menu"])) == ["main","menu"]
    assert(autocomplete("hello",["world"])) == []

if __name__ == "__main__":
    test_if_complete()
    test_autocomplete()
    print("All tests have succeeded!")