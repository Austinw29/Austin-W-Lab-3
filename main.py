# Function that adds 2 numbers
def add(x,y):
    print(x+y)

# Function that subtracts 2 numbers
def sub(x,y):
    print(x-y)

# Function that multiply 2 numbers
def mult(x,y):
    print(x*y)

# Function that divides 2 numbers
def divi(x,y):
    print(x/y)

##########################################################################################
print("Welcome to Calculator Choom")
while(True):
    print("Go Ahead and give it a try, its pretty nova")
    print(" whant to (a)dd (s)ubtract (m)ultiply (d)ivide (q)uit")

    user_input = input(":")
    #print(user_input)
    

    if user_input == 'a':
        x = int(input("Enter the first number"))
        y = int(input("Enter the second number"))
        add(x,y)

    elif user_input == 's':
        x = int(input("Enter the first number"))
        y = int(input("Enter the second number"))
        sub(x,y)

    elif user_input == 'm':
        x = int(input("Enter the first number"))
        y = int(input("Enter the second number"))
        mult(x,y)

    elif user_input == 'd':
        x = int(input("Enter the first number"))
        y = int(input("Enter the second number"))
        divi(x,y)
    elif user_input == 'q':
        print("goodbye")
        break
print("YOU GONK!!")


