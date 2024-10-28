import tkinter as tk


root = tk.Tk()
root.title("Ejercicio 2")
root.geometry("300x200")
def mostrar_mensaje():
    etiqueta1 = tk.Label(root, text="Bienvenid@!")
    etiqueta1.pack()
def close():
    root.destroy()


boton1 = tk.Button(root, text= "Haz click aquí", command=mostrar_mensaje, bg="green", fg="white")
boton1.pack(pady=50)

boton2 = tk.Button(root, text= "Haz click para cerrar", command=close, bg="green", fg="white")
boton2.pack(pady=10)


root.mainloop()
