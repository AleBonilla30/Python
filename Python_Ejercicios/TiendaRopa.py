from datetime import datetime

print("********************************")
print("******    BIENVENIDO A    ******")
print("***** Tienda los Bonillas ******")
print("********************************")

inventario = {

    "pantalon": 25,
    "pantalon corto": 30,
    "crop top": 40,
    "vestido": 10,
    "sandalia": 20,
    "camiseta": 5,
    "falda": 10,
    "gabardina": 3

}

productos_totales = 0
for item in inventario.values():
    productos_totales += item

print()
print("Ingresa tu nombre:")
nombre = input()
print("Ingresa tu apellido:")
apellido = input()

nombre_completo = nombre +" "+ apellido

print("********************************")
print("Gracias por visitar nuestra tienda,", nombre_completo)


compras = []

def mostrar_menu():
    print()
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print("Selecciona la opcion que deseas")
    print("1. conocer cuantos productos tiene la tienda")
    print("2. comprar productos")
    print("3. Mostrar compras")
    print("4. Salir del programa")
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

def mostrar_inventario():
    print("◇◇◇◇   INVENTARIO   ◇◇◇◇")
    for llave, valor in inventario.items():
        print(f"    {llave}: {valor}")
    print("El total de productos que tenemos en la tienda es:", productos_totales)

def comprar_productos():
    global productos_totales
    carrito = []

    while True:
        print()
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("Que producto quieres comprar?")
        print("Escribe f para terminar o v para ver que contiene tu carrito")
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        productos = input()

        if productos == "f": break
        
        if productos =="v":
            print(f" Tu carrito contiene {carrito}")
            continue
        if productos not in inventario:
            print()
            print(f"Lo sentimos no tenemos ese producto, {productos} en nuestra tienda")
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        elif inventario[productos] == 0:
            print()
            print(f"Lo sentimos no tenemos en stock este, {productos} solicitado ")
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        elif productos not in carrito:
            carrito.append(productos)
        else:
            print()
            print("Este producto ya se encuentra en tu carrito")
    print()
    print("◈◈◈◈ El contenido de tu carrito es ◈◈◈◈")
    for item in carrito:
        print(f"    {item}")
        inventario[item] -= 1
        productos_totales -= 1

    
    fecha = datetime.now()
    compras.append((nombre,carrito, fecha))

def mostar_compras():
    print()
    print("◈◈◈◈   TU LISTA   ◈◈◈◈")
    for compra in compras:
        print(f"{compra[0]}, compro, {compra[1]}, en fecha {compra[2]}")

while True:
    mostrar_menu()
    respuesta = int(input())

    if respuesta == 1:
        mostrar_inventario()
    elif respuesta == 2:
        comprar_productos()
    elif respuesta == 3:
        mostar_compras()
    elif respuesta == 4:
        print()
        print("Gracias por compras en nuestra tienda")
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        break




