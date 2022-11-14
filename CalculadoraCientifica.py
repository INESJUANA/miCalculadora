from math import *
from tkinter import *

ventana = Tk()
ventana.title("Calculadora Cientifica con Python")
ventana.geometry("448x550")

#Se crean variables en la que estaran especificado el tamaño que tengan cada boton
al=3
an=11

#Se crean las funciones que nos permitira realizaar las operaciones
def bclik(num):
    global operador
    operador=operador+str(num)
    a.set(operador)

def clear():
    global operador
    operador=" "
    a.set(operador)

def operacion():
    global operador
    try:
        opera=eval(operador)
    except:
        clear()
        opera=("Error")
    a.set(opera)

a=StringVar()
operador=" "

# Se crean los botones con sus resectivos nombres
botonraiz=Button(ventana, text="√", width=an,height=al,command=lambda:bclik(sqrt("")))
botonraiz.place(x=1, y=85)
botonexpo=Button(ventana, text="EXP", width=an,height=al,command=lambda:bclik("" ""))
botonexpo.place(x=90, y=85)
botonlog=Button(ventana, text="log", width=an,height=al,command=lambda:bclik(log10("")))
botonlog.place(x=179, y=85)
botonln=Button(ventana, text="ln", width=an,height=al,command=lambda:bclik(log("")))
botonln.place(x=268, y=85)
botonsin=Button(ventana, text="sin", width=an,height=al,command=lambda:bclik(sin("")))
botonsin.place(x=357, y=85)

botoncos=Button(ventana, text="cos", width=an,height=al,command=lambda:bclik(cos("")))
botoncos.place(x=1, y=143)
botontan=Button(ventana, text="tan", width=an,height=al,command=lambda:bclik(tan("")))
botontan.place(x=90, y=143)
botonarcsin=Button(ventana, text="arcsin", width=an,height=al,command=lambda:bclik(asin("")))
botonarcsin.place(x=179, y=143)
botonarccos=Button(ventana, text="arccos", width=an,height=al,command=lambda:bclik(acos("")))
botonarccos.place(x=268, y=143)
botonarctan=Button(ventana, text="arctan", width=an,height=al,command=lambda:bclik(atan("")))
botonarctan.place(x=357, y=143)

botonsec=Button(ventana, text="sec", width=an,height=al,command=lambda:bclik("1/cos("))
botonsec.place(x=1, y=201)
botoncsc=Button(ventana, text="csc", width=an,height=al,command=lambda:bclik("1/sin("))
botoncsc.place(x=90, y=201)
botoncot=Button(ventana, text="cot", width=an,height=al,command=lambda:bclik("1/tan("))
botoncot.place(x=179, y=201)
botonpraiz=Button(ventana, text="(", width=an,height=al,command=lambda:bclik("("))
botonpraiz.place(x=268, y=201)
botonparde=Button(ventana, text=")", width=an,height=al,command=lambda:bclik(")"))
botonparde.place(x=357, y=201)

boton7=Button(ventana, text="7", width=an,height=al,command=lambda:bclik(7))
boton7.place(x=1, y=259)
boton8=Button(ventana, text="8", width=an,height=al,command=lambda:bclik(8))
boton8.place(x=90, y=259)
boton9=Button(ventana, text="9", width=an,height=al,command=lambda:bclik(9))
boton9.place(x=179, y=259)
botonAC=Button(ventana, text="AC", width=an,height=al,command=clear)
botonAC.place(x=268, y=259)
botonDEL=Button(ventana, text="DEL", width=an,height=al,command=lambda:bclik("remover"))
botonDEL.place(x=357, y=259)

boton4=Button(ventana, text="4", width=an,height=al,command=lambda:bclik(4))
boton4.place(x=1, y=317)
boton5=Button(ventana, text="5", width=an,height=al,command=lambda:bclik(5))
boton5.place(x=90, y=317)
boton6=Button(ventana, text="6", width=an,height=al,command=lambda:bclik(6))
boton6.place(x=179, y=317)
botonmultip=Button(ventana, text="x", width=an,height=al,command=lambda:bclik("*"))
botonmultip.place(x=268, y=317)
botondivi=Button(ventana, text="/", width=an,height=al,command=lambda:bclik("/"))
botondivi.place(x=357, y=317)

boton1=Button(ventana, text="1", width=an,height=al,command=lambda:bclik(1))
boton1.place(x=1, y=375)
boton2=Button(ventana, text="2", width=an,height=al,command=lambda:bclik(2))
boton2.place(x=90, y=375)
boton3=Button(ventana, text="3", width=an,height=al,command=lambda:bclik(3))
boton3.place(x=179, y=375)
botonsuma=Button(ventana, text="+", width=an,height=al,command=lambda:bclik("+"))
botonsuma.place(x=268, y=375)
botonresta=Button(ventana, text="-", width=an,height=al,command=lambda:bclik("-"))
botonresta.place(x=357, y=375)

boton0=Button(ventana, text="0", width=an,height=al,command=lambda:bclik(0))
boton0.place(x=1, y=433)
botoncoma=Button(ventana, text=",", width=an,height=al,command=lambda:bclik("."))
botoncoma.place(x=90, y=433)
botonpi=Button(ventana, text="π", width=an,height=al,command=lambda:bclik("pi"))
botonpi.place(x=179, y=433)
botonporc=Button(ventana, text="%", width=an,height=al,command=lambda:bclik("%"))
botonporc.place(x=268, y=433)
botonresl=Button(ventana, text="=", width=an,height=al,command=operador)
botonresl.place(x=357, y=433)

botonsalir=Button(ventana, text="salir", width=an,height=al,command=quit)
botonsalir.place(x=357, y=490)

salida=Entry(ventana, font=("Arial",20,"bold"), textvariable=a, width=22, bd=20, insertwidth=5, bg="powder blue", justify="right")
salida.pack()

ventana.mainloop()

