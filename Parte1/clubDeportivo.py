nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if(edad>=13 and edad<15):
    print("Se encuentra en la categoría INFANTIL")
elif(edad>=15 and edad<17):
    print("Se encuentra en la categoría CADETE")
elif(edad>=17 and edad<19):
    print("Se encuentra en la categoría JUVENIL")
elif(edad>=19):
    print("Se encuentra en la categoría MAYOR")
else:
    print("No tiene categoría, es menor de edad")
