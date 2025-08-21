###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

my_name = "Victor Moreno"
city = "argentona"
print(f"Me llamo {my_name}.\nVivo en {city}.")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

print(f"a = {a} y es tipo: {type(a)}")
print(f"b = {b} y es tipo: {type(b)}")
print(f"c = {c} y es tipo: {type(c)}")
print(f"d = {d} y es tipo: {type(d)}")
print(f"e = {e} y es tipo: {type(e)}")

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

cadena = "12345"
print(type(cadena))
cadena = int(cadena)
print(type(cadena))
cadena = float(cadena)
print(type(cadena))
numero = 3.99
numero = int(numero)
print(f"Si transformo en entero el 3.99 se convierte en {numero}, ya que al hacer casting de float a int simplemente se eliminan los decimales")

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")
# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

name = "highShaz"
age = 29
height = 1.76
print(f"¡Hola! Me llamo {name} y tengo {age} años, mido {height}")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

resultado = round(3.1416)
resultado = int(resultado / 2)
print(resultado)