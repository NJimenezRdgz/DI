import tkinter as tk



def mostrar_texto():
    texto = entry.get()
    etiqueta_texto.config(text = texto)

def borrar_texto():
    etiqueta_texto.config(text = "")

root = tk.Tk()
root.title("Ejercicio 8")
root.geometry("600x400")


frame1 = tk.Frame(root, bg="lightgrey",bd = 2, relief= "sunken")
frame1.pack(padx=20,pady=20,fill='both',expand=True)

etiqueta1 = tk.Label(frame1,text="Etiqueta dentro del Frame", bg="lightgrey")
etiqueta1.pack(pady=10)

etiqueta2 = tk.Label(frame1, text="Etiqueta 2",bg="lightgrey")
etiqueta2.pack(pady=10)

entry= tk.Entry(frame1,width=30, bg = "lightgrey")
entry.pack(pady=5)

frame2 = tk.Frame(root, bg="lightgrey",bd = 2, relief= "sunken")
frame2.pack(padx=20,pady=20,fill='both',expand=True)


boton_escribir = tk.Button(frame2,text="Mostrar texto", command=mostrar_texto, bg ="lightgrey")
boton_escribir.pack(pady=10)

boton_borrar = tk.Button(frame2, text="Borrar texto",command= borrar_texto,bg="lightgrey")
boton_borrar.pack(pady=10)


etiqueta_texto = tk.Label(frame2,text = "", bg="lightgrey")
etiqueta_texto.pack(pady=10)

root.mainloop()
