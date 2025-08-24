###
# 03 - Listas
# Secuencias mutables de elementos
# Pueden contener elementos de diferentes tipos
###

from os import system
if system("clear") != 0: system("cls")

# Creación de listas
print("\nCrear listas")
lista1 = [1, 2, 3, 4, 5] # lista de enteros
lista2 = ["manzana", "pera", "plátano"] # lista de cadenas
lista3 = [1, "hola", 3.14, True] # lista de tipos mixtos

lista_vacia = []
lista_de_listas = [[1, 2], [3, 4]]
matriz = [[1, 2], [3, 4], [5, 6]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matriz)

# Acceder a elementos por índice
print("\nAcceder a elementos por índice")
print(lista2[0]) # manzanas
print(lista2[1]) # pera
print(lista2[-1]) # plátano. EMPIEZA POR EL FINAL
print(lista2[-2]) # pera. SEGUNDA POSICIÓN DESDE EL FINAL

print(lista_de_listas[1][0]) # 3
print(lista_de_listas[0][1]) # 2
print(lista_de_listas[0][0]) # 1
print(lista_de_listas[1][1]) # 4

# SLICING (rebanado) de listas

lista1 = [1, 2, 3, 4, 5]
print(lista1[1:4]) # [2, 3, 4] coje desde el incio de la primera posición
# indicada hasta el inicio de la segunda, 

