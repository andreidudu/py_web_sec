#!/bin/python3

#***** menu *****

#***** importing *****
import sys





def call_menu():		
	print("**************** Main Menu ****************")
	


	choice = input("""
		A. Phishing Tool - Copy a Webpage
		B. Password Strength Check
		C. Security Tips & Tricks
		D. Website Scanner
	
********************************************
				""")
	print()	

	
	if choice == "A" or choice =="a":
		print("fishy stuff")
		import phishing
		
	elif choice =="B" or choice =="b":
		from pass_strength import checkPass

	elif choice == "C" or choice =="c":
		log = open("info", "r")	
		for line in log:
    			print(line)
    			
	elif choice =="D" or choice =="d":
		import main
	
	else:
		print("Please choose between A, B, C, D")
		print("Please try again!")
		
	call_menu()

