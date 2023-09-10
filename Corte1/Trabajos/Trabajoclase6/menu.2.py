print("ingrse una opcioin")
print("1. numeros divisibles por un nuemero")
print("2. multiplicacion de numeros")
print("3. serie Fibonacci")

opc = int(input("ingrse una opción:  "))
if opc == 1:
    n = int(input("ingrese un numero: "))

 if n== 0:
        print("El número es cero. No tiene divisores.")
    else:
        print("Divisores positivos de :", n)
        for i in range(1, n + 1):
            if n % i == 0:
                print(i)
elif opc == 2:
    n1 = int(input("ingrse un numero"))
    n2 = int(input("ingrse un numero"))
    R = n1*n2
    print("el producto entrer los numeros son: ", R)
elif  opc == 3:
    num_digits = int(input("Ingresa la cantidad de dígitos que deben tener los términos de la serie de Fibonacci: "))

    fib_series = [0, 1]
    while len(str(fib_series[-1])) < num_digits:
        fib_series.append(fib_series[-1] + fib_series[-2])

    print(f"Serie de Fibonacci con términos de al menos {num_digits} dígitos:")
    print(*fib_series, sep=" ")