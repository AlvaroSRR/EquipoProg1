distanciaKM=int(input("distancia en km: "))
toneladas=float(input("Toneladas: "))
nombre=input("Envio a nombre de: ")
vagones= float(toneladas/100)
if vagones%2==0:
    vagones=int(vagones)
else:
    vagones=int(vagones)+1

if distanciaKM < 200:
    costo= float(vagones*5000)
elif distanciaKM >= 200:
    costo= float(vagones*10000)
if vagones<=50:
    locomotora = "Tipo A"
elif vagones>50 and vagones<=250:
    locomotora = "Tipo B"
elif vagones>250:
    locomotora= "Tipo C"

print(f"Envio a nombre de: {nombre}\nToneladas: {toneladas} Tn\nDistancia: {distanciaKM} KM")
print(f"Vagones necesarios: {vagones}\n Costo del envio: ${costo}\n Locomotora: {locomotora}")