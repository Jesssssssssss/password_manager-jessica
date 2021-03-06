# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 11:49:25 2021

@author: jesss
"""
accounts = []
usernames = []
passwords = []
acc_info = [["Username", "Password123"], ["Jess123", "Abcd1234"]]

def add_account():
    acc = input("What account is this for?")
    accounts.append(acc)
    use = input("What is your username?")
    usernames.append(use)
    pas = input("What is your password?")
    passwords.append(pas)
    
def view_info():
    
    for i in range(len(accounts)):
        print("{}:".format(accounts[i]))
        print("Username: {}".format(usernames[i]))
        print("Password: {}".format(passwords[i]))
        
def new_account():
    valid = 0
    acc_username = input("Create a username: ")
    while valid == 0:
        acc_password = input("Create a password (must be at least 8 characters long and include a capital letter and a number): ").strip()
        if (len(acc_password) >= 8) and (any(requirements.isupper() for requirements in acc_password)) and (any(requirements.isdigit() for requirements in acc_password)):
            valid = 1
        else:
            print("Your password is invalid.")
            valid = 0
    acc_info.append([acc_username, acc_password])

def login(): 
    while True:
        acc_username = input("Username: ")
        acc_password = input("Password: ")
        if [acc_username, acc_password] in acc_info:
            print("Logged in!")
            break
        else:
            action = input("Incorrect username or password. Do you want to create a new account (type \"N\") or try again (type \"T\")")
            if action == "N":
                new_account()
                break
            

name = input("What is your name? ")

try:
    age = int(input("How old are you? "))
except ValueError:
    print("That is an invalid age. Please enter an integer (e.g. 11)")
    
if age < 13:
    print("Sorry, you need to be 13 to use this site.")
else:
    while 1 == 1:
        prior_user = input("Do you have an account already? (y/n?) ")
        if prior_user == "y":
            login()
            break
        elif prior_user == "n":
            new_account()
            break
        else:
            print("Please enter either \"y\" or \"n\"")
    while True:
        print()
        print("What do you want to do?")
        print("1. Add new account (username and password)")
        print("2. View passwords")
        print("3. Exit")     
        try:
            number = int(input("Number: "))
            
            if number == 1:
                add_account()
            elif number == 2:
                view_info()
            elif number == 3:
                print("Goodbye!")
                break
            else:
                print("Please enter a valid number (1, 2 or 3)")
        except ValueError:
            print("Please enter a number (1, 2 or 3)")
