#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 08:59:51 2020

@author: stephenchen
"""


# format
'''
s – strings
d – decimal integers (base-10)
f – floating point display
c – character
b – binary
o – octal
x – hexadecimal with lowercase letters after 9
X – hexadecimal with uppercase letters after 9
e – exponent notation
'''

# ValueError: Unknown format code 'd' for object of type 'float'
# print("The temperature today is {0:d} degrees outside !".format(35.567)) 
print("The temperature today is {0:f} degrees outside !".format(35.567)) 
print("The temperature today is {0:d} degrees outside !".format(35)) 

# Convert base-10 decimal integers  
# to floating point numeric constants 
print ("This site is {0:f}% securely {1}!!".format(100, "encrypted")) 


# To limit the precision 
print ("My average of this {0} was {1:.2f}%".format("semester", 78.234876)) 
# My average of this semester was 78.23%
  
# For no decimal places 
print ("My average of this {0} was {1:.0f}%".format("semester", 78.234876)) 
# My average of this semester was 78%

# Convert an integer to its binary or with other different converted bases. 
print("The {0} of 100 is {1:b}".format("binary", -100)) 
# The binary of 100 is -1100100
          
print("The {0} of 100 is {1:o}".format("octal", 100)) 
# The octal of 100 is 144

print("The {0} of 100 is {1:x}".format("hexadecimal", 100)) 
# The hexadecimal of 100 is 64



print ("{}, A computer science portal for geeks."
                        .format("GeeksforGeeks")) 
# GeeksforGeeks, A computer science portal for geeks.

# parameters in format function. 
my_string = "Hi ! My name is {} and I am {} years old."
print (my_string.format("Stephen", 18, 18)) 

#Formatters with Positional and Keyword Arguments :
# Syntax : {0} {1}.format(positional_argument, keyword_argument)
print("{0} eats {1}!!".format("Cat", "Mouse")) 
print("{1} eats {0}!!".format("Cat", "Mouse")) 

# Keyword arguments are called 
# by their keyword name 
print("{name} is a {0} in {1}"
.format("ML scientist", "Amazon", name ="Stephen")) 

'''
for i in range (a, b): 
  
        # Using formatters to give 6  
        # spaces to each set of values 
        print("{:<6d} {:<6d} {:<6d} {:<6d}"
        .format(i, i ** 2, i ** 3, i ** 4)) 
'''
# Function prints the organized set of values 
def organized(a, b): 
    for i in range (a, b): 
        # Using formatters to give 6  
        # spaces to each set of values 
        print("{:<8d} {:<8d} {:<8d} {:<8d}"
        .format(i, i ** 2, i ** 3, i ** 4)) 
    for i in range (a, b): 
        # Using formatters to give 6  
        # spaces to each set of values 
        print("{:^8d} {:^8d} {:^8d} {:^8d}"
        .format(i, i ** 2, i ** 3, i ** 4)) 
    for i in range (a, b): 
        # Using formatters to give 6  
        # spaces to each set of values 
        print("{:>8d} {:>8d} {:>8d} {:>8d}"
        .format(i, i ** 2, i ** 3, i ** 4)) 
        
    
organized(2,8)