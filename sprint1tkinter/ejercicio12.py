import tkinter as tk
from tkinter import messagebox


def actualizar_valor(edad):
    etiqueta_edad.config(text=f"Edad:")


root = tk.Tk()
root.title("Ejercicio12")
root.geometry("600x400")

lista_personas = []
etiqueta_nombre = tk.Label(root, text="Nombre")
etiqueta_nombre.grid(row=0,column=0, sticky = 'nsew')
entry_nombre = tk.Entry(root,width=30)
entry_nombre.grid(row=0,column=1, sticky = 'nsew')
scale_edad = tk.Scale(root, from_= 0, to = 100, orient= 'horizontal', command = actualizar_valor)
scale_edad.grid(row=1,column=1, sticky = 'nsew')

etiqueta_edad = tk.Label(root, text="Edad: ")
etiqueta_edad.grid(row=1,column=0, sticky = 'nsew')

def mostrar_seleccion():
    seleccion = var_genero.get()

var_genero= tk.StringVar()
var_genero.set("0tro")
etiqueta_genero = tk.Label(root, text="Género: ")
etiqueta_genero.grid(row=2,column=0, sticky = 'nsew')
check1 = tk.Radiobutton(root, text="Hombre",variable = var_genero,value ="Hombre",command=mostrar_seleccion)
check1.grid(row=2,column=1, sticky = 'nsew')
check2 = tk.Radiobutton(root, text="Mujer",variable=var_genero,value ="Mujer",command=mostrar_seleccion)
check2.grid(row=2,column=2, sticky = 'nsew')
check3 = tk.Radiobutton(root, text="Otro",variable=var_genero,value ="Otro",command=mostrar_seleccion)
check3.grid(row=2,column=3, sticky = 'nsew')

def guardar_persona_en_lista():
    persona =[entry_nombre.get(),scale_edad.get(),var_genero.get()]
    lista_personas.append(persona)

    listbox.insert(tk.END, persona)


boton_guardar_persona = tk.Button(root, text= "Guardar usuario", command=guardar_persona_en_lista)
boton_guardar_persona.grid(row = 3, column = 0)

listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.grid(row=4,columnspan=2)

def borrar_persona_en_lista():
    listbox.delete(listbox.curselection())

boton_borrar_persona = tk.Button(root, text= "Borrar usuario", command=borrar_persona_en_lista)
boton_borrar_persona.grid(row = 5, column = 0)


scroll_vert = tk.Scrollbar(root, command = listbox.yview)
scroll_vert.grid(row = 4, column= 1, sticky = 'ns')
listbox.config(yscrollcommand=scroll_vert.set)

def salir_aplicacion():
    root.quit()
boton_salir_aplicacion = tk.Button(root, text= "Salir de la aplicación", command=salir_aplicacion)
boton_salir_aplicacion.grid(row = 6, column = 3)

def mostrar_carga():
    messagebox.showinfo("Cargar", "Lista Cargada.")

def mostrar_guardar():
    messagebox.showinfo("Guardar", "Lista Guardada.")
menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Opciones", menu=menu_archivo)
menu_archivo.add_command(label="Guardar Lista",command=mostrar_guardar)
menu_archivo.add_separator()
menu_archivo.add_command(label="Cargar Lista", command=mostrar_carga)



root.mainloop()