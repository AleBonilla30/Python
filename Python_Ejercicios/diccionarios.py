#estos se pueden ver como una lista con llaves es como los arrays en java
persona = {"nombre": "Alejandra", "edad": 32, "apellido": "Gonzalez"}


persona["apellido"] = "Bonilla"
print(persona)

#estos datos son modificables pero no se acumulan en la variable
#esto quiere decir que lo modifica pero que no queda ningun registro de el otro
print(persona.keys())#este te imprimer lo de nombre, apellido etc
print(persona.values())#este te imprime los valores que has agregado