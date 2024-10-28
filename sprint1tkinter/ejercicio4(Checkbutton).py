import tkinter as tk

root = tk.Tk()
root.title("Ejercicio 4")
root.geometry("600x400")

def mostrar_seleccion():
    seleccion1 = var_check1.get()
    seleccion2 = var_check2.get()
    seleccion3 = var_check3.get()

    estado_leer = "Leer" if seleccion1 else " "
    estado_deporte = "Deporte" if seleccion2 else " "
    estado_musica = "Música" if seleccion3 else " "
    etiqueta.config(text=estado_leer+ " " +estado_deporte + " " +estado_musica)


var_check1 = tk.IntVar()
var_check2 = tk.IntVar()
var_check3 = tk.IntVar()

check1 = tk.Checkbutton(root, text="Leer",variable = var_check1,command=mostrar_seleccion)
check1.pack(pady=20)

check2 = tk.Checkbutton(root, text="Deporte",variable=var_check2,command=mostrar_seleccion)
check2.pack(pady=21)

check3 = tk.Checkbutton(root, text="Música",variable=var_check3,command=mostrar_seleccion)
check3.pack(pady=23)

etiqueta = tk.Label(root, text="")
etiqueta.pack(pady=10)




root.mainloop()
