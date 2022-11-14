from math import *
from tkinter import *

ventana = Tk()
ventana.title("Calculadora Cientifica")
ventana.geometry("448x550")
color_boton=("gray95")

#Se crean variables en la que estaran especificado el tamaño que tengan cada boton
al=3
an=11

#Se crean las funciones que nos permitira realizaar las operaciones
def bclik(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador) # Eta parte sirve para visualizar la operacion en la pantalla

def clear():
    global operador
    operador=" "
    input_text.set(operador)

def operacion():
    global operador
    try:
        opera=str(eval(operador)) # Sirve para realizar la operacion previamente visualizada en pantalla
    except:
        clear()
        opera=("ERROR")
    input_text.set(opera) # muestra el resultado

input_text=StringVar()
operador=" "

# Se crean los botones con sus resectivos nombres
# Lambda nos permite simplificar las sintaxis
botonraiz=Button(ventana, text="√", bg=color_boton, width=an,height=al,command=lambda:bclik(sqrt(""))).place(x=1, y=85)
botonexpo=Button(ventana, text="EXP", bg=color_boton, width=an,height=al,command=lambda:bclik("" "")).place(x=90, y=85)
botonlog=Button(ventana, text="log", bg=color_boton, width=an,height=al,command=lambda:bclik(log10(""))).place(x=179, y=85)
botonln=Button(ventana, text="ln", bg=color_boton, width=an,height=al,command=lambda:bclik(log(""))).place(x=268, y=85)
botonsin=Button(ventana, text="sin", bg=color_boton, width=an,height=al,command=lambda:bclik(sin(""))).place(x=357, y=85)

botoncos=Button(ventana, text="cos", bg=color_boton, width=an,height=al,command=lambda:bclik(cos(""))).place(x=1, y=143)
botontan=Button(ventana, text="tan", bg=color_boton, width=an,height=al,command=lambda:bclik(tan(""))).place(x=90, y=143)
botonarcsin=Button(ventana, text="arcsin", bg=color_boton, width=an,height=al,command=lambda:bclik(asin(""))).place(x=179, y=143)
botonarccos=Button(ventana, text="arccos", bg=color_boton, width=an,height=al,command=lambda:bclik(acos(""))).place(x=268, y=143)
botonarctan=Button(ventana, text="arctan", bg=color_boton, width=an,height=al,command=lambda:bclik(atan(""))).place(x=357, y=143)

botonsec=Button(ventana, text="sec", bg=color_boton, width=an,height=al,command=lambda:bclik("1/cos(")).place(x=1, y=201)
botoncsc=Button(ventana, text="csc", bg=color_boton, width=an,height=al,command=lambda:bclik("1/sin(")).place(x=90, y=201)
botoncot=Button(ventana, text="cot", bg=color_boton, width=an,height=al,command=lambda:bclik("1/tan(")).place(x=179, y=201)
botonpraiz=Button(ventana, text="(", bg=color_boton, width=an,height=al,command=lambda:bclik("(")).place(x=268, y=201)
botonparde=Button(ventana, text=")", bg=color_boton, width=an,height=al,command=lambda:bclik(")")).place(x=357, y=201)

boton7=Button(ventana, text="7", bg=color_boton, width=an,height=al,command=lambda:bclik(7)).place(x=1, y=259)
boton8=Button(ventana, text="8", bg=color_boton, width=an,height=al,command=lambda:bclik(8)).place(x=90, y=259)
boton9=Button(ventana, text="9", bg=color_boton, width=an,height=al,command=lambda:bclik(9)).place(x=179, y=259)
botonAC=Button(ventana, text="AC", bg=color_boton, width=an,height=al,command=clear).place(x=268, y=259)
botonDEL=Button(ventana, text="DEL", bg=color_boton, width=an,height=al,command=lambda:bclik("remover")).place(x=357, y=259)

boton4=Button(ventana, text="4", bg=color_boton, width=an,height=al,command=lambda:bclik(4)).place(x=1, y=317)
boton5=Button(ventana, text="5", bg=color_boton, width=an,height=al,command=lambda:bclik(5)).place(x=90, y=317)
boton6=Button(ventana, text="6", bg=color_boton, width=an,height=al,command=lambda:bclik(6)).place(x=179, y=317)
botonmultip=Button(ventana, text="x", bg=color_boton, width=an,height=al,command=lambda:bclik("*")).place(x=268, y=317)
botondivi=Button(ventana, text="/", bg=color_boton, width=an,height=al,command=lambda:bclik("/")).place(x=357, y=317)

boton1=Button(ventana, text="1", bg=color_boton, width=an,height=al,command=lambda:bclik(1)).place(x=1, y=375)
boton2=Button(ventana, text="2", bg=color_boton, width=an,height=al,command=lambda:bclik(2)).place(x=90, y=375)
boton3=Button(ventana, text="3", bg=color_boton, width=an,height=al,command=lambda:bclik(3)).place(x=179, y=375)
botonsuma=Button(ventana, text="+", bg=color_boton, width=an,height=al,command=lambda:bclik("+")).place(x=268, y=375)
botonresta=Button(ventana, text="-", bg=color_boton, width=an,height=al,command=lambda:bclik("-")).place(x=357, y=375)

boton0=Button(ventana, text="0", bg=color_boton, width=an,height=al,command=lambda:bclik(0)).place(x=1, y=433)
botoncoma=Button(ventana, text=",", bg=color_boton, width=an,height=al,command=lambda:bclik(".")).place(x=90, y=433)
botonpi=Button(ventana, text="π", bg=color_boton, width=an,height=al,command=lambda:bclik("pi")).place(x=179, y=433)
botonporc=Button(ventana, text="%", bg=color_boton, width=an,height=al,command=lambda:bclik("%")).place(x=268, y=433)
botonresl=Button(ventana, text="=", bg=color_boton, width=an,height=al,command=operacion).place(x=357, y=433)

botonsalir=Button(ventana, text="salir", bg=color_boton, width=an,height=al,command=quit).place(x=357, y=490)

salida=Entry(ventana, font=("Arial",20,"bold"), textvariable=input_text, width=22, bd=20, insertwidth=5, bg="powder blue", justify="right")
salida.pack()

ventana.mainloop()

