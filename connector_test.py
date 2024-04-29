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
    print("1. Check Balance\n")
    print("2. Make a Deposit\n")
    print("3. Withdraw\n")

def returnToMenu():
    a = input("would you like to return to the main menu? (type y for yes or n for no ): ")
    if a == "y":
        print("\n")
        menu()
        
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

    print("Success! Your balance is now $" + str(check_balance(credentials)[0]))
    returnToMenu()
def new_account(id, password, name, balance):
    testQuery = 'INSERT INTO account_info (id, password, name, balance) VALUES ("' + str(id) + '", "' + str(password) + '", "' + str(name) + '", "' + str(balance) + '");'
    cursor.execute(testQuery)
    print(str(check_balance(password)[0]))
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