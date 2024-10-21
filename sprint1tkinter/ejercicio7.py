import tkinter as tk


def dibujar_formas():
        x = int(entry_x.get())
        y = int(entry_y.get())
        ancho_rect = int(entry_ancho.get())
        alto_rect = int(entry_alto.get())
        diametro_circulo = int(entry_diametro.get())

        canvas.create_rectangle(x, y, x + ancho_rect, y + alto_rect, outline="blue", width=2)
        canvas.create_oval(x + 10, y + 10, x + 10 + diametro_circulo, y + 10 + diametro_circulo, fill="red")




root = tk.Tk()
root.title("Ejercicio 7")
root.geometry("500x400")

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=20)

label_x = tk.Label(root, text="X:")
label_x.pack(pady=5)
entry_x = tk.Entry(root, width=30)
entry_x.pack(pady=5)

label_y = tk.Label(root, text="Y:")
label_y.pack(pady=5)
entry_y = tk.Entry(root, width=30)
entry_y.pack(pady=5)

label_ancho = tk.Label(root, text="Ancho del rectángulo:")
label_ancho.pack(pady=5)
entry_ancho = tk.Entry(root, width=30)
entry_ancho.pack(pady=5)

label_alto = tk.Label(root, text="alto del rectángulo:")
label_alto.pack(pady=5)
entry_alto = tk.Entry(root, width=30)
entry_alto.pack(pady=5)

label_diametro = tk.Label(root, text="Diámetro del círculo:")
label_diametro.pack(pady=5)
entry_diametro = tk.Entry(root, width=30)
entry_diametro.pack(pady=5)

boton_dibujar = tk.Button(root, text="Dibujar", command=dibujar_formas)
boton_dibujar.pack(pady=10)

root.mainloop()
