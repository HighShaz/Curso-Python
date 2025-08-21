###
# 04 - Variables
# Las variables sirven para guardar datos en memoria.
# Python es uin lenguaje de tipado dinámico y de tipado fuerte.
###

# Para asignar una variable solo hace falta:
my_name = "victor"
print(my_name)

age = 29
print(age)

age = 39
print(age)

# TIPADO DINÁMICO: el tipo de dato se determina en tiempo de ejecución
# no se tiene que decalarar explícitamente
name = "victor"
print(type(name))

name = 32
print(type(name))

# TIPADO FUERTE: Python no realiza conversiones de forma automática
#print(10 + "2")

# f-string (literal de cadena de formato) --> desde la versión Python 3.6
print(f"Hola soy {my_name}, tengo {age - 10} años.")

###
# Python NO tiene CONSTANTES, pero se pueden simular.
# Se escriben en MAYUS, pero realmente se les puede modificar el valor
###


# NO recomendada forma de declarar variables
name, age, city = "victor", 29, "argentona"

# CONVENCIONES para declarar variables
mi_nombre_de_variable = "ok"    # snake_case RECOMENDADO
nombre = "ok"
mi_nombre_de_variable_123 = "ok"

# CONVENCIÓN para declarar 'constantes' (aunque realmente no existen en Python...)
CODIGO_POSTAL = "08310"
# CODIGO_POSTAL = 00000, cambiaría de valor, pero al ponerse en mayus se entiende que no debe

# Declaraciones no aceptadas o que producen error
# MiNombreDeVariable = "ko"
# 123_mi_nombre_de_variable = "ko" # las variables no pueden empezar por número
# mi-variable = "ko"

# Evitar las palabras reservadas: True, False, if, and, else,...
# true = false

# AGREGAR tipado a variables (type hints)
is_user_logged_in: bool = True
print(is_user_logged_in)
# Aún así, Python tiene tipado dinámico y no estático... Con lo que se puede modificar el tipo
is_user_logged_in = "now a string"
is_user_logged_in = 29
print(is_user_logged_in)
# Se puede modificar el editor en ajustes para que te avise si detecta que modificar el tipado
# de una variable previamente tipada (Type Cheking Mode - Strict) pero se sigue ejecutando






