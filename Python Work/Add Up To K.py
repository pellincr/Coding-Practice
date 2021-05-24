#add_up_to_K: int (listofints) -> boolean
#purpose: to determine if there are any 2 values in the given list that add up to K
def add_up_to_K(k,lon):
    i = 0
    j = 0
    res = False
    while (i<len(lon)):
        while(j<len(lon)):
            if(i == j):
                j+=1
            elif(lon[i] + lon[j] == k):
                res = True
                j+=1
            else:
                j+=1
        i+=1
    return res

#test_add_up_to_K: ->
#Purpose: to test the function add_up_to_K
def test_add_up_to_K():
    assert add_up_to_K(17, [10,15,3,7]) == True
    assert add_up_to_K(20, [10,5,4,3]) == False
    assert add_up_to_K(20, [10,5,4,3,10]) == True

if __name__ == "__main__":
    test_add_up_to_K()
    print("All tests have succeeded!")