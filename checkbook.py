'''Makes a checkbook that tracks balance inputs and withdraws over time   '''

import os
import regex as re

############################################## helper functions for printing messages to the user as each stage of the app##########################################################

def print_open_text():
    

    print()
    print("You have opened the Apature Science account tracker!")
    print("We do what we must because we can!")
    print()


def print_menu_text():

    print("This is the main menu")
    print()
    print("what would you like to do?")
    print()
    print("1) see balance")
    print("2) Make deposit")
    print("3) Make withdrawl")
    print("4) quit")
    print()

def print_prev_balance(balance):

    print(f"Your previous balance is {balance}")

def print_bal_text(balance):

    print(f"Your current balance is {balance}")
    print()        
    print("You will now return to the main menu.")
    print()


def print_dep_text():

        print("You are making a deposit!")
        print()
        print("How much do you want to deposit?")
        print()


def print_withdr_text(balance):

    print("You are making a withdrawal")
    print(f"You have {balance} in your account")
    print()
    print("How much do you want to withdrawal?")
    print()


def print_quit_text():

    print("You are exiting the application.")
    print("Have a Nice day!")
    print()


##################################################################################### Helper functions for validating input##################################################################


def valid_menu_input(user_input):
    ''' check if user input is a valid selection of 1 2 3 or 4
        print input
        '''

    if user_input in ('1','2','3','4'):

        print()
        print(f"Your input is {user_input}")
        print()
        return True

    else:

        print()
        print("This input is invalid")
        print()
        return False


def is_valid_number(customer_input):
    ''' Check if number is a valid decimal'''

    if re.match(r"\d*\.?\d*", customer_input):

        return True

    else:

        print()
        print("The number input is not a valid number. Please input a valid number using the number and decimal keys.")
        print()

        return False


def is_valid_withdrawl(withdrawl, balance):
    ''' Returns True if withdrawl amount is less than current balance and False otherwise
        If false returns error message'''

    if float(withdrawl) <= float(balance):

        return True

    else:
        
        print("Withdrawl amount exceeds balance. A withdrawl of this amount is not allowed.")
        print()
        return False 

####################################################### Helper functions for containing while loops needed for screening userinput and reprompting ########################################################################################

def main_menu():
    '''
    Display main menu
    get user input
    validate user input
    pass only when  user input is valid
    '''

    # nested while loop for main menu to check for valid input
    while True:

        # main menu
        print_menu_text()

        # get user input
        user_input = input() 

        # if input is valid display error,
        if valid_menu_input(user_input):

            break

    return user_input


def make_deposit():
    '''
    Display deposit text
    get deposit input 
    validate input 
    reprompt if input is invalid
    '''

    while True:

        print_dep_text()

        depositing = input()

        if is_valid_number(depositing):

            break

    return depositing


def make_withdrawl(balance):
    '''
    Display withdrawl text
    get withdrawl input 
    validate input 
    reprompt if input is invalid
    '''

    while True:

        print_withdr_text(balance)

        withdrawl = input()

        if is_valid_number(withdrawl) and is_valid_withdrawl(withdrawl,balance):

            break

    return withdrawl

###################################################################### Functions for reading and writing to the text file for storage #################################################################################

def get_balance_from_file():

    # if file exists get balance number from file
    if os.path.exists('balance_scroll.txt'):

        with open('balance_scroll.txt', 'r') as reader:

            balance = reader.read()
            

    # otherwise set balance to zero and save balance to file
    else:

        balance = 0

        save_balance(balance)

    return balance
  

def save_balance(balance):

    # open create text file and store balance as a string
    with open("balance_scroll.txt", "w") as writer:

        writer.write(f"{balance}")

    return balance

############################################################################################ Main loop for Application#########################################################################

# print oppening text
print_open_text()

# getting balance from text file or setting to 0
balance = get_balance_from_file()

# main while loop for running checkbook
while True:

    user_input = main_menu()

    # if user_input = 4 print closing message and close the application
    if user_input == '4':

        print_quit_text()

        break

    # if users input is 1 display balance and return to menue
    elif user_input == '1':

        print_bal_text(balance)

    # if user input is 2 make deposit the return to the main menue
    elif user_input == '2':

        depositing = make_deposit()

        print_prev_balance(balance)

        balance = str(round(float(balance) + float(depositing),2))

        save_balance(balance)

        print_bal_text(balance)

    # if user_input is 3 print withdrwl text, check for valid input
    elif user_input == '3':

        withdrawl = make_withdrawl(balance)

        print_prev_balance(balance)

        balance = str(round(float(balance) - float(withdrawl),2))

        save_balance(balance)

        print_bal_text(balance)

