import random  # Agrega esta línea para importar el módulo random

def generar_lista():
    return [random.randint(1, 50) for _ in range(10)]

def encontrar_mayor(lista):
    mayor = lista[0]
    for num in lista[1:]:
        if num > mayor:
            mayor = num
    return mayor  # Cambié el print a un return para obtener el valor máximo

if __name__ == "__main__":
    lista_generada = generar_lista()
    print(lista_generada)
    
    maximo = encontrar_mayor(lista_generada)
    print(f'El número mayor en la lista es: {maximo}')

