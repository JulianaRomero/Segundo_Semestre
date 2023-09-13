import Fcn_ext

def main():
    a=int(input('Ingrese un numero: '))
    b=int(input('Ingrese otro numero: '))
    Fcn_ext.suma(a,b)
    print(f'Ejecutado desde {__name__}')

if __name__=="__main__":
    main()
    