#ENUNCIADO DE PROGRAMACION
#Desarrolla un programa que solicite al usuario que ingrese su edad y determine en que categoría se encuentra según los siguientes criterios:
#	•	Menor de 13 años: El usuario es un "Niño".
#   •	Entre 13 y 19 años (inclusive): El usuario es un "Adolescente".
#	•	Entre 20 y 64 años (inclusive): El usuario es un "Adulto".
#	•	65 años o más: El usuario es un "Anciano".
#El programa debe imprimir el resultado correspondiente a la categoría del usuario basado en su edad.

edad=int(input("Ingrese su edad: "))
if edad<13 :
    print("El usuario es un niño")
elif edad>=13 and edad<=19 :
    print("El usuario es un adolescente")
elif edad>=20 and edad<=64 :
    print("El usuario es un adulto")
else :
    print("El usuario es un Anciano")
