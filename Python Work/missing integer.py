#create_in_order_list: num num -> list
#purpose: to create a list in the range [min,max]
def create_in_order_list(min, max):
    i = min
    list = []
    while i <= max:
        list.append(i)
        i = i + 1
    return list
    
#find_missing_int: list -> num
#purpose: determines the missing number in the given list of numbers from 1-100
def find_missing_int(list):
    i = 0
    if list[i] != 1:
        return 1
    while i < (len(list) - 1):
        if list[i+1] != (list[i] + 1):
            return list[i] + 1
        i = i + 1
    return "No Missing Integer in the given array"


#Tests
def test_find_missing_int():
    list1 = create_in_order_list(1,100)
    list1.remove(59)
    assert find_missing_int(list1) == 59
    list2 = create_in_order_list(1,100)
    list2.remove(25)
    assert find_missing_int(list2) == 25
    list3 = create_in_order_list(1,100)
    list3.remove(1)
    assert find_missing_int(list3) == 1



#main
if __name__ == "__main__":
    test_find_missing_int()
    print("All tests passed!")
    