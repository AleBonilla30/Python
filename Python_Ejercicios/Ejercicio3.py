print("******  Bienvenido  ******")

def miFuncion(nombre, num1, num2):
    print("vas a ", nombre)
    if nombre == "Suma":
        print("El resultado es:", num1 + num2)
    elif nombre == "Resta":
        print("El resultado es:", num1 - num2)
    elif nombre == "Multiplicar":
        print("El resultado es:", num1 * num2)
    elif nombre == "Dividir":
        print("El resultado es:", num1 / num2)
    else:
        print("Opciòn no valida")

miFuncion("Suma", 2, 6)
miFuncion("Multiplicacion", 5, 8)
miFuncion("Division", 20, 5)
print("=====================")
print("Finalizando programa....")