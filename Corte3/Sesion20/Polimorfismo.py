class Ciudadano():
    def __init__(self,idioma:str,nombre:str):
        self.__idioma=idioma
        self.__nombre=nombre
    
    def setIdioma(self,idioma:str):
        self.__idioma=idioma
    
    def setNombre(self,nombre:str):
        self.__nombre=nombre

    def getIdioma(self):
        return self.__idioma
    
    def getNombre(self):
        return self.__nombre
    
    # -------- SobreCarga------------
    def saludo(self):
        return f'Quoi de beau!'

class Colombiano(Ciudadano):
    def __init__(self, idioma: str, nombre: str,cc:str):
        super().__init__(idioma, nombre)
        self.__cc=cc
    
    def setCC(self,cc:str):
        self.__cc=cc
    
    def getCC(self):
        return self.__cc

    # -------- SobreCarga -----------
    def saludo(self):
        return f'Qiubo Parce!'

class Ingles(Ciudadano):
    def __init__(self, idioma: str, nombre: str,id:str):
        super().__init__(idioma, nombre)        
        self.__id=id
    
    def setId(self,id:str):
        self.__id=id
    
    def getId(self):
        return self.__id
    
    #---------SobreCarga----------
    def saludo(self):
        return f'Hello my Friend!'

class Chino(Ciudadano):
    def __init__(self, idioma: str, nombre: str,sfz:str):
        super().__init__(idioma, nombre)
        self.__sfz=sfz
    
    def setSfz(self,sfz:str):
        self.__sfz=sfz
    
    def getSfz(self):
        return self.__sfz
    
    #---------SobreCarga-------
    def saludo(self):
        return f'你好，你干嘛呀！'

def darSaludo(objeto):
    return objeto.saludo()

def main():
    ciudadano1=Ciudadano('Frances','Carla Bruni')
    ciudadano2=Colombiano('Español','Radamel García','272368493')
    ciudadano3=Ingles('Ingles','David Beckham','AS2134')
    ciudadano4=Chino('Mandarín','成龙','CH2353534')

    ciudadanos=[ciudadano1,ciudadano2,ciudadano3,ciudadano4]
    print('-----------Presentación-------------')
    for persona in ciudadanos:
        print(f'Ciudadano: {persona.getNombre()}, idioma:{persona.getIdioma()}')
        print(f'{persona.getNombre()} dice: '+ darSaludo(persona)+'\n')
    
    
        

if __name__=="__main__":
    main()