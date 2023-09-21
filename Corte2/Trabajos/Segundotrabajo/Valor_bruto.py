# Definir una lista de alimentos con sus tasas de IVA correspondientes
alimentos = {
    "Arroz": 0,
    "Harina de maiz": 5,
    "Pastas alimenticias": 5,
    "Cereales preparados": 19,
    "Otrso cereales": 5,
    "Pan": 0,
    "Otros productos de panadería": 0,
    "Papa": 5,
    "Yuca": 0,
    "Otros tuberculos": 0,
    "Plátanos": 0,
    "Cebolla": 0,
    "Tomate": 0,
    "Zanahoria": 0,
    "Revuelta verde": 0,
    "Otras hortalizas y legumbres frezcas": 0,
    "Frijol": 0,
    "Arveja": 0,
    "Otras hortalizas y legumbres secas": 0,
    "Hortalizas y legumbres enlatadas": 19,
    "Naranajas": 0,
    "Bananos": 0,
    "Tomate de arbol": 0,
    "Moras": 0,
    "Otras frutas secas": 0,
    "Frutas en conserva o secas": 19,
    "Res": 0,
    "Cerdo": 0,
    "Pollo": 0,
    "Carnes frias y embutidos": 5,
    "Pascado de mar,rio y elatado": 0,
    "Otros productos de mar": 19,
    "Huevos": 0,
    "Leche": 0,
    "Queso": 0,
    "Otros derivados lácteos": 19,
    "Aceites": 19,
    "Grasas": 19,
    "Panela": 0,
    "Azucar": 5,
    "Café": 5,
    "Chocolate": 5,
    "Sal": 0,
    "Otros condimentos": 19,
    "Sopas y cremas": 19,
    "Salsas y aderezos": 19,
    "Dulces y gelatinas": 10,
    "Otros abarrotes": 19,
    "Jugos": 19,
    "Gaseosas y maltas": 19,
    "Otras bebidas no alcoholicas(agua)": 0,
    "Almuerzo": 0,
    "Hamburgueza": 0,
    "Comidas rápidas calientes": 0,
    "Gastos de caferería": 0,
    "Comidas rapidas frías": 0,
}
# Función para calcular el valor bruto y el IVA de un producto dado
def calcular_valor_bruto_y_iva(nombre_producto, valor_neto, alimentos):
    if nombre_producto in alimentos:
        iva = alimentos[nombre_producto]
        valor_base = valor_neto / (1 + iva / 100)
        valor_iva = valor_neto - valor_base
        return valor_base, valor_iva
    else:
        return None
# Programa principal
while True:
    nombre_producto = input("Ingrese el nombre del producto (o 'salir' para terminar):\n ")
    if nombre_producto.lower() == "salir":
        break

    if nombre_producto in alimentos:
        valor_neto = float(input("Ingrese el valor neto del producto: "))
        valor_base, valor_iva = calcular_valor_bruto_y_iva(nombre_producto, valor_neto, alimentos)
        if valor_base is not None:
            print(f"Valor Base: {valor_base:.2f}")
            print(f"Valor del IVA: {valor_iva:.2f}")
        else:
            print("Producto no encontrado en la lista.")
    else:
        print("Producto no encontrado en la lista.")
