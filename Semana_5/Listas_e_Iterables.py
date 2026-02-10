
"""Ejercicios de listas e iterables"""
first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = [ 'casos', 'los', 'la', 'por', 'es', 'util']

for index in range(0,len(first_list)):
    print(first_list[index], second_list[index])
    
"""2."""
my_string=  'pizza con piña'

for index in range(len(my_string)-1,-1,-1):
    print(my_string[index])
    
""" 3."""
Countries= ['france', 'mexico', 'usa', 'germany']

if len(Countries)>= 2:
    Countries[0],Countries[-1]=Countries[-1],Countries[0]
    print(Countries)

""" 4."""
my_list = [1,2,3,4,5,6,7,8,9]

even_numbers = []

for number in my_list:
    if number %2 == 0:
        even_numbers.append(number)
print(even_numbers)

"""5."""
numbers = []

for index in range(5):
    number = int(input(f'Enter number {index + 1}:'))
    numbers.append(number)

print('Numbers entered:', numbers)
highest_number = max(numbers)
print('the hightes number was', highest_number)

    