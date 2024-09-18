edad = int(input("Ingrese su edad: "))
if edad < 13:
    categoria = "Niño"
elif 13 <= edad <= 19:
    categoria = "Adolescente"
elif 20 <= edad <= 64:
    categoria = "Adulto"
else:
    categoria = "Anciano"
print(f"Usted es un {categoria}.")
