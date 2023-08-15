import random

#Muestre la lista
lista = []

for i in range(10):
    numero = random.randint(1, 20)
    lista.append(numero)

print(f"La lista es: {lista}")

#El usuario ingresa debe ingresar un valor un valor. El programa debe informar cuántos valores de la lista son mayores a dicho valor, para eso debe utilizar una función. La función debe recibir como argumentos la lista y un entero, y debe retornar la cantidad de valores de la lista mayores a dicho entero

def numerosMayores(valor, lista):
    contador = 0
    lista2 = []
    for elemento in lista:
        if elemento > valor:
            lista2.append(elemento)
            contador = contador + 1 
    return (lista2, contador)

valor = float(input("Ingrese un valor: "))

(lista2, contador) = numerosMayores(valor, lista)

print(f"La lista con los valores mayores al entero es: {lista2}, con {contador} valores")

#Crear una función que calcule el promedio de la lista y utilizarla.
def promLista (lista):
    suma = 0
    for elemento in lista:
        suma = suma + elemento
    promedio = suma / len(lista)
    return promedio

promedio = promLista(lista)

print(f"El promedio de la primera lista es de {promedio}")

#Crear una función que encuentre el valor más grande y el más pequeño de la lista y los retorne.

def mayoresYmenores(lista):
    mayor = -1
    menor = 21
    for elemento in lista:
        if elemento > mayor:
            mayor = elemento
        elif elemento < menor:
            menor = elemento
    return (mayor, menor)

(mayor, menor) = mayoresYmenores(lista)

print(f"El mayor número de la lista es {mayor} y el menor es {menor}")