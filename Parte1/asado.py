cantInvitados = int(input("Ingrese la cantidad de invitados: "))
precioCarne = float(input("Ingrese el precio de la carne: "))
kgXpersona = 0.7
kgTotales = kgXpersona * cantInvitados
total = kgTotales * precioCarne
print(f"Deberá pedirle al carnicero {kgTotales}kg. de carne y el total será de {total:.2f}")