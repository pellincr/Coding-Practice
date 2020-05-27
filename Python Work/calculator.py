mainstack = []

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

def calc(eq):
    while eq != "":
        if eq[0:1] != ")":
            mainstack.append(eq[0:1])
            eq = eq[1:len(eq)]
        else:
            evaluate


print(evaluate(1,2,"+"))
assert evaluate(5,1,"/") == 5, "Should be 5"