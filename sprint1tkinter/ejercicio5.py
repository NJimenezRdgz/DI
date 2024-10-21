import tkinter as tk



root = tk.Tk()
root.title("Ejercicio 5")
root.geometry("600x400")

def mostrar_seleccion():
    seleccion = var_check.get()
    root.config(background=seleccion)



var_check= tk.StringVar()
var_check.set("red")


check1 = tk.Radiobutton(root, text="Rojo",variable = var_check,value ="red",command=mostrar_seleccion)
check1.pack(pady=20)

check2 = tk.Radiobutton(root, text="Verde",variable=var_check,value ="green",command=mostrar_seleccion)
check2.pack(pady=21)

check3 = tk.Radiobutton(root, text="Azul",variable=var_check,value ="blue",command=mostrar_seleccion)
check3.pack(pady=23)





root.mainloop()
