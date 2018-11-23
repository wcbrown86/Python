# This program is a simple calculator that takes in put from the user.
# It takes the input and determines the mathematical function to preform.
# Then determines the correct output then prints this to the user, and will
# continue to run until the users enters stop.


# Function that returns the sum of two numbers
def add(num1, num2):
    return num1 + num2


# Function that returns the results of number1 from number2
def subtract(num1, num2):
    return num1 - num2


# Function that returns the product of number1 times number2
def multiply(num1, num2):
    return num1 * num2


# Function that returns number1 divided by number2
def divide(num1, num2):
    return num1/num2


# Setting up variable that controls the outer while loop
stop = False

# Print section that prints the instructions at the start of the program.
print("Welcome, please enter a simple calculation,")
print("ex: 1 + 1 or 2 / 2")
print("Make sure to provide a space between each number or mathmatical symbol. ")
print("If you wish to exit the calculator please type 'stop'")

# Main while loop that keeps the program running until the user types stop or answers no to the
# the continue propt that is given after a calculation is preformed.
while stop is False:

    # Variable that stores the user entered expression from the command line
    user_input = input("Please enter your expression. \n")

    # The information entered by the ser is split at any blank space. and stored in the variable user_array
    user_array = str(user_input).split(" ")

    #
    if len(user_array) == 3:
        try:
            number1 = float(user_array[0])
            number2 = float(user_array[2])
        except:
            print("Please check your expression and try again.")
        finally:
            if user_array[1] == "+":
                calculation = add(number1, number2)
            elif user_array[1] == "-":
                calculation = subtract(number1, number2)
            elif user_array[1] == "*":
                calculation = multiply(number1, number1)
            elif user_array[1] == "/":
                calculation = divide(number1, number2)
            else:
                print("The expression entered is incorrect. Please check and try again.")

    else:
        print("The expression entered is incorrect. Please check and try again.")

    print(str(calculation))
    correct_input = False
    while correct_input is False:
        cont_y_n = input('Would you like to preform another calculation? yes/no \n')
        if str(cont_y_n) == "yes":
            stop = False
            correct_input = True
        elif str(cont_y_n) == "no":
            stop = True
            correct_input = True
        else:
            print("Please check your answer, it needs to be either yes or no. \n")

