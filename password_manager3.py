# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 11:49:25 2021

@author: jesss
"""
user_info = []
accounts = []
usernames = []
passwords = []
valid = 1

def add_account():
    acc = input("What account is this for?")
    accounts.append(acc)
    un = input("What is your username?")
    usernames.append(un)
    pas = input("What is your password?")
    passwords.append(pas)
    
def view_info():
    i = 0
    while i <= len(accounts):
        print(accounts[i], ":")
        print(usernames[i], ":")
        print(passwords[i], ":")
        i =+ 1
        
def new_account():
    valid = 0
    while valid == 0:
        username = input("Create a username: ")
        password = input("Create a password (must be at least 8 characters long) ")
        if len(password) <= 7:
            print("Your password is")
            valid = 0

name = input("What is your name? ")

try:
    age = int(input("How old are you? "))
except ValueError:
    print("That is an invalid age. Please enter an integer (e.g. 11)")
    
if age <= 13:
    print("Sorry, you need to be 13 to use this site.")
else:
    while 1 == 1:
        prior_user = input("Do you have an account already? (y/n?)")
        if prior_user == "y":
            login()
            break
        elif prior_user == "n":
            new_account()
            break
        else:
            print("Please enter either \"y\" or \"n\"")
    while 1 == 1:
        print("-----------------------")
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
                print()
            elif number == 3:
                print("Goodbye!")
                break
            else:
                print("Please enter a valid number (1, 2 or 3)")
        except ValueError:
            print("Please enter a number (1, 2 or 3)")
    
