def function_1():
    print("This is the function 1")
    function_2()

def function_2():
    print("This is the function 2")

function_1()


def function_x():
    Message = ("is inside the function")
    print("the function x", Message)

function_x()


counter = 0 

def increase():
    global counter
    counter += 5
   
    
print("before call function", counter)
increase()
print("call function",counter)


def list_num(lista):
    return sum(lista)
print(list_num([4,6,2,29]))


def reverse(word):
    return word[::-1]
print(reverse("Hello World"))

def counter_upper_lower(counter):
    upper =sum(1 for c in counter if c.isupper())
    lower= sum(1 for c in counter if c.islower())
    print(f"There is {upper} upper cases and {lower} lower cases")

counter_upper_lower("I love Nacion Sushi in Heredia, CR")

def order_words(order):
    
    words = order.split('-')
    words.sort()
    result= '-'.join(words)

    return result

print(order_words("python-variable-funcion-computadora-monitor"))

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def filter_primes(lista):
    return [num for num in lista if is_prime(num)]

Numbers_list = [1, 4, 6, 7, 13, 9, 67]
print(filter_primes(Numbers_list))




