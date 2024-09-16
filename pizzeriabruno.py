ingredientesBase="mozzarella, tomate"
tipoPizza=int(input("Ingrese numero de pizza:\n 1 - vegetariana\n 2 - no vegetariana\n Nº: "))

if tipoPizza==1:
    ingredienteCliente=int(input("Ingrese numero de ingrediente:\n 1 - pimiento \n 2 - tofu\n Nº: "))
    if ingredienteCliente==1:
        ingredienteCliente="pimiento"
    elif ingredienteCliente==2:
        ingredienteCliente="tofu"
elif tipoPizza==2:
    ingredienteCliente= int(input("Ingrese numero de ingrediente:\n 1 - peperoní \n 2 - jamón \n 3 - salmón\n Nº: "))
    if ingredienteCliente==1:
        ingredienteCliente="peperoni"
    elif ingredienteCliente== 2:
        ingredienteCliente="jamón"
    elif ingredienteCliente==3:
        ingredienteCliente="salmón"
if tipoPizza==1:
    tipoPizza="vegetariana"
else:
    tipoPizza="no Vegetariana"

print ("Pizza:" ,tipoPizza, ingredientesBase, ingredienteCliente ,)