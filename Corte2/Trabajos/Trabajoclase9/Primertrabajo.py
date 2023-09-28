from random import randint

def generar_matriz(filas, columnas):
    matriz = [[randint(1, 100) for _ in range(columnas)] for _ in range(filas)]
    return matriz

def encontrar_extremos(matriz):
    aplanada = [num for fila in matriz for num in fila]
    menor = min(aplanada)
    mayor = max(aplanada)
    return menor, mayor

def ordenar_matriz(matriz):
    aplanada = [num for fila in matriz for num in fila]
    aplanada.sort()
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_ordenada = [aplanada[i:i+columnas] for i in range(0, len(aplanada), columnas)]
    return matriz_ordenada

if __name__ == "__main__":
    filas = 5
    columnas = 10
    matriz = generar_matriz(filas, columnas)
    
    menor, mayor = encontrar_extremos(matriz)
    print(f'El número mayor de la matriz es: {mayor}')
    print(f'El número menor de la matriz es: {menor}')
    
    matriz_ordenada = ordenar_matriz(matriz)
    print(f'La matriz ordenada de menor a mayor es:')
    for fila in matriz_ordenada:
        print(fila)
