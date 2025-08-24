###
# 02 - types()
# Python tiene varios tipos de datos. Tiene TIPADO DINÁMICO – el tipo de una variable 
# se puede modificar durante la ejecución
# int, float, complex, str, bool, Nonetype, list, dict, set, tuple, range,...
###

from os import system
if system("clear") != 0: system("cls")

print("int:")
print(10)
print(0)
print(-5)
print(4325986734598645674567743)
print(type(10)) ## De esta forma Python nos dice el TIPO DE DATO que le pasamos

suma = (None)

print("float:")
print(type(3.14))
print(type(1.0))
print(type(1e3))

print("complex:")
print(type(1 + 2j))

print("str:")
print(type("Hola"))
print(type(""))
print(type("123"))
print(type("""
    Multilinea
"""))

print("bool:")
print(type(True))
print(type(False))
print(type(1 < 2)) ## Cualquier operación lógica es siempre un booleano

print("NoneType:")
print(type(None)) ## Mezcla entre non-defined y NULL. Representa la AUSENCIA DE VALOR

# type es el tipo del resto de tipos
print(type(type))

# TIPADO DINÁMICO
variable = True
print(type(variable))
variable = 42
print(type(variable))