class Articulo:
    def __init__(self, codigo, descripcion, precio):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio

    def calcular_valor_bruto(self):
        return self.precio

    def calcular_valor_con_iva(self, tarifa_iva):
        return self.calcular_valor_bruto() * (1 + tarifa_iva)

class ArticuloIVA0(Articulo):
    def calcular_valor_con_iva(self, tarifa_iva):
        return self.precio  # No se aplica IVA

class ArticuloIVA5(Articulo):
    def calcular_valor_bruto(self):
        return self.precio / 1.05

    def calcular_valor_con_iva(self, tarifa_iva):
        return self.calcular_valor_bruto() * (1 + tarifa_iva)

class ArticuloIVA19(Articulo):
    def calcular_valor_bruto(self):
        return self.precio / 1.19

    def calcular_valor_con_iva(self, tarifa_iva):
        return self.calcular_valor_bruto() * (1 + tarifa_iva)

def cargar_base_de_datos():
    try:
        with open("Alimentos.txt", "r") as f:
            lineas = f.readlines()

        articulos = {}
        for linea in lineas:
            codigo, descripcion, tarifa_iva = linea.strip().split(",")
            articulos[codigo] = (descripcion, float(tarifa_iva))

        return articulos
    except FileNotFoundError:
        print("No se encontró el archivo 'Alimentos.txt'. La base de datos está vacía.")
        return {}

def guardar_base_de_datos(articulos):
    with open("Alimentos.txt", "w") as f:
        for codigo, (descripcion, tarifa_iva) in articulos.items():
            f.write(f"{codigo},{descripcion},{tarifa_iva}\n")

def buscar_articulo_por_codigo(codigo, base_de_datos):
    if codigo in base_de_datos:
        descripcion, tarifa_iva = base_de_datos[codigo]
        return descripcion, tarifa_iva
    else:
        return None, 0.0

def main():
    base_de_datos = cargar_base_de_datos()

    while True:
        codigo = input("Ingrese el código del artículo o escriba 'salir' para terminar:\n")
        if codigo == 'salir':
            guardar_base_de_datos(base_de_datos)
            break

        if codigo in base_de_datos:
            descripcion, tarifa_iva = buscar_articulo_por_codigo(codigo, base_de_datos)
            precio = float(input(f"Ingrese el valor que le cobraron por el artículo '{descripcion}':\n"))

            if tarifa_iva == 0:
                articulo = ArticuloIVA0(codigo, descripcion, precio)
            elif tarifa_iva == 0.05:
                articulo = ArticuloIVA5(codigo, descripcion, precio)
            elif tarifa_iva == 0.19:
                articulo = ArticuloIVA19(codigo, descripcion, precio)

            valor_bruto = articulo.calcular_valor_bruto()
            valor_con_iva = articulo.calcular_valor_con_iva(tarifa_iva)

            print(f'El artículo "{descripcion}" (Código: {codigo})')
            print(f'Precio bruto: {valor_bruto:.2f}')
            print(f'Precio con IVA ({tarifa_iva * 100}%): {valor_con_iva:.2f}')
        else:
            print('El artículo no existe en la base de datos.')

if __name__ == '__main__':
    main()
