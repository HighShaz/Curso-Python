###
# 05 - input() : entrada de usuario en versión simplificada
# Función que permite obtener datos del usuario a través de
# la consola SIEMPRE en cadena de texto
###

print("Hola, ¿cómo te llamas?:")
nombre = input()
print(f"Hola {nombre}, ¿cómo estás?")

# Se puede incluir el input() dentro del print()
nombre = input("Hola, ¿cómo te llamas?:\n") # Añado el \n para que la entrada de usuario se ponga debajo y no a continuación

# Las entradas por input() SIEMPRE se guardan como str
edad = input("¿Qué edad tienes?")
print(type(edad))
edad = int(edad) # o alternativamente : edad = int(input("¿Qué edad tienes?"))

# Obtener múltiples valores a la vez con split()
country, city = input("¿En qué país y en qué ciudad vives?\n").split()
print(f"Vives en {city}, {country}")

