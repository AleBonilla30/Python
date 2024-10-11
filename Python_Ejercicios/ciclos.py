#ciclos o bucles
#while mientras el codigo sea verdadera seguira ejecutando 
"""numero = 0
while numero < 10:
    if numero < 5:
        print("El numero,", numero, "Es menor que 5")
    else:
        print("El numero,", numero, "es mayor a 5")
    
    numero += 1
print("Termino la iteracion")"""

#ciclo for
#for x in "Alejandra":
  # print(x)
#la funcion range si le pones un numero lo que hace es imprimir la lista de esos numeros
#la funcion range puede recibir dos parametros en lugar de 1 el primero es inclusivo y el segundo no

#for x in range(1, 11):
    #print(x)

while True:
    print("Escribe la opcion deseada:")
    print("1. Saludar")
    print("2. Salir")

    respuesta = int(input())

    if respuesta == 1:
        print("Saludos terricola")
    elif respuesta == 2:
        break
print("Terminando programa.....")