#Debug Challenge 1
number=int(input("What number would you like to check?: "))
if number % 2 ==0: #'==' sign is used to check condition and '=' is used to assign a varibale
    print("This is an even number!")
else:
    print("This is an odd number!")
    
#Debug Challenge 2
year= int(input("Which year would you like to check?: "))#'int' is used to convert the input to interger
if year % 4==0:
    if year % 100==0:
        if year % 400==0:
            print("This is a leap year!")
        else:
            print("Not a leap year!")
    else:
        print("This is a leap year!")
else:
    print("Not a leap year!")
    
#Debug Challenge 3
for number in range(1, 101):
    if number % 3==0 and number % 5 ==0: #Used 'and' instead of 'or' to rectify the code
        print ("Fizzbuzz")
    elif number % 3== 0: #Used elif statements to rectify the code
        print("Fizz")
    elif number % 5==0:
        print ("Buzz")
    else:
        print(number)