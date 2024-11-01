# Ask user to enter their name
#pin1 = 5   #integer
#pin2 = "4" #string
from pickletools import string1

#name = input("What is your name?")
#print(f"It is nice to meet you {name}")
#print("It is nice to meet you",   name)

#ex2
#char1 = input("give char1")
#char2 = input("give char2")
#print("The robots expression is now as follows:")
#print("##########")
#print(f"#  {char1}  {char2}  #")
#print("#  ----  #")
#print("##########")



#pin1 = 1
#pin2 = "1"
#pin3 = str(1)
#ex3
#whole_number1 = input()
#whole_number2 = int(input())

#print(type(whole_number1))
#print(type(whole_number2))


#decimal_number1 = input()
#decimal_number2 = float(input())

#print(type(decimal_number1))
#print(type(decimal_number2))

name = input("What is your name?")

weight = float(input("Please enter your weight: "))
age = int(input("How old are you (in years)?"))
height = float(input("How tall are you (in meters)?"))

print(f"Your name is {name}, you {age} years old and your bmi is {(weight/height*height)} ")