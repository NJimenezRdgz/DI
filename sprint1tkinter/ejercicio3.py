import tkinter as tk


def obtener_texto():
    texto=entry.get()
    etiqueta_saludo.config(text=f"Saludos, {texto}")

root = tk.Tk()
root.title("Ejemplo de entry")
root.geometry("300x200")

entry= tk.Entry(root,width=30)
entry.pack(pady=5)

boton = tk.Button(root, text="Saludar ", command=obtener_texto)
boton.pack(pady=5)
etiqueta_saludo = tk.Label(root,text="")
etiqueta_saludo.pack(pady=10)

root.mainloop()
