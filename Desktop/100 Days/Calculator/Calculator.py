#Project Calculator
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations={ "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide,
}
def calculator():
    num1=float(input("What's the first number?: "))
    for sign in operations:
        print(sign)
    operation_sign=input("Pick an operation from the given operations above: ")
    num2=float(input("Enter your second number?: "))
    function= operations[operation_sign]
    answer= function (num1, num2)
    print(f"{num1} {operation_sign} {num2} = {answer}")
    calculation_continue=True
    while calculation_continue:
        another_calculation=input("Type 'y' to continue calculating with previous answer or type 'n' to exit: ").lower()
        if another_calculation=="y":
            operation_sign=input("Pick an operation: ")
            next_number=float(input("What's the next number?: "))
            next_function=operations[operation_sign]
            answer= next_function(answer, next_number)
            print(f"ans {operation_sign} {next_number} = {answer}")
        else:
            calculation_continue= False
            calculator()           
calculator()  