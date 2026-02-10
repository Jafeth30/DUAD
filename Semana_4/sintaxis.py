#1.

print("Practice"+ " Syntax" ) # string + string   #Practica Sintaxis

print("practice" + 30)  #string + int #TypeError: can only concatenate str (not "int") to str

print(99 + "practice") #int + string #TypeError: can only concatenate str (not "int") to str

print([20, 30, 40] + [1, 2, 3]) #List + list [20, 30, 40, 1, 2, 3]

print(220.5 +850) # float + int 1070.5

print(True + True) #2  #BOOLEAN + BOOLEAN
print(True + False)#1

#-----------------------------------------------------------------------

#2. Cree un programa que le pida al usuario su nombre, apellido, y edad, y 
#muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

def classify_age(age):
    if age < 3 :
        return "beby"
    elif age <12:
        return "kid"
    elif age <15:
        return "Tween"
    elif age <18:
        return "teenager"
    elif age <25:
        return "young adult"
    elif age <60:
        return "adult"
    else:
        return "older adult"

name = input('Enter your name: ')
last_name = input('Enter your last name: ')
age = int(input('Enter your age: '))

category  = classify_age(age)

print(f"Your name is {name} {last_name}, you are {age} years old and you are a {category}.")

# 3. Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el 
    # usuario adivine el numero.

import random

secret_number = random.randint(1, 10)

print("This is the secret number game")

while True:
    try:
        guess = int(input('Enter the secret number: '))

        if guess == secret_number:
            print("This is the secret number")
            break
        elif guess < secret_number:
            print('That is not the correct number')
        else:
            print('That is not the correct number')
    except ValueError:
        print("Please enter a valid number")
        
        