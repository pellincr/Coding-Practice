#cons: A B -> pair
#purpose: to pair the given two elements
def cons(a, b):
    def pair(p):
        return p(a, b)
    return pair

#car: pair -> A
#purpose: to output the first part of the pair
def car(pair):
    def first(a,b):
        return a
    return pair(first)

#cdr: pair -> B
#purpose: to output the second part of the pair
def cdr(pair):
    def second(a,b):
        return b
    return pair(second)

#test_car: ->
#purpose: to test the car function
def test_car():
    assert car(cons(1,2)) == 1
    assert car(cons("A","B")) == "A"

def test_cdr():
    assert cdr(cons(1,2)) == 2
    assert cdr(cons("A","B")) == "B"

if __name__ == "__main__":
    test_car()
    test_cdr()
    print("All tests have passed!")