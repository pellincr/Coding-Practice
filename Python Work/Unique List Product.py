#list_product: (listof int) -> int
#purpose: to multiply all elements in the list together
def list_product(lon):
    res = 1
    for number in lon:
        res = res*number
    return res

#unique_list_products: (listof int) -> (listof int)
#purpose: to change every element of the list to be the product of each element in the list without including itself
def unique_list_products(lon):
    temp = list_product(lon)
    i = 0
    while (i<len(lon)):
        lon[i] = temp/lon[i]
        i+=1
    return lon
    
#test_list_product: ->
#purpose: to test the list_product function
def test_list_product():
    assert list_product([1,2,3,4,5]) == 120
    assert list_product([1,5,7,3]) == 105

#test_unique_list_products: ->
#purpose: to test the unique_list_products function
def test_unique_list_products():
    assert unique_list_products([1,2,3,4,5]) == [120,60,40,30,24]
    assert unique_list_products([1,5,7,3]) == [105,21,15,35]

if __name__ == "__main__":
    test_list_product()
    test_unique_list_products()
    print("All tests have succeeded!")