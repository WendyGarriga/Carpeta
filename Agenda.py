import tkinter as tk
import sys
class Agenda:
    def __init__(self):
        self.nombre=[]
        self.telefono=[]
        self.mail=[]
        self.ventana1=tk.Tk()
        self.boton1=tk.Button(self.ventana1, text="Agregar Contactos",command=self.contactos)
        self.boton1.grid(column=0,row=0)
        self.boton2=tk.Button(self.ventana1,text="Listado",command=self.listado)
        self.boton2.grid(column=0,row=1)
        self.boton3=tk.Button(self.ventana1,text="Consultar Contacto",command=self.consulta)
        self.boton3.grid(column=0,row=2)
        self.boton4=tk.Button(self.ventana1,text="Modificar",command=self.modificar)
        self.boton4.grid(column=0,row=3)
        self.boton5=tk.Button(self.ventana1,text="Salir",command=self.salir)
        self.boton5.grid(column=0,row=4)
        self.ventana1.mainloop()
    def contactos(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1,text="Ingrese Contactos")
        self.label1.grid(column=0,row=0)
        self.dato1=tk.StringVar(self.ventana1)
        self.label2=tk.Label(self.ventana1,text="Ingrese Nombre: ")
        self.label2.grid(column=0,row=1)
        self.entry1=tk.Entry(self.ventana1,width= 10,textvariable=self.dato1)
        self.entry1.grid(column=0,row=2)
        self.dato2=tk.StringVar(self.ventana1)
        self.label3=tk.Label(self.ventana1,text="Agregar Telefono: ")
        self.label3.grid(column=0,row=3)
        self.entry2=tk.Entry(self.ventana1,width=10,textvariable=self.dato2)
        self.entry2.grid(column=0,row=4)
        self.dato3=tk.StringVar(self.ventana1)
        self.label4=tk.Label(self.ventana1,text="Agregar Mail: ")
        self.label4.grid(column=0,row=5)
        self.entry3=tk.Entry(self.ventana1,width=10,textvariable=self.dato3)
        self.entry3.grid(column=0,row=6)
        self.boton6=tk.Button(self.ventana1,text="Guardar",command=self.guardar)
        self.boton6.grid(column=0,row=7)
    def guardar(self):
        nombres=self.dato1.get()
        telefonos=self.dato2.get()
        mails=self.dato3.get()
        self.nombre.append(nombres)
        self.telefono.append(telefonos)
        self.mail.append(mails)
    def listado(self):
        self.ventana1=tk.Tk()
        self.label5=tk.Label(self.ventana1,text="Nombre de contacto: ")
        self.label5.grid(column=0,row=0)
        self.label6=tk.Label(self.ventana1,text="Telefono de contacto:")
        self.label6.grid(column=1,row=0)
        self.label7=tk.Label(self.ventana1,text="Mail de contacto: ")
        self.label7.grid(column=2,row=0)
        for x in range(len (self.nombre)):
            self.labe4=tk.Label(self.ventana1,text=self.nombre[x])
            self.labe4.grid(column=0,row=x+1)
            self.labe5=tk.Label(self.ventana1,text=self.telefono[x])
            self.labe5.grid(column=1,row=x+1)
            self.label10=tk.Label(self.ventana1,text=self.mail[x])
            self.label10.grid(column=2, row=x+1)
    def consulta(self):
        self.ventana1=tk.Tk()
        self.label8=tk.Label(self.ventana1,text="Ingrese contacto a consultar:")
        self.label8.grid(column=0,row=0)
        self.dato4=tk.StringVar(self.ventana1)
        self.entry5=tk.Entry(self.ventana1,width=10,textvariable=self.dato4)
        self.entry5.grid(column=0,row=1)
        self.boton7=tk.Button(self.ventana1,text="Consultar",command=self.show)
        self.boton7.grid(column=0,row=4)
    def show(self):
        for x in range(len(self.nombre)):
            if self.dato4.get()==self.nombre[x]:
                self.labe1=tk.Label(self.ventana1,text="Telefono: ")
                self.labe1.grid(column=0,row=2)
                self.label9=tk.Label(self.ventana1,text=self.telefono[x])
                self.label9.grid(column=1,row=2)
                self.labe2=tk.Label(self.ventana1,text="Mail:")
                self.labe2.grid(column=0, row=3)
                self.label10=tk.Label(self.ventana1,text=self.mail[x])
                self.label10.grid(column=1, row=3)
    def modificar(self):
        self.ventana1=tk.Tk()
        self.lab1=tk.Label(self.ventana1,text="Ingrese contacto a modificar:")
        self.lab1.grid(column=0,row=0)
        self.dato5=tk.StringVar(self.ventana1)
        self.entry7=tk.Entry(self.ventana1,width=10,textvariable=self.dato5)
        self.entry7.grid(column=1,row=0)
        self.boton8=tk.Button(self.ventana1,text="Modificar",command=self.showtime)
        self.boton8.grid(column=1,row=3)
    def showtime(self):
        for x in range(len(self.nombre)):
            if self.dato5.get()==self.nombre[x]:
                self.lab2=tk.Label(self.ventana1,text="Telefono: ")
                self.lab2.grid(column=0,row=1)
                self.dato6=tk.StringVar(self.ventana1)
                self.labe2=tk.Label(self.ventana1,text="Mail:")
                self.labe2.grid(column=0, row=2)
                self.dato7=tk.StringVar(self.ventana1)
                self.entry8=tk.Entry(self.ventana1,width=10,textvariable=self.dato7)
                self.entry8.grid(column=1,row=1)
                self.dato8=tk.StringVar(self.ventana1)
                self.entry6=tk.Entry(self.ventana1,width=10,textvariable=self.dato8)
                self.entry6.grid(column=1,row=2)
                self.boton9=tk.Button(self.ventana1,text="Guardar",command=self.guardas) 
                self.boton9.grid(column=1,row=4)
    def guardas(self):
        nom=self.dato5.get()
        tels=self.dato7.get()
        mai=self.dato8.get()
        for x in range(len(self.nombre)):
            if self.nombre[x]==nom:
                self.telefono[x]=tels
                self.mail[x]=mai
    def salir(self):
        sys.exit(0)
Alfa:Agenda()