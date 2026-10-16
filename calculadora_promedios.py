# Calculadora para calcular el promedio de n números
import statistics

print("Hola, ingresa el número total de elementos a los cuales vamos a promediar")

n = int(input("n = "))

# Definimos mi lista vacia
lista = []

# Creamos la lista
for i in range(n):
    elemento = float(input(f"Ingresa el {i + 1}° valor: "))
    lista.append(elemento)

promedio = statistics.mean(lista)

print(f"El promedio de los elementos es: {promedio}")