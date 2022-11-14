from tkinter import *
from math import *

ventana = Tk()
ventana.title("Calculadora Cientifica con Python")
ventana.geometry("400x370")
ventana.configure(background="ivory4")
color_boton=("gray90")

#Se crean variables en la que estaran especificado el tamaño que tengan cada boton
al=2
an=5

#Se crean las funciones que nos permitira realizaar las operaciones
def bclik(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador) # Eta parte sirve para visualizar la operacion en la pantalla
def clear():
    global operador
    operador=(" ")
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



# Se crean los botones con sus respectivos nombres. 
# Lambda nos permite simplificar las sintaxis
boton7=Button(ventana, text="7", bg=color_boton, width=an, height=al,command=lambda:bclik(7)).place(x=10, y=100)
boton8=Button(ventana, text="8", bg=color_boton, width=an, height=al,command=lambda:bclik(8)).place(x=57, y=100)
boton9=Button(ventana, text="9", bg=color_boton, width=an, height=al,command=lambda:bclik(9)).place(x=104, y=100)
botonAC=Button(ventana, text="AC", bg="orange", width=an,height=al,command=clear).place(x=151, y=100)
botondivi=Button(ventana, text="/", bg=color_boton, width=an, height=al,command=lambda:bclik("/")).place(x=198, y=100)

boton4=Button(ventana, text="4", bg=color_boton, width=an, height=al,command=lambda:bclik(4)).place(x=10, y=142)
boton5=Button(ventana, text="5", bg=color_boton, width=an, height=al,command=lambda:bclik(5)).place(x=57, y=142)
boton6=Button(ventana, text="6", bg=color_boton, width=an, height=al,command=lambda:bclik(6)).place(x=104, y=142)
botonpi=Button(ventana, text="π", bg=color_boton, width=an, height=al,command=lambda:bclik("pi")).place(x=151, y=142)
botonmultipli=Button(ventana, text="*", bg=color_boton, width=an, height=al,command=lambda:bclik("*")).place(x=198, y=142)

boton1=Button(ventana, text="1", bg=color_boton, width=an, height=al,command=lambda:bclik(1)).place(x=10, y=184)
boton2=Button(ventana, text="2", bg=color_boton, width=an, height=al,command=lambda:bclik(2)).place(x=57, y=184)
boton3=Button(ventana, text="3", bg=color_boton, width=an, height=al,command=lambda:bclik(3)).place(x=104, y=184)
botonEXP=Button(ventana, text="EXP", bg=color_boton, width=an, height=al,command=lambda:bclik("**")).place(x=151, y=184)
botonresta=Button(ventana, text="-", bg=color_boton, width=an, height=al,command=lambda:bclik("-")).place(x=198, y=184)

boton0=Button(ventana, text="0", bg=color_boton, width=an, height=al,command=lambda:bclik(0)).place(x=10, y=226)
botoncoma=Button(ventana, text=",", bg=color_boton, width=an, height=al,command=lambda:bclik(".")).place(x=57, y=226)
botonporc=Button(ventana, text="%", bg=color_boton, width=an, height=al,command=lambda:bclik("%")).place(x=104, y=226)
botonln=Button(ventana, text="ln", bg=color_boton, width=an, height=al,command=lambda:bclik("( -32)/1.8")).place(x=151, y=226)
botonsuma=Button(ventana, text="+", bg=color_boton, width=an, height=al,command=lambda:bclik("+")).place(x=198, y=226)

botonresul=Button(ventana, text="=", bg=color_boton, width=an, height=al,command=operacion).place(x=10, y=268)



salida=Entry(ventana, font=("Arial",20,"bold"), width=22,textvariable=input_text,bd=10, insertwidth=4, bg="white", justify="right").place(x=13, y=10)


ventana.mainloop()

