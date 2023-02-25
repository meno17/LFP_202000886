class Peliculas:
    #CONSTRUCTOR
    def __init__(self,num, nombre, actores, año, genero):
        self.num = num 
        self.nombre = nombre
        self.actores = actores
        self.año = año
        self.genero = genero
    
#FUNCIONES
    #FUNCION DE MOSTRAR TODAS LAS PELICULAS
    def mostarinfo(self):
        print("ID:",self.num,
              "\nPELICULA: ",
              self.nombre, 
              "\nACTORES: ", 
              self.actores,
              "\nAÑO ESTRENO: "
              , self.año,
              "\nGENERO: ",
                self.genero)
    #FUNCION DE MOSTRAR PELICULA POR NUMERO 
    def mostrarActorPorNumero(self,num):
        if num == self.num:
            print("ID:",self.num,
              "\nPELICULA: ",
              self.nombre, 
              "\nACTORES: ", 
              self.actores,
              "\nAÑO ESTRENO: "
              , self.año,
              "\nGENERO: ",
                self.genero)
        

    #FUNCION DE MOSTRAR SOLO PELICULAS CON SU ID            
    def mostrarSoloPelicula(self):
    
        print("ID:",self.num,"PELICULA: ",self.nombre)

    #FUNCION DE FILTRAR PELICULAS POR ACTORES
    def mostrarPorActor(self,dato):
        #se crea if para comparar si el dato es en self.actores
        if dato in self.actores:
            #Devuelve los datos de la pelicula que contiene self.actores
            print("\nID:",self.num,
              "\nPELICULA: ",
              self.nombre, 
              "\nACTORES: ", 
              self.actores,
              "\nAÑO ESTRENO: "
              , self.año,
              "\nGENERO: ",
                self.genero)

    #FUNCION DE FILTRAR PELICULAS POR AÑO
    def mostrarPorAño(self,dato):
        #Devuelve los datos de la pelicula que contiene self.año
        if dato in self.año:
            print("\nID:",self.num,
              "\nPELICULA: ",
              self.nombre, 
              "\nACTORES: ", 
              self.actores,
              "\nAÑO ESTRENO: "
              , self.año,
              "\nGENERO: ",
                self.genero)

    #FUNCION DE FILTRAR PELICULAS POR GENERO        
    def mostrarPorGenero(self,dato):
        #Devuelve los datos de la pelicula que contiene self.genero
        if dato in self.genero:
            print("\nID:",self.num,
              "\nPELICULA: ",
              self.nombre, 
              "\nACTORES: ", 
              self.actores,
              "\nAÑO ESTRENO: "
              , self.año,
              "\nGENERO:",
                self.genero,)
            
        