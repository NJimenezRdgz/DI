import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Mi ventana")
root.geometry("300x200")
etiqueta1 = tk.Label(root, text= "Bienvenid@!")
etiqueta1.pack()


etiqueta2 = tk.Label(root, text= "Mi nombre es Nico")
etiqueta2.pack()


def mostrar_mensaje():
    etiqueta3.config(text="Ha cambiado el texto")

etiqueta3 = tk.Label(root, text= "Texto original")
etiqueta3.pack()
boton1 = tk.Button(root, text= "Haz click aquí para cambiar el texto", command=mostrar_mensaje, bg="green", fg="white")
boton1.pack(pady=50)




root.mainloop()
