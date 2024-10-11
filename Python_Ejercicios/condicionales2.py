print("Escribe tu nombre")
nombre = input()
print("Escribe tu edad:")
edad = int(input())

if nombre == "Alejandra" and edad >= 20:
    print("Saludos Alejandra, eres un adulto")
elif nombre == "Alejandra" and edad < 20:
    print("Saludos Alejandra, eres una joven")
elif nombre == "Damaris" or nombre == "Jorge":
    print("Me gusta tu nombre")
else:
    print("Saludos")