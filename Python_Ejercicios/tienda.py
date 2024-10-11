from datetime import datetime

print("********************************")
print("******    BIENVENIDO A    ******")
print("**** La tienda de mascotas *****")
print("********************************")

inventario = {
    "perro": 10,
    "gato": 8,
    "pajaro": 25,
    "iguana": 2,
    "tortuga": 5
}

animales_totales = 0
for val in inventario.values():
    animales_totales += val

print("Por favor ingresa tu nombre")
nombre = input()
print("Por favor escribe tu apellido")
apellido = input()

#concatenacion es tomar dos datos de tipo texto y juntarlos, se puede hacer con la suma, ya que python no los suma como los enteros las variables de tipo string si no que los junta
#para agregar un espacio a los nombre y apellidos a ña hora de imprimir vamos agregar ""
nombre_completo = nombre +" "+ apellido

print("Gracias por visitarnos,", nombre_completo)

compras = []

def mostrar_menu():
    print()
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print("Selecciona la opcion que deseas")
    print("1: conocer cuantos animales tiene la tienda")
    print("2: comprar un animal")
    print("3. Mostrar compras")
    print("4. Salir del programa")

def mostrar_inventario():
    print("◇◇◇◇   INVENTARIO   ◇◇◇◇")
    for llave, valor in inventario.items():
        print(f"    {llave}: {valor}")
    print("El total de animales que tenemos en la tienda es:", animales_totales)

def comprar_animal():
    carrito = []
    while True:
        print()
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("Que animal quieres comprar? solo puedes comprar uno de cada especie")
        print("Escribe f para terminar o v para ver que contiene tu carrito")
        animal = input()
        if animal == "f": break

        if animal == "v":
            print(f"Tu carrito contiene {carrito}")
            continue
        if animal not in inventario:
            print(f"Lo sentimos, no contamos con el animal {animal}")
        elif inventario[animal] == 0:
            print(f"Lo sentimos no tenemos en existencia el animal {animal}")
        elif animal not in carrito:
            carrito.append(animal)
        else:
            print("Ese animal ya se encuentra en tu carrito")
        #print("Has comprado un,", animal)
    print("◈◈◈◈ El contenido de tu carrito es ◈◈◈◈")
    for animal in carrito:
        print("  ", animal)
        inventario[animal] -= 1
    
    fecha = datetime.now()
    
    compras.append((nombre, carrito, fecha))

def mostrar_compras():
    print()
    print("◈◈◈◈   COMPRAS REALIZADAS   ◈◈◈◈")
    for compra in compras:
        print(f" {compra[0]} compro {compra[1]} en {compra[2]}")


while True:
    mostrar_menu()
    respuesta = int(input())

    if respuesta == 1:
        mostrar_inventario()
        
    elif respuesta == 2:
        comprar_animal()
    elif respuesta == 3:
        mostrar_compras()

    elif respuesta == 4:
        print("Terminando programa....")
        break





