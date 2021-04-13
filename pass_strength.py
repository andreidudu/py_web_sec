#!/bin/python3
def checkPass(password, pre_pass,name_f, name_s):
    length = int()
    lower = int()
    upper = int()
    special = int()
    number = int()
    like_past = int()
    f_name = int()
    l_name = int()
    password_strength = 0
    if len(new_password)>=8 :
        length = 1
    for i in lower_alphabet:
        if i in new_password:
            lower = 1
    for i in upper_alphabet:
        if i in new_password:
            upper = 1
    for i in special_characters:
        if i in new_password:
            special = 1
    for i in numbers:
        if i in new_password:
            number = 1
    if name_f.lower() not in new_password.lower():
        f_name = 1
    if name_l.lower()not in new_password.lower():
        l_name = 1
    if pre_pass.lower() not in new_password.lower():
        like_past = 1
    
    if length == 1:
        password_strength += 1
    if lower == 1 :
        password_strength += 1
    if upper== 1 :
        password_strength += 1
    if special == 1:
        password_strength +=2
    if f_name != 1:
        password_strength -=2
    if l_name != 1:
        password_strength -=2
    if like_past != 1:
        password_strength -=1
    
    password_rank = str()
    
    if password_strength >= 5:
        password_rank = 'Very Strong'
    elif password_strength == 4:
        password_rank = 'Strong'
    elif password_strength == 3:
        password_rank = 'OK'
    elif password_strength == 2:
        password_rank = 'Not Good'
    elif password_strength ==1:
        password_rank = 'Bad'
    elif password_strength < 1:
        password_rank = 'Very Bad'
    print('\nI think that your password is ',password_rank)
    issues = [length, lower, upper, special, number, like_past, f_name, l_name, password_rank]
    return issues

lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
special_characters = [' ', '!', '#', '$', '%', '&', '"', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',"'"]

choice = None

print("""
***** Welcome to our password strength checker! *****
""")

while choice != '0':
    print("""
***** tool options *****
    1 - Check Password Strength
    0 - Exit

    
""")
    choice = str(input('Please enter your choice: '))
    if choice == '1':
        new_password = input('\nPlease enter your new password: ')
        old_password = input('\nPlease enter your old password: ')
        name_f = input('\nPlease enter your first name: ')
        name_l = input('\nPlease enter your last name: ')
        issues = checkPass(new_password,old_password,name_f,name_l)
        why = input('\nWould you like to find out why? (yes|no): ')
        if why.lower() == 'yes':
            if issues[0] != 1:
                print("It's too short")
            if issues[1] != 1:
                print("It doesn't have a lower case character in it")
            if issues[2] != 1:
                print("It doesn't have an upper case character in it")
            if issues[3] != 1:
                print("It doesn't have a special character in it")
            if issues[4] != 1:
                print("It doesn't have a number in it")
            if issues[5] != 1:
                print("It's like your old password")
            if issues[6] != 1:
                print("It's got your first name in it")
            if issues[7] != 1:
                print("It's got your last name in it")
            if issues[8] == 'Very Strong':
                print('There is nothing wrong with it!')
    elif choice == '0':
        print('Goodbye')
    else:
        print('Choice is invalid, please try again')
        

