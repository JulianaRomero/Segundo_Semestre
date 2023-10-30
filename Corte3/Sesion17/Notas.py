class Estudiantes():
    def __init__(self,nombre:str,codigo:int,carrera:str,
    materia:str,notas:float):     #Método Constructor
        self.__nombre=nombre
        self.__codigo=codigo
        self.__carrera=carrera
        self.__materia=materia
        self.__notas=notas

    #---------- Setters ------------
    def setNombre(self,nombre:str):
        self.__nombre=nombre
    def setCodigo(self,codigo:int):
        self.__codigo=codigo
    def setCarrera(self,carrera:str):
        self.__carrera=carrera
    def setMateria(self,materia:str):
        self.__materia=materia
    def setNotas(self,notas:float):
        if 0<notas<5:
            self.__notas=notas
    
    #---------- Getters ------------
    def getNombre(self):
        return self.__nombre
    def getCodigo(self):
        return self.__codigo
    def getCarrera(self):
        return self.__carrera
    def getMateria(self):
        return self.__materia
    def getNotas(self):
        return self.__notas

    #--------- Metodo -----------
    def __promedio(self):
        n=self.getNotas()
        return round(sum(n)/len(n),2)

    def getPromedio(self):
        average=self.__promedio()
        if average<3:
            return f'El estudiante {self.getNombre()} reprobó con {average}'
        return f'El estudiante {self.getNombre()} aprobó con {average}'

def main():
    while 1:
        universidad=[]
        nota=[]
        nombre=input('Nombre: ')
        codigo=input('Codigo: ')
        carrera=input('Carrera: ')
        materia=input('Materia: ')
        numero_notas=int(input('Cantidad de notas: '))
        x=1
        while x<numero_notas+1:
            notas=float(input(f'Nota {x}: '))
            if 0<=notas<=5:
                nota.append(notas)
                x+=1
            else:
                print('Ingreso una nota invalida')
        
        usuario=Estudiantes(nombre,codigo,carrera,materia,nota)
        universidad.append(usuario)


        print(f'\nNombre: {usuario.getNombre()}\n'\
            f'Codigo: {usuario.getCodigo()}\n'\
            f'Materia: {usuario.getMateria()}\n'\
                f'Carrera: {usuario.getCarrera()}\n'\
                    f'Nota: {usuario.getNotas()}\n'\
                        f'=> {usuario.getPromedio()}')

if __name__=="__main__":
    main()