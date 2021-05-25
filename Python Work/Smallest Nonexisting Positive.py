#smallest_nonexisting_positive: (listof int) -> int
#purpose: to output the smallest positive number that does not exist in the given list
def smallest_nonexisting_positive(lon):
    res = 1
    lon = sorted(lon)
    i = 0
    while(i<len(lon)):
        if(lon[i]<=0):
        #if number at lon[i] is not positive
            i+=1
        elif (lon[i] > 0 and lon[i] == res):
        #if number at lon[i] is positive and equals res
            res +=1
            i+=1
        elif(lon[i] > 0 and lon[i] > res):
        #if number at lon[i] is positive and is greater than res
            return res
    return res

#test_smallest_nonexisting_positive: ->
#purpose: to test the smallest_nonexisting_positive function
def test_smallest_nonexisting_positive():
    assert smallest_nonexisting_positive([3,4,-1,1]) == 2
    assert smallest_nonexisting_positive([-3,-2,-1,0]) == 1
    assert smallest_nonexisting_positive([1,2,3,4,5]) == 6
    assert smallest_nonexisting_positive([2,3,4,5,6]) == 1

if __name__ == "__main__":
    test_smallest_nonexisting_positive()
    print("All tests have succeeded!")