
#find_dup: list-of-x -> x
#purpose: to determine what the duplicate value is in the given list
def find_dup(list):
    i = 0
    while i <= len(list):
        j = i+1
        while j < len(list):
            if list[j] == list[i]:
                return list[i]
            j = j + 1
        i = i+1


#tests
def find_dup_test():
    list1 = [1,2,3,4,1]
    assert find_dup(list1) == 1
    list2 = [1,2,3,4,2,6,5]
    assert find_dup(list2) == 2
    list3 = [1,2,3,3,4,5,6]
    assert find_dup(list3) == 3
    list4 = [1,2,3,4,1,5]
    assert find_dup(list4) == 1

if __name__ == "__main__":
    find_dup_test()
    print("All tests have passed!")