#import secret, string and random module
import secrets
import string
import random
#assign values to variables
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
#create variable combination
selection_list = letters + digits + special_chars
#ask user to input length of password
password_len = int(input("Enter length of password:"))
password = ''
for i in range(password_len):
    password+= ''.join(secrets.choice(selection_list))
print("Your password is:",password)