"""
1. Cree un diccionario que guarde la siguiente información sobre un hotel:
    - nombre
    - numero_de_estrellas
    - habitaciones
El value del key de 'habitaciones' debe ser una lista, y cada habitación debe tener la siguiente información:
    - numero
    - piso
    - precio_por_noche
"""

hotel ={
    "Name": "Riu",
    "Stars": 2,
    "room":[
        {
            "number":5,
            "Floor":1,
            "Price":100,

        }
    ]
}
print(hotel)
"""
1. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
    1. Ejemplos:
    2. `list_a = [first_name, last_name, role]`
    `list_b = [Alek, Castillo, Software Engineer]`
    → `{first_name: Alek, last_name: Castillo, role: Software Engineer}`
"""
list_a = ["first_name", "last_name","role"]
list_b = ["Alek","Castillo","Software_Engineer"]

person={}

if len(list_a) == len(list_b):
    for index in range(len(list_a)):
        person[list_a[index]] = list_b[index]
    print("The Dictionary is:  ")

    print(  person  )
    for value in person.values():
        print(value)


"""
2. Cree un programa que use una lista para eliminar keys de un diccionario.
    1. Ejemplos:
    2. `list_of_keys = [’access_level’, ‘age’]`
    `employee = {’name’: ‘John’, ‘email’: ‘john@ecorp.com’, ‘access_level’: 5, ‘age’: 28}`
    → `{’name’: ‘John’, 'email’: ‘john@ecorp.com’}`
"""


list_of_keys = ['access_level', 'age']
employee = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}

for key in list_of_keys:
    employee.pop(key,None)
print(employee)