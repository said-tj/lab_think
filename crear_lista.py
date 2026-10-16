# Para crear una lista con carácteres
print("Creación de Lista general")

# Definimos una lista vacía
lista_alumnos = []

# n de alumnos
n = int(input("Ingresa el número total de alumnos: "))

# Creamos la lista
for i in range(n):
    elemento = input(f" Ingresa el nombre del {i + 1}° alumno: ")
    lista_alumnos.append(elemento)

print(lista_alumnos)