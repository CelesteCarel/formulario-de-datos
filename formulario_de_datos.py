##3MLIDTS-CelesteCordova-03Python
##Formulario de registro
##Almacenamiento en TXT sin validación
import tkinter as tk
from tkinter import messagebox

def limpiar_campos():
    tbNombre.delete(0, tk.END)
    tbApellido.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    var_genero.set(0)

def borrar():
    limpiar_campos()
    
def guardar_campos():
    nombre = tbNombre.get()
    apellido = tbApellido.get()
    edad = tbEdad.get()
    telefono = tbTelefono.get()
    estatura = tbEstatura.get()
    genero = ""
    if var_genero.get() ==1:
        genero = "Hombre"
    elif var_genero.get() ==2:
        genero = "Mujer"
        
    datos = "Nombre: "+ nombre + "\n" + "Apellido: " + apellido + "\n" + "Edad: " + edad + "\n" + "Telefono: "+telefono + "\n" + "Estatura: " + estatura + "\n" + "Genero: " + genero + "\n" 
    with open ("C:/Users/bogab/Desktop/formulario python.txt", "a") as archivo: 
        archivo.write(datos+"\n\n")
    
    messagebox.showinfo("Informacion", "Datos guardados con exito: \n\n" +datos)
    limpiar_campos()
   
    
ventana = tk.Tk()
ventana.geometry("520x500")
ventana.title("Formulario 01")


# Variable para Radiobutton
var_genero = tk.IntVar()

# Nombres
lbNombre = tk.Label(ventana, text="Nombres: ")
lbNombre.pack()
tbNombre = tk.Entry(ventana)
tbNombre.pack()

# Apellidos
lbApellido = tk.Label(ventana, text="Apellidos: ")
lbApellido.pack()
tbApellido = tk.Entry(ventana)
tbApellido.pack()

# Edad
lbEdad = tk.Label(ventana, text="Edad: ")
lbEdad.pack()
tbEdad = tk.Entry(ventana)
tbEdad.pack()

# Teléfono
lbTelefono = tk.Label(ventana, text ="Telefono: ")
lbTelefono.pack()
tbTelefono = tk.Entry(ventana)
tbTelefono.pack()

# Estatura
lbEstatura = tk.Label(ventana, text ="Estatura: ")
lbEstatura.pack()
tbEstatura = tk.Entry(ventana)
tbEstatura.pack()

# Género
lbGenero = tk.Label(ventana, text="Genero: ")
lbGenero.pack()

rbHombre = tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbHombre.pack()

rbMujer = tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbMujer.pack()

btnBorrar = tk.Button(ventana, text = "Borrar valores", command=borrar)
btnBorrar.pack()

btnGuardar = tk.Button(ventana, text = "Guardar valores", command=guardar_campos)
btnGuardar.pack()

ventana.mainloop()

