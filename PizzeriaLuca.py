ingredientes_base = "Mozzarella, Tomate"
tipo_pizza = int(input("Ingrese el tipo de pizza que desea:\n1: Vegetariana\n2: No Vegetariana\n"))
if tipo_pizza == 1:
    ingrediente_cliente = int(input("Ingrese el ingrediente a su gusto:\n1: Pimiento\n2: Tofu\n"))
    if ingrediente_cliente == 1:
        ingrediente_cliente = "Pimiento"
    elif ingrediente_cliente == 2:
        ingrediente_cliente = "Tofu"
    else:
        ingrediente_cliente = "Opción no válida"
    tipo_pizza = "Vegetariana"
elif tipo_pizza == 2:
    ingrediente_cliente = int(input("Ingrese el ingrediente a su gusto:\n1: Pepperoni\n2: Jamón\n3: Salmón\n"))
    if ingrediente_cliente == 1:
        ingrediente_cliente = "Pepperoni"
    elif ingrediente_cliente == 2:
        ingrediente_cliente = "Jamón"
    elif ingrediente_cliente == 3:
        ingrediente_cliente = "Salmón"
    else:
        ingrediente_cliente = "Opción no válida"
    tipo_pizza = "No Vegetariana"
else:
    print("Opción de tipo de pizza no válida.")
    tipo_pizza = "No especificado"
    ingrediente_cliente = "No especificado"
print(f"Pizza: {tipo_pizza}\nIngredientes: {ingredientes_base}, {ingrediente_cliente}")