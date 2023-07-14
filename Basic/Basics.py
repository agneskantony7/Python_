print("   /|")
print("  / |")
print(" /  |")
print("/___|")

#VARIABLES
character_name = "John" #String
Character_age = 50 # or "50" #Integer
is_male = False #Boolean
print("There once was a man named " + character_name + ",")
print("he was " + str(Character_age) +" years old")
character_name = "mike"
print("he really liked " + character_name)

#STRINGS
print("Giraffe\nAcademy")
print("Giraffe\"Academy")
print("Giraffe\Academy")
phrase = "Hello cutie"
print(phrase)
print(phrase + " mom")
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase[-1])
print(phrase.index("e"))
print(phrase.replace("cutie","sweetie"))

#NUMBERS
from math import *
print(2)
print(2.5465)
print(-262.2)
print(3+4)
print(3+54.1) #or */-
print(3*(5/4))
print(10%3)
my_num = 7
print(str(my_num) + " is my favourite number")
a=-7
print(abs(a))
print(pow(3,2))
print(max(85,65))
print(min(85,65))
print(round(5.145))
print(floor(3.7))
print(ceil(3.7))
print(sqrt(49))

#INPUT FROM USER
Name = input("Enter Your Name: ")
Age = input("Enter Your Age: ")
print("Hello " + Name +"!")
print("Your Age is " + Age )

#CALCULATOR FUNCTION

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)
print(result)

#MAD LIBS GAME
color = input("Enter a color ")
plural_noun = input("Enter a plural noun ")
celebrity = input("Enter a celebrity ")
print("Roses are" + color )
print(plural_noun + " are blue")
print("I Love " + celebrity )





