#print, type, range las funciones son las que llevan parentesis
#ahora haremos las funciones propias
#para definir una funcion necesitamos usar la palabra def(definiendo una nueva funcion, es como los metodos en java)

# def nombre():, si no queremos definir una funciona todavia poner pass
def saludar(nombre):
    print("Hola", nombre)

"""saludar("Alejandra")
saludar("Jorge")
saludar("Damaris")"""

def convertir_a_fahrenheit(c):

    return (c * 1.8) + 32


print("Introduce celcius para pasarlo a fahrenheit:")
celcius = int(input())
fahrenheit = convertir_a_fahrenheit(celcius)
print(fahrenheit)


