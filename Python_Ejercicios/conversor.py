print("Bienvenido al conversor de millas a kilometros")

#para pedir datos al usuario se utiliza una funcion inputi() esto lo que hace que espera a que el usuario escriba un valor es como scanner en java
print("Escribre un numero en millas:")
millas = input()

#1 milla = 1.609 kms
#se pone de esta manera por que al convertir millas a km te da un error por input es de tipo string 
#y no se puede multiplicar con un float y reasignamor valor a la variable millas de tipo flaoat para que se pueda hacer la conversion
millas = float(millas)
kilometros = millas * 1.609
print("Millas ingresadas:", millas)
print("Kilometros:", kilometros)