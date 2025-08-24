###
# 02 - Booleanos
# Valores lógicos: True (verdadero) y False (falso)
# Fundamentales para el control de flujo y la lógica en programación
###
from os import system
if system("clear") != 0: system("cls")


print("\nValores booleanos típicos")
print(True)
print(False)

# Operadores de comparación: devuelven un valor booleano
print ("\nOperadores de comparación:")
print("5 > 3", 5 > 3)       # True
print("3 > 5", 3 > 5)       # False
print("5 == 5", 5 == 5)     # True (igualdad)
print("5 != 5", 5 != 5)     # True (desigualdad)

# TABLAS DE LA VERDAD
print("\n\n##TABLAS DE LA VERDAD##")
print("\nand:")
print("A      B      A and B")
print("True   True  ", True and True)
print("True   False ", True and False)
print("False  True  ", False and True)
print("False  False ", False and False)

print("\nor:")
print("A      B      A or B")
print("True   True  ", True or True)
print("True   False ", True or False)
print("False  True  ", False or True)
print("False  False ", False or False)

print("\nnot:")
print("A      not A")
print("True  ",not True)
print("False ",not False)