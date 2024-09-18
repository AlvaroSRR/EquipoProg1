# Hacer un algoritmo que separe personas en grupos dependiendo de la edad y altura: si tiene más de 10 pero menos de 30 y mide más de 1.50, va al grupo A. Sino, va al grupo B.

try:
    edad=int(input("Por favor, ingrese su edad: "))
    altura=float(input("Por favor, ingrese su altura (en metros): "))
    
    if edad>10 and edad<30 and altura>1.50:
        print ("Usted será parte del grupo A.")
    else:
        print ("Usted será parte del grupo B.")
except ValueError:
    print ("Por favor, ingrese valores válidos. Asegúrese de ingresar números enteros para la edad y números decimales para la altura.")
