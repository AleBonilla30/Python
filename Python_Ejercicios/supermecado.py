from datetime import datetime

print("********************************")
print("******    BIENVENIDO A    ******")
print("****   SUPERMERCADO MADRID   *****")
print("********************************")

inventario = {
    "leche": 20,
    "huevos": 25,
    "pan": 5,
    "azucar": 10,
    "chocolate": 2,
    "yogur": 10
}

productos_totales = 0
for val in inventario.values():
    productos_totales += val

compras = []

def mostrar_menu():
    print()
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print("Selecciona la opcion que deseas")
    print("1: conocer cuantos productos tiene el supermercado")
    print("2: comprar productos")
    print("3. Mostrar compras")
    print("4. Salir del programa")

def mostrar_inventario():
    print("◇◇◇◇   INVENTARIO   ◇◇◇◇")
    for llave, valor in inventario.items():
        print(f"    {llave}: {valor}")
    print("El total de productos que tenemos el supermecado es:", productos_totales)

def comprar_productos():
    carrito = []
    while True:
        print()
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("Que producto quieres comprar?")
        print("Escribe f para terminar o v para ver que contiene tu carrito")
        productos = input()

        if productos == "f": break

        if productos == "v":
            print(f"Tu carrito contiene {carrito}")
            continue
        if productos not in inventario:
            print(f"Lo sentimos no tenemos ese producto {productos}")
        elif inventario[productos] == 0:
            print(f"Lo sentimos no tenemos en stock el producto {productos}") 
        elif productos not in carrito:
            carrito.append(productos)
        else:
            print("Ese producto ya se encuentra en tu carrito")
    
    print("◈◈◈◈ El contenido de tu carrito es ◈◈◈◈")
    for producto in carrito:
        print(f"    {producto}")
        inventario[producto] -= 1
    
    fecha = datetime.now()
    compras.append((carrito, fecha))

def mostrar_compra():
    print("◈◈◈◈   TU LISTA   ◈◈◈◈")
    for compra in compras:
        print(f"Tu carrito de la compra tiene {compra[0]}, en la fecha {compra[1]}")

while True:
    mostrar_menu()
    respuesta = int(input())

    if respuesta == 1:
        mostrar_inventario()
    elif respuesta == 2:
        comprar_productos()
    elif respuesta == 3:
        mostrar_compra()
    elif respuesta == 4:
        print("Terminado programa....")
        break


