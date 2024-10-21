# This repo created with Ahmed Sayed
# Functionalities:
# User Registration (register_user):

Allows users to create a new account by providing details like username, password, phone, email, gender, age, and city.
Validates the password to ensure it contains at least 8 characters, including both uppercase, lowercase letters, and numbers.
Automatically assigns a unique user ID and initializes the user's balance to 0 EGP.
Saves the account information to a JSON file (database.json).
User Login (login_user):

# Allows users to log in using their user ID and password.
Verifies the credentials by checking if the entered password matches the stored password for the given user ID.
Currency Conversion (currency_conversion):

# Converts a given amount of money from a selected currency (EGP, USD, SAR) into EGP based on predefined exchange rates.
Deposit Money (deposit):

# Enables users to deposit money into their account in one of the supported currencies (EGP, USD, SAR).
The amount is converted to EGP and added to the user's balance.
Withdraw Money (withdraw):

# Allows users to withdraw money from their account in one of the supported currencies.
The system checks if the user has sufficient balance in EGP before proceeding with the withdrawal.
Transfer Money (transfer):

# Allows users to transfer money to another user's account by entering the recipient's user ID.
The transferred amount is converted to EGP and deducted from the sender's balance, then added to the recipient's balance.
It validates if the recipient exists and checks if the sender has enough funds.
Check Balance and Personal Info (check_balance_and_info):

# Displays the user's balance in EGP along with their personal information, such as username, phone number, email, gender, age, city, and ID.
Save Users (save_users):

# Saves the updated list of users and their data to the database.json file after every transaction or user registration.
Main Menu (show_menu):

Serves as the entry point of the application, where users can choose to either sign up or log in.
After logging in, users can select different options: deposit, transfer, check balance and info, withdraw, or exit the system.
It keeps running in a loop until the user decides to exit.
JSON File (database.json):
The users' data, including personal information and balance, is stored in a JSON file. This file is loaded when the program starts and updated after every transaction or new registration.
