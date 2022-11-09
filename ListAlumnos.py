import os
List_Alumnos=[]
def cargarAlumnos(): #cargo Alumnos
    while True: 
        nombre=input("ingrese el nombre del alumno: ")
        apellido=input("ingrese el apellido del alumno: ")
        CalCarp=int(input("ingrese la calificación de carpeta: "))
        CalTP=int(input("ingrese la calif de trab practicos: "))
        CalEv=int(input("ingrese la calif de evaluaciones: "))
        DicAlumno={"nombre":nombre, "apellido":apellido, "notCarpeta":CalCarp, "notaTP":CalTP, "NotaEv":CalEv}
        List_Alumnos.append(DicAlumno)
        resp=input("tiene otro alumno a cargar s/n: ")
        if resp=="n":
            break
def verNotasDeCArpeta(): # muestro notas de carpeta
    i=0 
    while i <= len(List_Alumnos)-1:
        mensaje="Alumno: " + List_Alumnos[i].get("nombre")+", "+ List_Alumnos[i].get("apellido")+ " Nota de carpeta: "+ str(List_Alumnos[i].get("notCarpeta"))
        print(mensaje)
        i=i+1
def verNotasDeExamen(): # muestro notas de evaluacion
    i=0
    while i <= len(List_Alumnos)-1:
        mensaje="Alumno: " + List_Alumnos[i].get("nombre")+", "+ List_Alumnos[i].get("apellido")+ " Nota de evaluación "+ str(List_Alumnos[i].get("NotaEv"))
        print(mensaje)
        i=i+1
def carpetasPresentadas(parametro):
    if parametro==True:
        # muestro carpetas no presentadas 
        i=0
        while i <= len(List_Alumnos)-1:
            if List_Alumnos[i].get("notCarpeta")==0:
                print(List_Alumnos[i].get("nombre")+" no presentado")   
            i=i+1
    else:
        # muestro carpetas presentadas
        i=0
        while i <= len(List_Alumnos)-1:
            if int(List_Alumnos[i].get("notCarpeta"))>0:
                print(List_Alumnos[i].get("nombre")+" presentado")   
            i=i+1
def cargar1alumno(nom, ape, notac=0, notatp=0, notaex=0):
    DicAlumno={"nombre":nom, "apellido":ape, "notCarpeta":notac, "notaTP":notatp, "NotaEv":notaex}
    List_Alumnos.append(DicAlumno)
    return "los datos se han añadido correctamente"
#----------------------------------------------------------------    
def cuantosSinNCarpeta(): # cuento cuantos no presentaron carpeta
    cc=0
    i=0
    while i <= len(List_Alumnos)-1:
        if int(List_Alumnos[i].get("notCarpeta"))==0:
            cc=cc+1
        i=i+1
    return cc
#-----------------------------------------------------------------
def verNotasAlumno(ape):
    i=0
    while i <= len(List_Alumnos)-1:
        if List_Alumnos[i].get("apellido")==ape:
            print("nota de carpreta: " , List_Alumnos[i].get("notCarpeta"))
            print("nota de examen: " , List_Alumnos[i].get("NotaEv"))
            print("nota de TP: " , List_Alumnos[i].get("notaTP"))
            prom=(int(List_Alumnos[i].get("notCarpeta"))+int(List_Alumnos[i].get("NotaEv"))+int(List_Alumnos[i].get("notaTP")))/3
            if prom>=7:
                print("has aprobado con " , prom)
            else: 
                print("has desaprobado con " , prom)
        i=i+1
# muestro el menu
while True:
    print("1 cargar alumnos")
    print("2 ver notas de examen")
    print("3 para ver notas de carpeta")
    print("4 ver carpetas presentadas ")
    print("5 ver carpetas no presentadas")
    print("6 cargar un alumno")
    print("7 para ver cuantos alumnos no presentaron carpeta")
    print("8 para ver las calificaciones de un alumno y el promedio")
    print("10 para salir")
    op=input("ingrese su opción: ")
    if op=="1":
        cargarAlumnos()
    elif op=="2":
        verNotasDeExamen()
    elif op =="3":
        verNotasDeCArpeta()
    elif op=="4":
        carpetasPresentadas(False)
    elif op=="5":
        carpetasPresentadas(True)
    elif op=="6":
        nombre=input("ingrese el nombre del alumno: ")
        apellido=input("ingrese el apellido del alumno: ")
        CalCarp=int(input("ingrese la calificación de carpeta: "))
        CalTP=int(input("ingrese la calif de trab practicos: "))
        CalEv=int(input("ingrese la calif de evaluaciones: "))
        cargar1alumno(nombre,apellido,CalCarp,CalTP,CalEv)
         
    elif op=="7":
        print("la cantidad de alumnos que no presento carpeta es de : ", cuantosSinNCarpeta() ) 
    elif op=="8":
        apellido=input("ingrese el aplellido del alumno: ")
        verNotasAlumno(str(apellido))
    elif op=="10":
        os.system("cls")
        break
    