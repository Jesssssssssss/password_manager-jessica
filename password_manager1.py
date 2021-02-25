# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 11:49:25 2021

@author: jesss
"""

usernames = []
passwords = []

name = input("What is your name? ")

try:
    age = int(input("How old are you? "))
except ValueError:
    print("That is an invalid age. Please enter an integer (e.g. 11)")
    
if age <= 13:
    print("Sorry, you need to be 13 to use this site.")
else:
    while 1 == 1:
        print("-----------------------")
        print("What do you want to do?")
        print("1. Add new password ")
        print("2. View passwords")
        print("3. Exit")
        
        try:
            number = int(input("Number: "))
            
            if number == 1:
                #add function here
                print()
            elif number == 2:
                #add function here
                print()
            elif number == 3:
                print("Goodbye!")
                break
            else:
                print("Please enter a valid number (1, 2 or 3)")
        except ValueError:
            print("Please enter a number (1, 2 or 3)")
    
