import os
#---------- por aca van las funciones ----------
def sumar():
    numero1 = int(input("ingrese el primer numero: "))
    numero2 = int(input("ingrese el segundo numero: "))
    return (numero1 + numero2)
def restar():
    numero1 = int(input("ingrese el primer numero: "))
    numero2 = int(input("ingrese el segundo numero: "))
    return (numero1 - numero2)
def multiplicar():
    numero1 = int(input("ingrese el primer numero: "))
    numero2 = int(input("ingrese el segundo numero: "))
    return (numero1 * numero2)
def dividir():
    numero1 = int(input("ingrese el primer numero: "))
    numero2 = int(input("ingrese el segundo numero: "))
    return (numero1 / numero2)

#---------- funcion para el menu ----------
def menu():
    os.system("cls")
    print(" + para Sumar")    
    print(" - para Restar")
    print(" * para Multiplicar")
    print(" / para Dividir")
    print(" s para Salir")


#----------- funcion principal ------------
def main():
    menu()
    op=input("Ingrese una opcion ")
    while op != "s":
        if op=="+":
            print("El resultado de la suma es: ", sumar())
        elif op=="-":
            print("El resultado de la resta es: ", restar())
        elif op=="*":
            print("El resultado de la multiplicacion es: ", multiplicar())
        elif op=="/":
            print("El resultado de la division es: ", dividir())
        else:
            print(" opcion no valida")
        input("presione una tecla para continuar... ")
        menu()
        op=input("Ingrese una opcion ")

#------------ aca empieza el programa -----------
main()
