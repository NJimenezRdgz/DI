import tkinter as tk
from tkinter import messagebox

def nueva_ventana():
    messagebox.showinfo("Nuevo", "Abrir una nueva ventana")

def salir_aplicacion():
    root.quit()


root = tk.Tk()
root.title("Ejercicio 9")
root.geometry("600x400")

menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Abrir",command=nueva_ventana)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir_aplicacion)

def mostrar_ayuda():
    messagebox.showinfo("Ayuda", "Esto es un mensaje de Ayuda.")

menu_ayuda = tk.Menu(menu_principal,tearoff=0)
menu_principal.add_cascade(label="Ayuda",menu=menu_ayuda)
menu_ayuda.add_command(label = "Acerca de", command=mostrar_ayuda)



root.mainloop()