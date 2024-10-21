import json
import re

filename = "database.json"

try:
    with open(filename, 'r') as file:
        users = json.load(file)
except FileNotFoundError:
    users = []

def save_users():
    with open(filename, 'w') as file:
        json.dump(users, file, indent=4)

def register_user():
    account_info = {}

    username = input("Please Enter a Username: ")

    while True:
        password = input("Enter a valid password, Pwd must contain 8+ chars, A-Z, a-z, and numbers: ")

        if (len(password) >= 8 and
                re.search(r'[a-zA-Z]', password) and
                re.search(r'[0-9]', password)):
            print("Password is valid.")
            break
        else:
            print("Password is invalid. Password must contain 8+ characters with upper, lower case, and number.")

    print(f"Your valid password is: {password}")

    phone = input("Please Enter Your Phone Number: ")
    email = input("Please Enter Your Email: ")
    gender = input("Please Enter Your Gender (M/F/Other): ")
    age = int(input("Please Enter Your Age: "))
    city = input("Please Enter Your City: ")

    account_info["username"] = username
    account_info["password"] = password
    account_info["phone"] = phone
    account_info["email"] = email
    account_info["gender"] = gender
    account_info["age"] = age
    account_info["city"] = city
    account_info["balance"] = 0.0  # Initialize balance
    account_info["ID"] = len(users) + 1  # Assign ID based on the number of users
    print(f"Your id: {account_info['ID']}")

    users.append(account_info)
    save_users()

    print("Account has been Successfully Added")

    return account_info

def login_user():
    user_id = int(input("Please enter your ID: "))
    pwd = input("Please Enter your Password: ")

    for user in users:
        if user.get("ID") == user_id:
            if user["password"] == pwd:
                print("You have successfully Logged in")
                return user
            break
    else:
        print("Your ID or Password Is Incorrect. Please try again")
        return None

def currency_conversion(amount, currency_code):
    rates = {"EGP": 1, "USD": 30, "SAR": 9}
    return amount * rates[currency_code]

def deposit(user):
    currencies = ["EGP", "USD", "SAR"]
    choice = int(input("Please choose the currency\n[0] EGP\n[1] USD\n[2] SAR\nPlease choose 0, 1, or 2: "))
    if choice in [0, 1, 2]:
        amount = float(input("Enter amount to deposit: "))
        amount_in_egp = currency_conversion(amount, currencies[choice])
        user["balance"] += amount_in_egp
        print(f"Successfully deposited {amount_in_egp:.2f} EGP. New balance: {user['balance']:.2f}")
    else:
        print("Invalid currency choice.")

def withdraw(user):
    currencies = ["EGP", "USD", "SAR"]
    choice = int(input("Please choose the currency\n[0] EGP\n[1] USD\n[2] SAR\nPlease choose 0, 1, or 2: "))
    if choice in [0, 1, 2]:
        amount = float(input("Enter amount to withdraw: "))
        amount_in_egp = currency_conversion(amount, currencies[choice])
        if user["balance"] >= amount_in_egp:
            user["balance"] -= amount_in_egp
            print(f"Successfully withdrew {amount_in_egp:.2f} EGP. New balance: {user['balance']:.2f}")
        else:
            print("Sorry! Not Enough Money.")
    else:
        print("Invalid currency choice.")

def transfer(user):
    try:
        recipient_id = int(input("Enter the ID of the recipient: "))
        recipient = next(u for u in users if u["ID"] == recipient_id)
    except StopIteration:
        print("Recipient not found.")
        return
    except ValueError:
        print("Invalid ID format.")
        return

    currencies = ["EGP", "USD", "SAR"]
    choice = int(input("Please choose the currency\n[0] EGP\n[1] USD\n[2] SAR\nPlease choose 0, 1, or 2: "))
    if choice in [0, 1, 2]:
        amount = float(input("Enter amount to transfer: "))
        amount_in_egp = currency_conversion(amount, currencies[choice])
        if user["balance"] >= amount_in_egp:
            user["balance"] -= amount_in_egp
            recipient["balance"] += amount_in_egp
            print(f"Successfully transferred {amount_in_egp:.2f} EGP to user with ID {recipient_id}. New balance: {user['balance']:.2f}")
        else:
            print("Sorry! Not Enough Money.")
    else:
        print("Invalid currency choice.")

def check_balance_and_info(user):
    print(f"\nUsername: {user['username']}")
    print(f"Current balance: {user['balance']:.2f} EGP")
    print(f"Phone: {user['phone']}")
    print(f"Email: {user['email']}")
    print(f"Gender: {user['gender']}")
    print(f"Age: {user['age']}")
    print(f"City: {user['city']}")
    print(f"Your ID: {user['ID']}")

def show_menu():
    while True:
        welcome = input("""\nWelcome to SIC Bank System
Would you like to:
[1] Sign up
[2] Login
Please Enter a valid choice (1 or 2): """)

        if welcome == "1":
            logged_in_user = register_user()
            break
        elif welcome == "2":
            logged_in_user = login_user()
            if logged_in_user:
                break
        else:
            print("Invalid choice! Please enter 1 or 2.")

    while True:
        choice = input(f"""\n********** Welcome {logged_in_user['username']} **********\nWhat would you like to do?
1. Deposit
2. Transfer
3. Check Balance & Personal Info
4. Withdraw
5. Exit
Please enter a valid choice (1-5): """)

        if choice == "1":
            deposit(logged_in_user)
        elif choice == "2":
            transfer(logged_in_user)
        elif choice == "3":
            check_balance_and_info(logged_in_user)
        elif choice == "4":
            withdraw(logged_in_user)
        elif choice == "5":
            save_users()
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

show_menu()
