ingredientesBase="Mozzarella, Tomate"
tipoPizza=int(input("Ingrese nº de pizza:\n 1 - vegetariana\n 2 - no vegetariana\n Nº: "))
if tipoPizza==1:
    ingredienteCliente=int(input("Ingrese nº de ingrediente:\n 1 - Pimiento \n 2 - Toffu\n Nº: "))
    if ingredienteCliente==1:
        ingredienteCliente="Pimiento"
    elif ingredienteCliente==2:
        ingredienteCliente="Toffu"
elif tipoPizza==2:
    ingredienteCliente = int(input("Ingrese nº de ingrediente:\n 1 - Peperoní \n 2 - Jamón \n 3 - Salmón\n Nº: "))
    if ingredienteCliente == 1:
        ingredienteCliente = "Peperoni"
    elif ingredienteCliente == 2:
        ingredienteCliente = "Jamón"
    elif ingredienteCliente==3:
        ingredienteCliente="Salmón"
if tipoPizza==1:
    tipoPizza="Vegetariana"
else:
    tipoPizza="No Vegetariana"
print(f" Pizza: {tipoPizza} \n Ingredientes: {ingredientesBase}, {ingredienteCliente}")