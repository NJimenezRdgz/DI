import tkinter as tk
from bisect import insort
from pydoc import text


def mostrar_selecciones():
    seleccion = listbox.curselection()
    elementos = [listbox.get(i) for i in seleccion]

    etiqueta.config(text = f"Seleccionaste: {', '.join(elementos)}")

root = tk.Tk()
root.title("Ejercicio 6")
root.geometry("300x250")

opciones = ["Manzana", "Banana","Naranja"]

listbox = tk.Listbox(root, selectmode= tk.SINGLE)
for opcion in opciones:
    listbox.insert(tk.END, opcion)
listbox.pack(pady=10)

boton = tk.Button(root, text="Mostrar Selección", command=mostrar_selecciones)
boton.pack(pady=5)

etiqueta = tk.Label(root, text="Seleccionaste: Ninguno")
etiqueta.pack(pady=10)

root.mainloop()
