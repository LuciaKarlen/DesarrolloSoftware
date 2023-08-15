# -*- coding: utf-8 -*-
import db_productos

# TODO #1b: cargar la lista de productos con la función
#          cargar_productos() del módulo db_productos.
productos = db_productos.cargar_productos()

# TODO #2: definir una función mostrar_productos()
#          que reciba la lista de productos, no retorne nada,
#          y muestre la lista utilizando el siguiente formato para cada producto:
# "Producto {id}"
# "{nombre} ${precio}"
# "---"
# "Producto {id}"
# "{nombre} ${precio}"
# "---"
# ...
def mostrar_productos(productos):
    for producto in productos:
        print(f"Producto {producto['id']}")
        print(f"{producto['nombre']} ${producto['precio']}")
        print("---")
mostrar_productos(productos)
# TODO #3: definir una función calcular_precio_actualizado()
#          que reciba: el precio anterior y porcentaje de aumento
#          y retorne: el precio con el aumento.

def calcular_precio_actualizado(precioAnterior, porcentajeAumento):
    precioActual = precioAnterior + (precioAnterior*porcentajeAumento)
    return precioActual

porcentajeAumento = 0.1

for producto in productos:
    precioAnterior = producto['precio']
    precioActual = calcular_precio_actualizado(precioAnterior, porcentajeAumento)
    print(f"El precio anterior del producto {producto['nombre']} era de {precioAnterior} y ahora es de {precioActual}")

# TODO #4: Crear una función actualizar_precios() que reciba la lista de productos y 
#          el porcentaje de aumento. La función debe recorrer cada producto de la
#          lista e invocar calcular_precio_actualizado() (a la cual tendrá que pasarle
#          el precio del producto y el porcentaje de aumento) para obtener el precio
#          actualizado y modifique la lista "in-place" actualizando el precio de cada
#          producto. La función no debe retornar nada sino dejar modificada la lista
#          pasada por el usuario.

def actualizar_precios(productos, porcentaje):
    for producto in productos:
        precioActual = calcular_precio_actualizado(producto['precio'], porcentaje)
        producto['precio'] = precioActual
        print(f"Producto {producto['id']}")
        print(f"{producto['nombre']} ${producto['precio']}")
        print("---")

actualizar_precios(productos, porcentajeAumento)

#if __name__ == '__main__':
    # TODO #5a: mostrar la lista cargada
for producto in productos:
    print(f"Producto {producto['id']}")
    print(f"{producto['nombre']} ${producto['precio']}")
    print("---")
    # TODO #5b: el usuario debe ingresar el porcentaje de aumento
porcentajeAumento = float(input("Ingrese el porcentaje de aumento, como 0.1: "))
    # TODO #5c: usar la función actualizar_precios() para actualizar los precios de la lista
actualizar_precios(productos, porcentajeAumento)
    # TODO #5d: mostrar la lista con los precios actualizados
print(productos)