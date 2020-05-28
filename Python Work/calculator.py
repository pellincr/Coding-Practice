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

#get_Priortiy: operator(string) -> boolean
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
    try:
        if isBalanced(eq):
            for element in eq:
                #element is a number
                if element.isnumeric():
                    numstack.append(int(element))
                #element is an open parenthesis
                elif element == "(":
                    opstack.append(element)
                #element is a closed parenthesis
                elif element == ")":
                    op = opstack.pop()
                    while(opstack != [] and op != "("):
                        val2 = numstack.pop()
                        val1 = numstack.pop()
                        numstack.append(evaluate(val1, val2, op)) 
                        op = opstack.pop() 
                #element is an operator                      
                elif isOp(element):
                    while(opstack != [] and get_Priority(opstack[len(opstack)-1])>= get_Priority(element)):
                        op = opstack.pop()
                        val2 = numstack.pop()
                        val1 = numstack.pop()
                        numstack.append(evaluate(val1, val2, op))
                    opstack.append(element)
                elif element == " ":
                    continue
            #for loop ends; if not everything has been evaluated in the stack yet
            while opstack != []:
                op = opstack.pop()
                val2 = numstack.pop()
                val1 = numstack.pop()
                numstack.append(evaluate(val1, val2, op))
            return numstack.pop()
        else:
            return "Parentheses are not properly balanced"
    except:
        return "Equation not properly written"



#Tests
def test_evaluate():
    assert evaluate(5,1,"/") == 5, "Should be 5"
    assert evaluate(3,5,"+") == 8, "Should be 8"
    assert evaluate(8,6,"-") == 2, "Should be 2"
    assert evaluate(4,2,"*") == 8, "Should be 8"

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
    assert get_Priority("*") == 2, "Should be 2"
    assert get_Priority("/") == 2, "Should be 2"

def test_calc():
    assert calc("3+4*2") == 11, "Should be 11"
    assert calc("(3+4)*2") == 14, "Should be 14"
    assert calc("((3+4)") == "Parentheses are not properly balanced"
    assert calc("()") == "Equation not properly written"
    assert calc("2+(5*4)") == 22, "Should be 22"
    assert calc("(2+2)*(4+4)") == 32, "Should be 32"
    assert calc("2+2*(4+4)") == 18, "Should be 18"
    assert calc("2/2") == 1, "Should be 1"
    assert calc("5*(2/2)") == 5, "Should be 5"
    assert calc("5* (2/ 2)") == 5, "Should be 5"

if __name__ == "__main__":
    test_evaluate()
    test_isOp()
    test_isBalanced()
    test_get_Priority()
    test_calc()
    print("All tests have passed!")