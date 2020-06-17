
#growth_rate: num num num -> num
#purpose: to determine the growth rate of the first number to the second number by the given number of years
def growth_rate(num1, num2, years):
    return pow((num2/num1), 1/years)



if __name__ == "__main__":
    #num1
    n1 = input("Enter your first number: ")
    #num2
    n2 = input("Enter your second number: ")
    #years
    years= input("How many years are you calculating for?: ")
    print(growth_rate(int(n1),int(n2),int(years)))    