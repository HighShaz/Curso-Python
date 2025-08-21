###
# 03 - Casting de types
# Transformar de un tipo de valor a otro
# Python NO realiza conversiones automáticas entre tipos incompatibles
# TIENE UN TIPADO FUERTE
###

print("Conversión de tipos:")
print(type(int("100"))) # La str "100" la convertimos a int
print(type(str(2)))     # El int 2 lo convertimos a str

#print("100" + 2)   # DA ERROR. El print interpreta que es del tipo que primero se concatena.
#print(2 + "100")   # DA ERROR.
print(int("100") + 2)   #Al hacer el casting sí que permite la operación  
print(str(2) + "100")

# Convertir cadena en float
print(type(float("3.1416")))

# Convertir float a int, bastante útil pero OJO porque simplemente elimina la parte decimal
# pero pierde precisión
# PARA REDONDEAR (ROUND) VER MÁS ABAJO!!!!!!!!!!!!!!!!!
print(int(3.1416))

# Convertir int/float a bool. SOLO el 0 == false.
print(bool(1))
print(bool(0))
print(bool(-1))
print(bool(3.1416))

# Convertir str a bool. SOLO el "" == false. 
print(bool(""))
print(bool(" "))
print(bool("HOLA MUNDO"))

# VALUE ERROR: NO SE PUEDE TRANSFORMAR TODO. 
# print(int("Hola Mundo"))


### 
# FUNCIÓN ROUND().
# Siempre redondea al Par más cercano cuando está en medio (algo.5) 
# para que los redondeos se distribuyan correctamente.
# Así a veces redondea a la alta y otras a la baja.
print(round(2.3))
print(round(2.6))
print(round(2.51))
print(round(2.5))
print(round(3.5))

