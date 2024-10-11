print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
print("▬▬▬▬▬ BIENVENIDO ▬▬▬▬▬")
print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

print("Introduce tu nombre:")
nombre = input()

manzanas = 20

print("Hola,", nombre, "Gracias por visitarnos actualmente tenemos", manzanas, "manzanas disponibles, cada una por un precio de 5 euros.")

print("Cuantas manzanas quieres comprar:")
num_manzanas = input()

num_manzanas = int(num_manzanas)
precio = num_manzanas * 5

print("Gracias,", nombre, "por comprar nuestras manzanas, has comprado,", num_manzanas, "manzanas a un precio de:", precio)

manzanas_sobrantes = manzanas - num_manzanas

print("Nos queda un total de:", manzanas_sobrantes, "manzanas a la venta.")