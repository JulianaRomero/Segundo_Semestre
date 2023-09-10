def verificar_letra(letra):
    vocales = "aeiouAEIOU"
    if letra.isalpha() and len(letra) == 1:
        if letra in vocales:
            return "Es una vocal."
        else:
            return "Es una consonante."
    else:
        return "No es una letra válida."

def programa_vocal_consonante():
    letra = input("Ingresa una letra del abecedario: ")
    resultado = verificar_letra(letra)
    print(resultado)

def calcular_cobro_parqueo(tiempo_minutos):
    tarifa_por_minuto = 139
    subtotal = tiempo_minutos * tarifa_por_minuto
    iva = subtotal * 0.16
    total = subtotal + iva
    total_redondeado = round(total / 50) * 50
    return total_redondeado

def programa_cobro_parqueo():
    tiempo_minutos = int(input("Ingresa el tiempo de parqueo en minutos: "))
    total_a_pagar = calcular_cobro_parqueo(tiempo_minutos)
    print(f"Total a pagar: ${total_a_pagar:.2f}")

def verificar_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Equilátero"
        elif a == b or a == c or b == c:
            return "Isósceles"
        else:
            return "Escaleno"
    else:
        return "No se puede formar un triángulo."

def programa_verificar_triangulo():
    a = float(input("Ingresa la longitud del primer lado: "))
    b = float(input("Ingresa la longitud del segundo lado: "))
    c = float(input("Ingresa la longitud del tercer lado: "))
    tipo_triangulo = verificar_triangulo(a, b, c)
    print(f"El triángulo es {tipo_triangulo}")

def main():
    while True:
        print("\nMenú de Inicio:")
        print("1. Verificar vocal o consonante")
        print("2. Calcular cobro de parqueo")
        print("3. Verificar tipo de triángulo")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            programa_vocal_consonante()
        elif opcion == "2":
            programa_cobro_parqueo()
        elif opcion == "3":
            programa_verificar_triangulo()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()
