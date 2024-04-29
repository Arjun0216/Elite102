# -------------------ESTABLISHING SQL CONNECTION --------------------------

import mysql.connector

connection = mysql.connector.connect(
    user = 'root', 
    database = 'bank_accounts',
    password = 'MySQLIsCool123'
)

cursor = connection.cursor()
current_id = 1
# ------------- FUNCTIONS -------------------------------------------
def menu():
    print("\n")
    print("1. Check Balance\n")
    print("2. Make a Deposit\n")
    print("3. Withdraw\n")
    print("4. Close an account\n")
    print("5. Modify Account\n")

def returnToMenu():
    choice = input("Would you like to go back to our homepage? (type y for yes or n for no): ")
    if choice == "y":
        main()
        
def check_balance(credentials):
    testQuery = 'SELECT balance FROM account_info WHERE password = "' + credentials + '"'
    cursor.execute(testQuery)

    for item in cursor:
        return item
def make_deposit(amount, credentials):
    current_balance = check_balance(credentials)[0]
    new_balance = current_balance + float(amount)
    testQuery = 'UPDATE account_info SET balance = "' + str(new_balance) + '" WHERE password = "' + credentials + '"'
    cursor.execute(testQuery)

    print("Success! Your balance is now $" + str(check_balance(credentials)[0]))
    returnToMenu()

def withdraw(amount, credentials):
    current_balance = check_balance(credentials)[0]
    new_balance = current_balance - float(amount)
    testQuery = 'UPDATE account_info SET balance = "' + str(new_balance) + '" WHERE password = "' + credentials + '"'
    cursor.execute(testQuery)
    print("You have succesfully withrawed $" + amount + "!\n")
    returnToMenu()
def delete_account(credentials):
    testQuery = 'DELETE FROM account_info WHERE password = "' + credentials + '"'
    cursor.execute(testQuery)
    print("Your account has been deleted. Sorry to see you go.\n")
    returnToMenu()
def modify_password(new_val, credentials):
    testQuery = 'UPDATE account_info SET password = "' + str(new_val) + '" WHERE password = "' + credentials + '"'
    cursor.execute(testQuery)
    print("Your password has been changed!\n")
    returnToMenu()
def modify_name(new_val, credentials):
    testQuery = 'UPDATE account_info SET name = "' + str(new_val) + '" WHERE password = "' + credentials + '"'
    cursor.execute(testQuery)
    print("Your name has been changed!\n")
    returnToMenu()
    
def new_account(id, password, name, balance):
    testQuery = 'INSERT INTO account_info (id, password, name, balance) VALUES ("' + str(id) + '", "' + str(password) + '", "' + str(name) + '", "' + str(balance) + '");'
    cursor.execute(testQuery)
    print("Success! Welcome to Bank of Tomorrow\n")
    returnToMenu()


def customer():
    
    credentials = input("Please input your password to get started: ")
    testQuery = 'SELECT name FROM account_info WHERE password = "' + credentials + '"'
    def name():
        cursor.execute(testQuery)
        for item in cursor:
            return item
    
    print("Welcome " + str(name()[0]) + "! How can we help you today?\n")
    menu()

    choice = input("enter the number of your choice: ")
    if choice == "1":
        print("Your Balance is $" + str(check_balance(credentials)[0]))
        returnToMenu()
    if choice == "2":
        amount = input("How much would you like to deposit? ")
        make_deposit(amount, credentials)
    if choice == "3":
        amount = input("How much would you like to withdraw? ")
        if float(amount)> check_balance(credentials)[0]:
            print("insufficient funds")
        else: withdraw(amount, credentials)
    if choice == "4":
        delete_account(credentials)
    if choice == "5":
        col = "something"
        print("What would you like to modify? \n")
        print("1. password\n")
        print("2. name\n")

        choice = input("Enter the number of your choice here : ")
        if choice == "1":
            new_val = input("What would you like to change your password to? ")
            modify_password(new_val, credentials)
        else:
            new_val = input("What would you like to change your name to? ")
            modify_name(new_val, credentials)
        

def new_customer():
    global current_id
    current_id += 1
    balance = 0
    name = input("Welcome to Bank of Tomorrow! Let's make a new account. What is your name? ")
    password = input("Awesome " + name + "! What would you like your password to be? ")
    new_account(current_id, password, name, balance)


    
    

#----------------------------MAIN-----------------------

def main():
    print("Hello! Welcome to the Bank of Tomorrow's Website!\n")
    status = input("Are you a new or returning customer? (type n for new or r for returning): ")
    if status == "n":
        new_customer()
    else:
        customer()
 
main()








connection.commit()
cursor.close()
connection.close()
        





"""
testQuery = ('SELECT * FROM account_info' )
cursor.execute(testQuery)

for item in cursor:
    print(item)


# insertQuery = ("INSERT INTO sample.board_games (ID, name, description, player_count) VALUES (4, 'uno', 'glglglg', 5);")
# cursor.execute(insertQuery)
# cursor.execute(testQuery)

# for item in cursor:
    # print(item)

"""