#función con parametros y retorno

def suma(num1,num2):
    x=num1+num2
    return x

print('Inicio del programa')
a=int(input('Ingrese un numero: '))
b=int(input('Ingrese otro numero: '))
resultado=suma(a,b)
print(resultado)
print('Fin del programa')