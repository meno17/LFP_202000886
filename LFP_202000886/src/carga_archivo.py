
#importaciones
from Class import Peliculas

#FUNCION LEER ARCHIVO   
def leerArchivoEntrada(lista):
#ABRIR ARCHIVO
    #Le solicita al usuario la ruta para leer el archivo
    ruta = input("Ingrese la ruta ('C:\...) para leer el archivo .lfp: ")
    #La variable archivo es igual a la ruta del archivo a abrir
    archivo = open(ruta, 'r')
    #LEER ARCHIVO LINERA POR LINEA
    lineas = archivo.readlines()
    #CERRAR ARCHIVO
    archivo.close()
    #Declaramos Datonum y lo inicializamos
    Datonum=0
    #Creamos un ciclo for para recorrer las lineas del archivo
    for i in lineas:
        #declaramos que las iteraciones estaran separadas por ";"
        i = i.split(";")
        #Declaramos la variable count y la inicializamos 
        count = 1
        #Declaramos la variable Datonum +=1 para que 
        # se incremente en uno
        Datonum +=1
        #Inicializamos las variables con una dato valido
        DatoNombre = None
        DatoActores= None
        DatoAño = None
        DatoGenero = None
        #creamos un ciclo for para recorrer las columnas de las lineas
        for j in i:
        #creamos if y elif para asignarle las...
        #...columnas a las variables de los datos
            if count == 1:
                DatoNombre = j
            elif count == 2:
                j = j.split(",")
                DatoActores = j
            elif count == 3:
                DatoAño = j
            elif count == 4:
                DatoGenero = j
            #incrementa el contador
            count += 1
        #Declaramos la variable y decimos que sus datos ...
        #...seran los datos de nuestro constructor
        peli = Peliculas(Datonum,DatoNombre, DatoActores, DatoAño, DatoGenero)
        #Agregamos los datos a la lista
        lista.append(peli)

