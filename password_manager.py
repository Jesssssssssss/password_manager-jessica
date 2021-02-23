# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 11:49:25 2021

@author: jesss
"""

name = input("What is your name? ")

try:
    age = int(input("How old are you? "))
except ValueError:
    print("That is an invalid age. Please enter an integer (e.g. 11)")
    
if age <= 13:
    print("Sorry, you need to be 13 to use this site.")
