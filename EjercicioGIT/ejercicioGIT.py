print("Bienvenido!")

valor1 = input("Ingrese el 1° valor: ")
valor2 = input("Ingrese el 2° valor: ")

print("-----------------------------------------")
print("MENU:")
print("-----------------------------------------")
print("1. Ingresar valor 1")
print("2. Ingresar valor 2")
print("3. Mostrar suma")
print("4. Mostrar resta")
print("5. Mostrar multiplicación")
print("6. Mostrar división")
print("7. Salir")

opcion = input("Elija una opción: ")

while (opcion != 7):
    if (opcion == 1):
        valor1 = input("Ingrese el 1° valor: ")
        print(f"Los valores son: \nVALOR 1:{valor1} \nVALOR 2:{valor2}")
    elif(opcion == 2):
        valor2 = input("Ingrese el 2° valor: ")
        print(f"Los valores son: \nVALOR 1-->{valor1} \nVALOR 2-->{valor2}")
    elif(opcion == 3):
        suma = valor1 + valor2
        print(f"La suma entre {valor1} y {valor2} es: {suma:.2f}")
    elif(opcion == 4):
        resta = valor1 - valor2
        print(f"La resta entre {valor1} y {valor2} es: {resta:.2f}")
    elif(opcion == 5):
        multiplicacion = valor1 * valor2
        print(f"La multiplicación entre {valor1} y {valor2} es: {multiplicacion:.2f}")
    elif(opcion == 6):
        division = valor1 / valor2
        print(f"La división entre {valor1} y {valor2} es: {division:.2f}")
    print("-----------------------------------------")
    print("MENU:")
    print("-----------------------------------------")
    print("1. Ingresar valor 1")
    print("2. Ingresar valor 2")
    print("3. Mostrar suma")
    print("4. Mostrar resta")
    print("5. Mostrar multiplicación")
    print("6. Mostrar división")
    print("7. Salir")
    opcion = input("Elija una opción: ")

print("Nos vemos!")