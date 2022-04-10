from tkinter import*
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox as MessageBox

#Interfaz
raiz = Tk()
raiz.title("Practica 1 - Algoritmo de euclides y algoritmo exntentido de euclides")
raiz.geometry("800x500")
raiz.config(bg="white")

#Código propuesto en clase
#Algoritmo de Euclides
def Euclides(a, b):
    x = a
    y = b
    while y > 0:
        r = x % y
        x = y
        y = r

    return x


#Algoritmo de Euclides Extendido
def EuclidesExtendido(a, b):
    u0 = 1
    u1 = 0
    v0 = 0
    v1 = 1
    
    while b != 0:
        
        #Hacemos las correspondientes asignaciones
        q = a//b
        r = a - b * q
        u = u0 - q * u1
        v = v0 - q * v1
        
        #Actualizamos los valores
        a = b
        b = r

        #Se actualiza para la siguiente iteración
        u0 = u1
        u1 = u
        v0 = v1
        v1 = v

    return u0, v0

#def resultado(a,b,n,x): 

def Calcular():
    Alpha = valorA.get()
    Betha = valorB.get()
    Num = valorC.get()
    while True:
        if Euclides(Alpha,Num) == 1:
            break
        else:
            #dialog
            MessageBox.showerror("Error","Por favor, Ingresa parametros validos")
            break;
    
    if(Alpha > Num):
        x, y = EuclidesExtendido(Alpha, Num)
    else:
        y, x = EuclidesExtendido(Num, Alpha)

    if(x < 0):
        x = x % Num

    if(Betha > Num):
        auxiliar = Betha % Num
        mensaje1 = "C = "+ str(Alpha) + "p + "+ str(auxiliar) +" mod " + str(Num)
        mensaje2 = "P = "+ str(x) + "[C + (-"+  str(auxiliar)+  ")] mod "+ str(Num)
        salida1.config(text=mensaje1)
        salida2.config(text=mensaje2)
    else: 
        mensaje1 = "C = "+ str(Alpha) + "p + "+ str(Betha) +" mod " + str(Num)
        mensaje2 = "P = "+ str(x) + "[C + (-"+  str(Betha)+  ")] mod "+ str(Num)
        salida1.config(text=mensaje1)
        salida2.config(text=mensaje2)


#Datos
label1= Label(raiz,text="\nC R Y P T O G R A P H Y\n")
label1.grid(row=3,column=4)
label1.config(bg="#800040",fg="white",font=("Verdana",10))

label2= Label(raiz,text="\nPRÁCTICA 1\nAlgoritmo de Euclides y Algoritmo de Euclides extendido")
label2.grid(row=4,column=4)
label2.config(bg="white",font=("Verdana",8))

label3= Label(raiz,text="\nBello Muñoz Edgar Alejandro\nOrtiz Salazar Manuel Eduardo\nPérez Sereno Ricardo Erick\n")
label3.grid(row=5,column=4)
label3.config(bg="white",font=("Verdana",8))

label3= Label(raiz,text="\n 3CM17\n")
label3.grid(row=6,column=4)
label3.config(bg="white",font=("Verdana",9))


label4= Label(raiz,text="Ingresa n:")
label4.grid(row=8,column=4)
label4.config(bg="white",fg="black")
valorC = IntVar()
entrada = Entry(raiz,textvariable = valorC)
entrada.grid(row = 9, column = 4)
entrada.config(justify="center")

label5= Label(raiz,text="Ingresa a:")
label5.grid(row=10,column=4)
label5.config(bg="white",fg="black")
valorA = IntVar()
entrada = Entry(raiz,textvariable = valorA)
entrada.grid(row = 11, column = 4)
entrada.config(justify="center")

label6= Label(raiz,text="Ingresa b:")
label6.grid(row=12,column=4)
label6.config(bg="white",fg="black")
valorB = IntVar()
entrada = Entry(raiz,textvariable = valorB)
entrada.grid(row = 13, column = 4)
entrada.config(justify="center")


#Boton generar Clave
b1 = Button(raiz,text="Calcular",command = Calcular)
b1.grid(row=14,column=4)
b1.config(bg="black",fg="white")


label7= Label(raiz,text="\nEk:")
label7.grid(row=15,column=4)
label7.config(bg="white",fg="black")
salida1 = Label(raiz)
salida1.grid(row=16,column=4)
salida1.config(bg="white",fg="black")

label8= Label(raiz,text="\nDk:")
label8.grid(row=17,column=4)
label8.config(bg="white",fg="black")
salida2 = Label(raiz)
salida2.grid(row=18,column=4)
salida2.config(bg="white",fg="black")

raiz.mainloop()