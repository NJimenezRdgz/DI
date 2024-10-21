import tkinter as tk

def insertar_texto():
    for i in range(1,200):
        cuadro_texto.insert(tk.END, f"Línea{i}\n")


root = tk.Tk()
root.title("Ejercicio 10")
root.geometry("600x400")

frame = tk.Frame(root)
frame.pack(fill='both',expand = True)

cuadro_texto = tk.Text(frame, wrap='none')
cuadro_texto.grid(row=0,column=0,sticky='nsew')

scroll_vert = tk.Scrollbar(frame, orient = 'vertical', command = cuadro_texto.yview)
scroll_vert.grid(row = 0, column = 1, sticky = 'ns')
cuadro_texto.config(xscrollcommand=scroll_vert.set)

scroll_horiz = tk.Scrollbar(frame, orient = 'horizontal', command = cuadro_texto.xview)
scroll_horiz.grid(row = 1, column = 0, sticky = 'ew')
cuadro_texto.config(xscrollcommand=scroll_horiz.set)

frame.grid_rowconfigure(0,weight=1)
frame.grid_columnconfigure(0,weight=1)
insertar_texto()

root.mainloop()
