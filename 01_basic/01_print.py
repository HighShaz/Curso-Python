##
# 01- print()
# El módulo print()= es el módulo que nos permite imprimir en consola
# Sirve para mostrar información en consola
##

from os import system
if system("clear") != 0: system("cls")

# Utilizar comilla doble o simple según lo que se vaya a imprimir. Si queremos poner algo con
# comilla simple dentro, utilizar la comilla doble para todo y viceversa.
print("Hola, 'Mundo'!")
print('También "funciona" con una sola comilla')

# Para imprimir múltiples valores (utiliza el 'espacio' como separador por defecto)
print("Python", "es", "genial")

# Para modificar el separador
print("Python", "es", "la", "leche", sep="-") 

## Para modificar el cambio de línea, que por defecto será un salto de línea \n

print("Esto se imprime en una línea", end = " ")

print("en una línea")


## Para añadir un salto de línea

print()


## Imprimir números o variables
print(42)
variable = 43
print(variable)
