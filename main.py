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
print("Go Ahead and give it a try, its pretty nova")
print(" whant to (a)dd (s)ubtract (m)ultiply (d)ivide (q)uit")

user_input = input(":")
#print(user_input)
x = int(input("Enter the first number"))
y = int(input("Enter the second number"))

while(True):

    if user_input == 'a':
    add(x,y)

    elif user_input == 's':
    sub(x,y)

    elif user_input == 'm':
    mult(x,y)

    elif user_input == 'd':
    divi(x,y)

    elif user_input == 'q':
    break

    print("YOU GONK!!")


