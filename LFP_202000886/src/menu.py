
from carga_archivo import leerArchivoEntrada
import graphviz
import os
import webbrowser

#Inicializamos el arreglo y el id
global ArregloPeliculas
ArregloPeliculas = []
id=0


# INICIA EL PROGRAMA

# Recuadro de Datos de autor
print(
      "\n|        Lenguajes Formales y de Programación       |",
      "\n|                     Seccion: A+                   |",
      "\n|      202000886 - José Ricardo Menocal Kong        |",
      "\n")
#Termina recuadro

#INICIA EL MENU
op = 1

#SE CREA UN WHILE PARA RECORRER EL MENU UNA Y OTRA VEZ

while op != 0:

#OPCIONES MENU

    print("-------MENU PRINCIPAL--------")
    print("1 CARGAR ARCHIVO DE ENTRADA")
    print("2 GESTIONAR PELICULAS")
    print("3 FILTRADO")
    print("4 GRAFICA")
    print("5 SALIR")
    print("-----------------------")
    #Ingreso de la opcion por el usuario
    op = int(input("Elija una opcion de 1 a 5: "))

#1. CARGA DE ARCHIVOS

    if op == 1:
        #Se invoca la funcion de leerArchivoEntrada()
        print("****** CARGA DE ARCHIVOS ******\n")
        leerArchivoEntrada(ArregloPeliculas)
        print("****** ***** ** ******** ******")
        print("\nCARGA EXITOSAMENTE\n")
        print("****** ***** ** ******** ******")

#2. GESTION

    elif op == 2:
    #Se muestra el menu de GESTION
        print("****** GESTIONAR PELICULAS ******\n")
        print("1. Mostrar peliculas: ",
              "\n2. Mostrar actores: ")
        #Se ingresa la opcion deseada
        op = int(input("Eliga una opcion: "))
        print("****** ********* ********* ******\n")

    #2.1 MOSTRAR PELICULAS
        #se crea un if para que, si la opcion ingresada es igual a 1
        if op ==1:
            #se recorre el arreglo a paso i
            for i in ArregloPeliculas:
                #se invoca la funcion mostrar info()
                i.mostarinfo()
                print("****** ********* ********* ******")
    #2.2 MOSTRAR ACTORES DE LAS PELICULAS
        #se crea un if para que, si la opcion ingresada es igual a 2
        if op ==2:
            #se recorre el arreglo a paso i
            for i in ArregloPeliculas:
                #se invoca la funcion mostrar mostrarSoloPelicula()
                i.mostrarSoloPelicula()
                print("****** ********* ********* ******")      
            #se pide que ingrese el numero a visualizar de tipo INT
            id = int(input("Ingrese el numero de la pelicula: "))
            print("****** ********* ********* ******") 
            #se recorre el arreglo a paso i
            for i in ArregloPeliculas:
                #se invoca la funcion mostrar mostrarActorPorNumero()
                i.mostrarActorPorNumero(id)
        print("****** ********* ********* ******") 

#3. FILTRO

    elif op == 3:
        print("***********FILTRO***********")
        print("1 Filtrado por actor")
        print("2 Flitrado por año")
        print("3 Filtrado por genero")
        #Ingreso de opcion tipo INT
        opc = int(input("Ingrese una opcion: "))

    #3.1FILTRO POR ACTOR
        #se crea un if para que, si la opcion ingresada es igual a 1
        if opc==1:
            print("****** FILTRADO POR ACTOR ******")
            #Ingreso del dato a buscar de tipo STRING
            act = str(input("Ingrese el nombre de un actor: "))
            print("****** ********* ********* ******")
            #se recorre el arreglo a paso i
            for i in ArregloPeliculas:
                #se invoca la funcion mostrar mostrarPorActor(act)
                i.mostrarPorActor(act)
            print("****** ********* ********* ******")

    #3.2 FILTRO POR AÑO
        #se crea un if para que, si la opcion ingresada es igual a 2
        elif opc==2:
            print("****** FILTRADO POR AÑO ******")
            #Ingreso del dato a buscar
            año = input("Ingrese el año: ")
            print("****** ********* ********* ******")
            #se recorre el arreglo a paso i
            for i in ArregloPeliculas:
                #se invoca la funcion mostrar mostrarPorActor(act)
                i.mostrarPorAño(año)
            print("****** ********* ********* ******")
            
    #3.3 FILTOR POR GENERO
        #se crea un if para que, si la opcion ingresada es igual a 3
        elif opc==3:
            print("****** FILTRADO POR GENERO ******")
            #Ingreso del dato a buscar de tipo STRING
            genero = str(input("Ingrese el genero: "))
            print("****** ********* ********* ******")
            #se recorre el arreglo a paso i
            for i in ArregloPeliculas:
                #se invoca la funcion mostrar mostrarPorGenero(genero)
                i.mostrarPorGenero(genero)
            print("****** ********* ********* ******")

#4. GRAFICO                
    elif op == 4:  
        print("---------GRAFICA---------")
        s = graphviz.Digraph('structs', filename='structs_revisited.gv',node_attr={'shape': 'record'})
        for i in ArregloPeliculas:
            s.node('struct1', '{{<peli> {i.nombre} |{{i.Año}}|{i.genero}}}')
            s.node('struct2', '<f0> {i.actores}')
            s.edges([('struct1:peli', 'struct2:f0')])
        print(s.source)
        r=open("C:\LFP\LFP_202000886\src\Reportes\Report.dot","w")
        r.write(s.source)
        r.close()
        os.system("dot -Tpng Reportes/Report.dot -o Reportes/Report.png")
        webbrowser.open_new_tab("C:\LFP\LFP_202000886\src\Reportes\Report.png")
        print("****** ********* ********* ******")  
        print("SE CREO LA GRAFICA EXITOSAMENTE")
        print("****** ********* ********* ******")      
    elif op == 5:

#5. SALIDA
        print("****** ********* ********* ******") 
        print("|  GRACIAS POR USAR EL PROGRAMA |")
        print("****** ********* ********* ******") 
        break