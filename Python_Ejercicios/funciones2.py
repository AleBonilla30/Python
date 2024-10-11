"""nombre = "Alejandra"
print("Longitud del nombre", len(nombre))
#abs es el valor absoluto que le pasamos por parametros por ejemplo imprimir un numero 
print(abs(-10))
#para imprimir numeroa aleatorios usamos random, pero hay que impprtarlo
#randint(min, max)---> este es para imprimir numero aleatorios enteros
import random
resultado = random.randint(1, 10)
print(resultado)"""

def saludar_y_sumar(nombre, num1, num2):
    print("Saludos,", nombre)
    print("Resultado de la suma", num1+num2)

saludar_y_sumar("Alejandra", 5, 10)