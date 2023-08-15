monto = float(input("Ingrese el monto de la compra: "))
if (monto >= 3500):
    montoTotal = monto - (monto * 0.1)
else:
    montoTotal = monto
print(f"El monto a pagar es: {montoTotal}")