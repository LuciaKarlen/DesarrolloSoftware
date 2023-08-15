import random

def generar_lista_de_atletas():
	"""
	Esta función genera aleatoriamente los datos de 20 atletas que participaron de una maratón.
	Devuelve una lista de atletas donde cada atleta es un diccionario con los campos:
		- nombre: el nombre del atleta
		- numero: el número con el que participó en la maratón
		- tiempo_llegada: la cantidad de segundos que tardó en llegar
	"""
	lista_atletas = []
	nombres = ('Daniel', 'Alejandro', 'Pablo', 'Hugo', 'Álvaro', 'Adrián', 'David', 'Sergio', 'Diego')
	apellidos = ('García', 'Rodríguez', 'González', 'Fernández', 'López', 'Martínez', 'Sanchez', 'Pérez')	
	for i in range(1, 21):
		atleta = {
			"nombre": random.choice(nombres)+" "+random.choice(apellidos),
			"numero": i,
			"tiempo_llegada": random.random()*120
		}
		lista_atletas.append(atleta)
	return lista_atletas

#Utilizar la función anterior para generar y almacenar una lista de atletas
listaAtletas = generar_lista_de_atletas()

#Escribir una función que reciba la lista de atletas e imprima una línea por cada atleta respetando el siguiente formato: "<num_atleta> - : (<tiempo_llegada> segundos)", donde <num_atleta> es el número del atleta, su nombre y <tiempo_llegadad> su tiempo de llegada.
def formatoAtletas (lista):
	for persona in lista:
		print(f"{persona['numero']} - {persona['nombre']} : ({persona['tiempo_llegada']:.4f} segundos)")
formatoAtletas(listaAtletas)

#Escribir una función que devuelva el número del atleta que resultó ganador.
def atletaGanador (lista):
	mayorTiempo = 0
	for persona in lista:
		if persona == 0:
			mayorTiempo = persona['tiempo_llegada']
			numAtleta = persona['numero']
		else:
			if persona['tiempo_llegada'] > mayorTiempo:
				mayorTiempo = persona['tiempo_llegada']
				numAtleta = persona['numero']
	return (mayorTiempo, numAtleta)

(mayorTiempo, numAtleta) = atletaGanador(listaAtletas)
print(f"El atleta que resultó ganador fue el número {numAtleta}, con {mayorTiempo:.4f} segundos")

#Escribir una función que, recibiendo el número de atleta de un competidor, devuelva todos sus datos (nombre, número y tiempo de llegadad).
def datosAtleta(numAtleta):
	for persona in listaAtletas:
		if persona['numero'] == numAtleta:
			return(persona)


numAtleta = int(input("Ingrese el número de atleta: "))
print(f"{datosAtleta(numAtleta)}")