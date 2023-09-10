print("1. circulo")
print("2. rectangulo")
print("3. triangulo")

opc = int(input("que figura usted quire realizar: "))

if opc == 1:
    r = int(input("ingrese el radio: "))
    A = r**2
    print("el area es: ", A)
elif opc == 2:
    b = int(input("ingrese la base: "))
    h = int(input("ingrse la altura: "))
    A = b*h
    print("el area es: ", A)
elif opc == 3:
    b = int(input("ingrese la base: "))
    h = int(input("ingrse la altura: "))
    A = b*h/2
    print("el area es: ", A)
else:
    print("ingrese una opcion correcta")