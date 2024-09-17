#el servicio de ferrocarril, necesita un programa que les ayude a organizar las cargas de sus trenes para lo cual solicita a cada cargamentos los siguientes datos: 
# los km a los que se encuentra el destino, la cantidad de toneladas, y a nombre de quien es el envio. Con los datos solicitados y sabiendo que cada vagon tiene una capacidad de 100 toneladas, calcule la cantidad de vagones de carga necesitarios por carga y el costo del envio, sabiendo que el costo por vagon es de $5000 para menos de 200 km y de $10000 a partir de 200 km y definir el tipo de locomotora, tipo A hasta 50 vagones, tipo B hasta 250 vagones y tipo C para mas de 250 vagones. Al finalizar debe imprimir el comprobante con los datos ingresados y calculados.
CAPACIDADXVAGON=100
COSTO_VAGON1=5000
COSTOVAGON2=10000
Km_recorrido=float(input("Ingrese los km a los que se encuentra el destino: "))
cantidad_toneladas=float(input("Ingrese cantidad de toneladas de la carga: "))
receptor=str(input("Ingrese Nombre y Apellido del receptor de la carga: "))
cantidad_vagones_necesarios=cantidad_toneladas/CAPACIDADXVAGON
if Km_recorrido<200:
    costo_envio=cantidad_vagones_necesarios*COSTO_VAGON1
else:
    costo_envio=cantidad_vagones_necesarios*COSTOVAGON2
if cantidad_vagones_necesarios<=50:
    tipo_locomotora="A"
elif cantidad_vagones_necesarios<=250:
    tipo_locomotora="B"
else:
    tipo_locomotora="C"

print(f"Km del recorrido:{Km_recorrido}km.\nCantidad toneladas: {cantidad_toneladas}.\nReceptor del cargamento: {receptor}\nCantidad de vagones necesarios: {cantidad_vagones_necesarios}\nCosto del envio: {costo_envio}\nTipo de locomotora: {tipo_locomotora}")


