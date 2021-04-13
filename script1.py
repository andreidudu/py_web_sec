#!/bin/python3

#***** importing *****

import sys #system functions and parameters
from menu import call_menu

from datetime import datetime




#***** newline *****

def new_line():
	print('\n')
	
new_line()

#***** print date and time *****

new_line()
print(datetime.now())


#***** login / register *****

users = ["Andrei", "George", "Ion"]
passwords = ["mercedes", "ford", "dacia"]
ages = [18,15,22]
loggedin = 0
while loggedin == 0:
	new_line()
	print("Hi, I am Travis!")

	user = input("What is your name? ").strip().capitalize()
	loggedin=0
	if user in users:
		print("Welcome", user+" ! ")
		
		while (loggedin==0):
			password = input("Please enter your password ")
		
			index = users.index(user)
		
			if (passwords[index] == password):
				print("You are logged in, ",user,"!")
				loggedin=1
				
				
	else:
		register = input("User unknown. Press r to register ").lower()
		if register == "r":
			user = input("Please enter your name! ").strip().capitalize()
			password = input("Please enter your password! ")
			age = input("Please enter your age! ").strip()
			users.append(user)
			passwords.append(password)
			ages.append(int(age))
			loggedin = 1	
	new_line()			
	print("*****HERE COMES THE MENU*****")
	new_line()
	new_line()
	call_menu()
	print(users)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
