class Ciudadano:
    def __init__(self):
        self.__nombre = None
        self.__cedula = None
        self.__edad = None

#----------------------setters------------------
    def setNombre(self, nombre: str):
        self.__nombre = nombre

    def setCedula(self, cedula):
        if 8 <= len(str(cedula)) <= 10:
            self.__cedula = cedula
        else:
            print("La cédula debe tener entre 8 y 10 dígitos.")

    def setEdad(self, edad: int):
        if edad > 0:
            self.__edad = edad
        else:
            print('La edad debe ser un número mayor a 0 y positivo.')
#---------------------Getters----------------
    def getNombre(self):
        return self.__nombre

    def getCedula(self):
        return self.__cedula

    def getEdad(self):
        return self.__edad

    def esMayorDeEdad(self):
        if self.__edad >= 18:
            print('Usted es mayor de edad')
        else:
            print('Usted es menor de edad')

def mostrar():
    usuarios = []
    while True:
        x= Ciudadano()
        x.setNombre(input('Ingrese su nombre:\n'))
        x.setCedula(int(input('Ingrese su número de cédula:\n')))
        x.setEdad(int(input('Ingrese su edad:\n')))
        x.esMayorDeEdad()
        usuarios.append(x)

        print(f'Nombre: {x.getNombre()}\nCédula: {x.getCedula()}\nEdad: {x.getEdad()}\n')


if __name__ == '__main__':
    mostrar()
