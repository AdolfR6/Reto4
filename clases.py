class Entregable():
    # Atributo
    Entregado = False
    __Num_hyt = 0

    # Constructor

    def __init__(self, num_hyt):
        self.__Num_hyt = num_hyt

    # Metodos
    def entregar(self):
        self.Entregado = True

    def devolver(self):
        self.Entregado = False

    def isEntregado(self):
        if self.Entregado == False:
            print("No ha sido entregado")
        else:
            print("Ha sido entregado")

    def get_Num_hyt(self):
        return self.__Num_hyt

    def set_Num_hyt(self, num_hyt):
        self.__Num_hyt = num_hyt

    def __gt__(self, comparar):
        return self.__Num_hyt > comparar.__Num_hyt


class Serie(Entregable):
    # Atributos
    __Titulo = ''
    __Genero = ''
    __Creador = ''
    __Num_hyt = 3

    #Cosntructor
    def __init__(self, titulo, genero, creador, num_hyt):
        Entregable.__init__(self, num_hyt)
        self.__Creador = creador
        self.__Titulo = titulo
        self.__Genero = genero

    # Get and Set

    def get_Titulo(self):
        return self.__Titulo

    def set_Titulo(self, titulo):
        self.__Titulo = titulo

    def get_Genero(self):
        return self.__Genero

    def set_Genero(self, genero):
        self.__Genero = genero

    def get_Creador(self):
        return self.__Creador

    def set_Creador(self, creador):
        self.__Creador = creador

    # Metodos

    def __str__(self):
        prueba = self.__Titulo + ' - ' + self.__Genero + ' - ' + self.__Creador + ' - ' + str(self.get_Num_hyt())
        return prueba


class Videojuego(Entregable):
    #Atributos
    __Titulo = ''
    __Genero = ''
    __Num_hyt=10
    __Compañia=''

    #Constructor
    def __init__(self,titulo,genero,compañia,num_hyt):
        Entregable.__init__(self, num_hyt)
        self.__Compañia=compañia
        self.__Titulo = titulo
        self.__Genero = genero

    # Get and Set

    def get_Titulo(self):

        return self.__Titulo

    def set_Titulo(self,titulo):

        self.__Titulo= titulo

    def get_Genero(self):

        return self.__Genero

    def set_Genero(self,genero):

        self.__Genero= genero

    def get_Compañia(self):
        return self.__Compañia

    def set_Compañia(self, compañia):
        self.__Compañia=compañia

    #Metodos

    def __str__(self):
        prueba= self.__Titulo + ' - ' + self.__Genero + ' - ' + self.__Compañia + ' - ' + str(self.get_Num_hyt())
        return prueba
