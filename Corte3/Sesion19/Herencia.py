class Deportista():
    def __init__(self,nombre:str,edad:int,documento:str):
        self.__nombre=nombre
        self.__edad=edad
        self.__documento=documento

    #----------Setters------------
    def setNombre(self,nombre:str):
        self.__nombre=nombre

    def setEdad(self,edad:int):
        self.__edad=edad

    def setDocumento(self,documento:str):
        self.__documento=documento

    #----------Getters------------
    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad

    def getDocumento(self):
        return self.__documento

    #---------Sobrecarga-----------
    def presentacion(self):
        return f'{self.getNombre()} es un gran deportista'

class Futbolista(Deportista):
    def __init__(self, nombre: str, edad: int, documento: str,\
        goles:int,equipo:str):
        super().__init__(nombre, edad, documento)
        self.__goles=goles
        self.equipo=equipo

    #-------Setters----------
    def setGoles(self,goles:int):
        self.__goles=goles
    def setEquipo(self,equipo:str):
        self.equipo=equipo
    
    #--------Getters---------
    def getGoles(self):
        return self.__goles
    def getEquipo(self):
        return self.equipo
    
    #--------Metodo----------
    def anotar(self):
        return f'el jugador {self.getNombre()} ha anotado {self.getGoles()} goles'
    def presentacion(self):
        return f'{self.getNombre()} es un gran futbolista'

class Tenista(Deportista):
    def __init__(self, nombre: str, edad: int, documento: str,\
        games:int,sets:int):
        super().__init__(nombre, edad, documento)
        self.__games=games
        self.__sets=sets

    #-------Setters----------
    def setGames(self,games:int):
        self.__games=games
    def setSets(self,sets:int):
        self.__sets=sets
    
    #--------Getters---------
    def getGames(self):
        return self.__games
    def getSets(self):
        return self.__sets
    
    #--------Metodo----------
    def ace(self):
        return f'el jugador {self.getNombre()} ha ganado {self.getGames()} games'

    # def presentacion(self):
    #     return f'{self.getNombre()} es un gran tenista'

def main():
    inscrito=Futbolista('Falcao García',35,'38763284',34,'Seleccion Colombia')
    print(f'Nombre: {inscrito.getNombre()}\n',\
        f'Edad: {inscrito.getEdad()}\n',\
            f'Documento: {inscrito.getDocumento()}\n',\
                f'#Goles: {inscrito.getGoles()}\n',\
                f'Equipo: {inscrito.getEquipo()}\n')
    print(inscrito.anotar())
    print(inscrito.presentacion())

    print('\n------------------------------------')
    inscrito2=Tenista('Roger Federer',43,'897234923',4,12)
    print(f'Nombre: {inscrito2.getNombre()}\n',\
        f'Edad: {inscrito2.getEdad()}\n',\
            f'Documento: {inscrito2.getDocumento()}\n',\
                f'#Games: {inscrito2.getGames()}\n',\
                f'#sets: {inscrito2.getSets()}\n')
    print(inscrito2.ace())
    print(inscrito2.presentacion())
    print('\n------------------------------------')
    inscrito3=Deportista('Magnus Carlsen',32,'2387623')
    print(inscrito3.presentacion())

if __name__=="__main__":
    main()