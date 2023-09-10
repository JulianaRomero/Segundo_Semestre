import math as m

a = int(input("ingrese un numero: "))
b = int(input("ingrese un numero: "))
c = int(input("ingrese un numero: "))

x1 = (-b + m.sqrt((b**2)-4*a*c))/(2*a)
x2 = (-b - m.sqrt((b**2)-4*a*c))/(2*a)

print("la solucion uno es: ", x1)
print("la solucion uno es: ", x2)