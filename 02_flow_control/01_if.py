###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones
###

import os # importar módulo del S.O., para acceder a cualquier comando del sistema
os.system("clear") # ejecutamos el comando "clear" al incio del programa para que
                   # se borren las ejecuciones anteriores de la consola

print("Sentencia simple condicional")
edad = 18

# El bloque de código que interpreta Python que está en el if, es lo que está
# tabulado justo debajo. NO se utilizan en este caso ni paréntesis ni ;
if edad >= 18: ####### ACTIVAR LIGADURAS EN AJUSTES PARA VER MEJOR EL SÍMBOLO >=
    print("Eres mayor de edad")
    print("Felicidades")

edad = 15
if edad >= 18:
    print("Eres mayor de edad")
    print("Felicidades")

print("Sentencia condicional con else")
if edad >= 18:
    print("Eres mayor de edad")
    print("Felicidades")
else:
    print("Eres menor de edad")
    print("Felicidades")

# Con el condicional elif, siempre se ejecuta la primera condición que se cumple de arriba a abajo.
# No es necesario hacer operaciones lógicas como AND o OR.
print("\n\nSentencia condicional con elif")
nota = 8
if nota >= 9: # Si se cumple esta condición ignorará las siguientes
    print("Enhorabuena, tienes un excelente!")
elif nota >= 7:
    print("Enhorabuena, tienes un notable!")
elif nota >= 5:
    print("Enhorabuena, has aprobado!")
elif nota < 5:
    print("Lo siento, has suspendido...")
else:
    print("La nota debe estar en un rango entre 0 y 10")

###
# OPERADORES LÓGICOS
# and --> si True y True devuelve True / si True y False devuelve False
# or --> si True y True devuelve True / si True y False devuelve True / si False y False
#        devuelve False
# not --> Devuelve el contrario. Si algo es True devuelve False y viceversa
###

print("\n\nCondiciones múltiples")
edad = 16
tiene_carnet = False

if edad >= 18 and tiene_carnet:
    print("Puedes conducir 🚗")
else:
    print("POLICIAAAAA!!!!!!!!!!!!! 🚓")

# imaginemos que estamos en Venezuela...
if edad >= 18 or tiene_carnet:
    print("Puedes conducir 🚗")
else:
    print("Soborna al policía...")

es_fin_de_semana = False
if not es_fin_de_semana:
    print("A currar!!!")
else:
    print("A descansar...")

# Intentar evitar el anidar condicionales... Cuanto menos profundidad tengan los
#anidados mejor, porque cuanto más profundos sean más complejos son.
print("\n\nAnidar condicionales")
edad = 18
tiene_dinero = False
if edad >= 18:
    if tiene_dinero:
        print("Sal de fiesta!!!")
    else:
        print("Quédate en casa...")
else:
    print("No tienes la edad para salir de fiesta.")

# Más sencillo de esta manera, sin anidar:
#if edad < 18:
#    print("No tienes la edad para salir de fiesta.")
#elif tiene_dinero:
#    print("Sal de fiesta!!!")
#else:
#    print("Quédate en casa...")

numero = 5
if numero:
    print("El número no es cero.") # True

numero = 0
if numero:
    print("Aquí no entrará nunca.") # False

nombre = "Juan"
if nombre:
    print("El nombre no está vacío, es ", nombre)

nombre = ""
if nombre:
    print("Aquí nunca entrará.")

numero = 3 # asignación
es_el_tres = numero == 3 # comparación. Si numero es igual a tres, se asigna a es_el_tres
if es_el_tres:
    print("Es el número 3")

print("\n\nLa condición ternaria")
# es una forma concisa de un if-else en un línea de código
# [código si cumple la condición] if [condición] else [código si no cumple]
edad = 19
mensaje = "Es mayor de edad" if edad >= 18 else "No es mayor de edad"
print(mensaje)