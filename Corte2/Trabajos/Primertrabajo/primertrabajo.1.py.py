import random

def generar_lista():
    return [random.randint(1, 50) for _ in range(10)]

def encontrar_mayor(lista):
    mayor = lista[0]
    for num in lista[1:]:
        if num > mayor:
            mayor = num
        print(mayor)

if __name__ == "__main__":
    lista_generada = generar_lista()
    print(lista_generada)
    encontrar_mayor(lista_generada)
