class Ciudadano:
    def __init__(self, nombre, cedula, edad):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__edad = edad

    def getNombre(self):
        return self.__nombre

    def getCedula(self):
        return self.__cedula

    def getEdad(self):
        return self.__edad

    def esMayorDeEdad(self):
        if self.__edad >= 18:
            print('¡Eres mayor de edad!')
        else:
            print('Eres menor de edad.')

class Profesionista(Ciudadano):
    def __init__(self, nombre, cedula, edad, especialidad, experiencia):
        super().__init__(nombre, cedula, edad)
        self.__especialidad = especialidad
        self.__experiencia = experiencia

    def getEspecialidad(self):
        return self.__especialidad

    def getExperiencia(self):
        return self.__experiencia

    def presentar(self):
        print(f'Soy un/una profesional en {self.getEspecialidad()} y tengo {self.getExperiencia()} años de experiencia.')

class Medica(Ciudadano):
    def __init__(self, nombre, cedula, edad, especialidad, num_colegiado):
        super().__init__(nombre, cedula, edad)
        self.__especialidad = especialidad
        self.__num_colegiado = num_colegiado

    def getEspecialidad(self):
        return self.__especialidad

    def getNumColegiado(self):
        return self.__num_colegiado

    def atender_paciente(self):
        print(f'¡Estoy atendiendo a un paciente como médico/médica, colegiado/colegiada con el número {self.getNumColegiado()}, especializado/especializada en {self.getEspecialidad()}!')

class Ingeniera(Ciudadano):
    def __init__(self, nombre, cedula, edad, especialidad, proyectos_realizados):
        super().__init__(nombre, cedula, edad)
        self.__especialidad = especialidad
        self.__proyectos_realizados = proyectos_realizados

    def getEspecialidad(self):
        return self.__especialidad

    def getProyectosRealizados(self):
        return self.__proyectos_realizados

    def presentar(self):
        print(f'Soy un/una ingeniero/ingeniera especializado/especializada en {self.getEspecialidad()} y he realizado los siguientes proyectos: {", ".join(self.getProyectosRealizados())}.')

if __name__ == '__main__':
    while True:
        nombre = input('Dinos tu nombre:\n')
        cedula = int(input('Ingresa tu número de cédula:\n'))
        edad = int(input('Cuéntanos tu edad:\n'))

        print('Elige una profesión:')
        print('1. Profesionista')
        print('2. Médica')
        print('3. Ingeniera')
        opcion = input('Selecciona el número de profesión (1/2/3): ')

        if opcion == '1':
            especialidad = input('Especialidad: ')
            experiencia = input('Años de experiencia: ')
            profesionista = Profesionista(nombre, cedula, edad, especialidad, experiencia)
            profesionista.presentar()
        elif opcion == '2':
            especialidad = input('Especialidad: ')
            num_colegiado = input('Número de colegiado: ')
            medica = Medica(nombre, cedula, edad, especialidad, num_colegiado)
            medica.atender_paciente()
        elif opcion == '3':
            especialidad = input('Especialidad: ')
            proyectos_realizados = input('Proyectos realizados (separados por comas): ').split(',')
            ingeniera = Ingeniera(nombre, cedula, edad, especialidad, proyectos_realizados)
            ingeniera.presentar()
        else:
            print('Opción no válida. Por favor, elige una profesión válida.')
            
            
            
            
            
            
            
            
