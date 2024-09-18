nombre = input("Ingrese su nombre: ")
try:
    sexo = input("Ingrese su sexo(F o M): ").upper()
    if sexo!="F"and sexo!="M":
        raise ValueError("error")
    if sexo=="F":
        if nombre[0]>"A" and nombre[0]<="m":
            print("pertenece al grupo A")
        else:
            print("pertenece al grupo B")
    else:
        if sexo=="M":
            if nombre[0]>"n" and nombre[0]<="z":
                print("pertenece al grupo A")
            else:
                print("pertenece al grupo B")
finally:()