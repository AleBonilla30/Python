print("Introduce un numero entre 1 y 100:")
numero = input()

numero = int(numero)

if numero < 1:
    print("Por favor ingrese un numero mayor a 0")
elif numero > 100:
    print("Porfavor ingrese un numero menor o igual a 100")
else:
    print("Muy bien,", numero, "es una gran opcion")