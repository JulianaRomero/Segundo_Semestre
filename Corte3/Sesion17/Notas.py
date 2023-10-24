

class Estudiantes():
    def __init__(self):     #Método Constructor
        self.__nombre=None
        self.__codigo=None
        self.__carrera=None
        self.__materia=None
        self.__notas=None

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

def main():
    usuario=Estudiantes()
    usuario.setNombre("Juliana")
    usuario.setCodigo("Juliana")
    usuario.setMateria("Juliana")
    usuario.setCarrera("Juliana")
    usuario.setNotas("Juliana")
    pass

if __name__=="__main__":
    main()