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

def get_num(eq):
    i = 0
    val = 0
    while i < len(eq) and eq[i].isnumeric():
        val = (val*10) + int(eq[i])
        i = i+1
    return val

#calc: equation(string) -> num
#purpose: to determine what the given calculation equates to            
def calc(eq):
    try:
        if isBalanced(eq):
            while eq != "":
                #element is a number
                if eq[0:1].isnumeric():
                    num = (get_num(eq))
                    numstack.append(num)
                    eq = eq[len(str(num)):len(eq)]
                #element is an open parenthesis
                elif eq[0:1] == "(":
                    opstack.append(eq[0:1])
                    eq = eq[1:len(eq)]
                #element is a closed parenthesis
                elif eq[0:1] == ")":
                    op = opstack.pop()
                    while(opstack != [] and op != "("):
                        val2 = numstack.pop()
                        val1 = numstack.pop()
                        numstack.append(evaluate(val1, val2, op)) 
                        op = opstack.pop()
                        eq = eq[1:len(eq)] 
                #element is an operator                      
                elif isOp(eq[0:1]):
                    while(opstack != [] and get_Priority(opstack[len(opstack)-1])>= get_Priority(eq[0:1])):
                        op = opstack.pop()
                        val2 = numstack.pop()
                        val1 = numstack.pop()
                        numstack.append(evaluate(val1, val2, op))
                    opstack.append(eq[0:1])
                    eq = eq[1:len(eq)]
                elif eq[0:1] == " ":
                    eq = eq[1:len(eq)]
                
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

def test_get_num():
    assert get_num("500") == 500, "Should be 500"
    assert get_num("500+2") == 500, "Should be 500"


def test_calc():
    assert calc("3+4*2") == 11
    assert calc("(3+4)*2") == 14, "Should be 14"
    assert calc("((3+4)") == "Parentheses are not properly balanced"
    assert calc("()") == "Equation not properly written"
    assert calc("2+(5*4)") == 22, "Should be 22"
    assert calc("(2+2)*(4+4)") == 32, "Should be 32"
    assert calc("2+2*(4+4)") == 18, "Should be 18"
    assert calc("2/2") == 1, "Should be 1"
    assert calc("5*(2/2)") == 5, "Should be 5"
    assert calc("5* (2/ 2)") == 5, "Should be 5"
    assert calc("50*10") == 500, "Should be 500"
    assert calc("20+(12/2)") == 26, "Should be 26"

if __name__ == "__main__":
    test_evaluate()
    test_isOp()
    test_isBalanced()
    test_get_Priority()
    test_get_num()
    test_calc()
    print("All tests have passed!")