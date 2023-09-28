def calcular_imc(peso_kg, altura_cm):
    
    # Convertir altura de centímetros a metros
    altura_m = altura_cm / 100
    imc = peso_kg / (altura_m ** 2)
    return imc

def main():
    # Datos de las personas
    personas = [
        {"nombre": "Pedro Caceres", "altura_cm": 188, "peso_kg": 97},
        {"nombre": "Maria Pérez", "altura_cm": 160, "peso_kg": 47},
        {"nombre": "Julian Dominguez", "altura_cm": 158, "peso_kg": 58},
        {"nombre": "Jessica Fuentes", "altura_cm": 170, "peso_kg": 73}
    ]

    # Calcular el IMC y mostrar la clasificación para cada persona
    for persona in personas:
        nombre = persona["nombre"]
        altura_cm = persona["altura_cm"]
        peso_kg = persona["peso_kg"]

        imc = calcular_imc(peso_kg, altura_cm)

        print(f"{nombre}:")
        print(f"   - IMC: {imc:.2f}")

        if imc <18.5:
            print("   - Clasificación: Por debajo")
        elif 18.5 <= imc < 24.9:
            print("   - Clasificación: Peso saludable")
        elif 25 <= imc < 29.9:
            print("   - Clasificación: Sobrepeso")
        elif 30 <= imc < 34.9:
            print("   - Clasificación: Obesidad grado 1")
        elif 35 <= imc < 39.9:
            print("   - Clasificación: Obesidad grado 2")
        else:
            print("   - Clasificación: Obesidad grado 3")

        print()

if __name__ == "__main__":
    main()
