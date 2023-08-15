sumaTemp=0
contador=0
for i in range (5):
    print(f"Ingrese la temperatura para el día {i}")
    temp = float(input())
    sumaTemp = sumaTemp + temp
    contador=contador+1
promedio = sumaTemp/contador
print(f"El promedio de las temperaturas ingresadas es de: {promedio}°C")

