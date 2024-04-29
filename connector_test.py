# -------------------ESTABLISHING SQL CONNECTION --------------------------

import mysql.connector

connection = mysql.connector.connect(
    user = 'root', 
    database = 'bank_accounts',
    password = 'MySQLIsCool123'
)

cursor = connection.cursor()

# ------------- FUNCTIONS -------------------------------------------
def check_balance(credentials):
    testQuery = 'SELECT balance FROM account_info WHERE password = "' + credentials + '"'
    cursor.execute(testQuery)

    for item in cursor:
        return item
def make_deposit():
    ye
    
    
def employee():
    password = input("Enter employee password: ")
    if password == "cheetos":
        print("ye")
def customer():
    credentials = input("Please input your password to get started: ")
    testQuery = 'SELECT name FROM account_info WHERE password = "' + credentials + '"'
    def name():
        cursor.execute(testQuery)
        for item in cursor:
            return item
    
    print("Welcome " + str(name()[0]) + "! How can we help you today?\n")
    print("1. Check Balance\n")
    print("2. Make a Deposit\n")
    print("3. Withdraw\n")

    choice = input("enter the number of your choice: ")
    if choice == "1":
        print("ye")
        print("Your Balance is $ " + str(check_balance(credentials)[0]))
    if choice == "2":
        make_deposit()
    if choice == "3":
        withdraw()

    
    

#----------------------------MAIN-----------------------

def main():
    intro = input("Hello! Welcome to the Bank of Tomorrow's Website! Are you a customer or a database employee? Enter c for cutomer or e for employee: ")
    if intro == "e":
        employee()
    elif intro == "c":
        customer()
    else:
        print("invalid")
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