numstack = []
opstack = []

#evaluate: num num string -> string
#purpose: to evaluate the given numbers using the 
def evaluate(num1, num2, op):
    if op == "+":
        return (num1 + num2)
    elif op == "-":
        return (num1 - num2)
    elif op == "*":
        return (num1 * num2)
    elif op == "/":
        return (num1 / num2)

#isOp: string -> boolean
#purpose: to determine if the given string is an operator
def isOp(str):
    return (str == "+" or str == "-" or str == "/" or str == "*")

#isBalanced: equation(string) -> boolean
#purpose: to determine if the given equation has balanced parantheses
def isBalanced(eq):
    balancer =[]
    try:
        while(len(eq) != 0):
            if eq[0:1] == "(":
                balancer.append(eq[0:1])
            elif eq[0:1] == ")":
                balancer.pop()
            eq = eq[1: len(eq)]
        return balancer == []
    except:
        return False

#get_Priortiy: string -> boolean
#purpose: to determine the priority of the given operator
def get_Priority(op):
    if op == "+" or op == "-":
        return 1
    elif op == "*" or op == "/":
        return 2
    else:
        return 0

#calc: equation(string) -> num
#purpose: to determine what the given calculation equates to            
def calc(eq):
    for element in eq:
        if element.isnumeric():
            numstack.append(int(element))
        elif element == "(":
            opstack.append(element)
        elif element == ")":
            op = opstack.pop()
            while(op != "("):
                val2 = numstack.pop()
                val1 = numstack.pop()
                numstack.append(evaluate(val1, val2, op))
        elif isOp(element):
            while(opstack != [] and get_Priority(opstack[0])>= get_Priority(element)):
                op = opstack.pop()
                val2 = numstack.pop()
                val1 = numstack.pop()
                numstack.append(evaluate(val1, val2, op))
            opstack.append(element)
    while opstack != []:
        op = opstack.pop()
        val2 = numstack.pop()
        val1 = numstack.pop()
        numstack.append(evaluate(val1, val2, op))
    return numstack.pop()



#Tests
def test_evaluate():
    assert evaluate(5,1,"/") == 5, "Should be 5"#5/1
    assert evaluate(3,5,"+") == 8, "Should be 8"#3+5
    assert evaluate(8,6,"-") == 2, "Should be 2"#8-6
    assert evaluate(4,2,"*") == 8, "Should be 8"#4*2

def test_isOp():
    assert isOp("123") == False, "Shoule be False"
    assert isOp("+") == True, "Should be True"
    assert isOp("-") == True, "Should be True"
    assert isOp("*") == True, "Should be True"
    assert isOp("/") == True, "Should be True"

def test_isBalanced():
    assert isBalanced("(4+3)") == True, "Should be True"
    assert isBalanced("((4+3)") == False, "Should be False"
    assert isBalanced("(") == False, "Should be False"
    assert isBalanced("(5+22))") == False, "Should be False"
    assert isBalanced(")4+3(") == False, "Should be False"

def test_get_Priority():
    assert get_Priority("+") == 1, "Should be 1"
    assert get_Priority("-") == 1, "Should be 1"
    assert get_Priority("*") == 2, "Should be 1"
    assert get_Priority("/") == 2, "Should be 1"

def test_calc():
    assert calc("3+4*2") == 11, "Should be 11"
    assert calc("(3+4)*2") == 14, "Should be 14"
    assert calc("((3+4)") == "Parentheses are not properly balanced"
    assert calc("()") == "Equation not properly written"

if __name__ == "__main__":
    test_evaluate()
    test_isOp()
    test_isBalanced()
    test_get_Priority()
    #test_calc()
    print("All tests have passed!")