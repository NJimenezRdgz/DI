# vista_notas.py
import tkinter as tk
from PIL import Image, ImageTk

class VistaNotas:
    def __init__(self, controlador=None):
        self.controlador = controlador
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("Gestión de Notas")
        self.root.bind("<Button-1>", self.click_izquierdo)

        self.titulo_aplicacion = tk.Label(self.root, text="Gestión de Notas")
        self.titulo_aplicacion.pack(pady=10)

        self.lista_notas = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.lista_notas.pack(pady=5)

        self.entry_agregar_nota = tk.Entry(self.root)
        self.entry_agregar_nota.pack(pady=10)

        self.boton_agregar_nota = tk.Button(self.root, text="Agregar nota", command=self.agregar_nota)
        self.boton_agregar_nota.pack(pady=5)

        self.boton_eliminar_nota = tk.Button(self.root, text="Eliminar nota", command=self.eliminar_nota)
        self.boton_eliminar_nota.pack(pady=5)

        self.boton_guardar_notas = tk.Button(self.root, text="Guardar notas", command=self.guardar_notas)
        self.boton_guardar_notas.pack(pady=5)

        self.boton_cargar_notas = tk.Button(self.root, text="Cargar notas", command=self.cargar_notas)
        self.boton_cargar_notas.pack(pady=5)

        self.boton_descargar_imagen = tk.Button(self.root, text="Descargar imagen", command=self.descargar_imagen)
        self.boton_descargar_imagen.pack(pady=5)

        self.coordenadas_raton = tk.Label(self.root, text="Coordenadas click ratón: None")
        self.coordenadas_raton.pack(pady=10)

        self.label_imagen = tk.Label(self.root)
        self.label_imagen.pack()

        self.root.mainloop()

    def set_controlador(self, controlador):
        self.controlador = controlador
        self.boton_agregar_nota.config(command=self.controlador.agregar_nota)
        self.boton_eliminar_nota.config(command=self.controlador.eliminar_nota)
        self.boton_guardar_notas.config(command=self.controlador.guardar_notas)
        self.boton_cargar_notas.config(command=self.controlador.cargar_notas)
        self.boton_descargar_imagen.config(command=self.controlador.descargar_imagen)

    def actualizar_listbox(self, notas):
        self.lista_notas.delete(0, tk.END)
        for nota in notas:
            self.lista_notas.insert(tk.END, nota)

    def mostrar_imagen(self, imagen_path):
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((200, 200), Image.ANTIALIAS)
        self.imagen_tk = ImageTk.PhotoImage(imagen)
        self.label_imagen.config(image=self.imagen_tk)

    def actualizar_coordenadas_label(self, x, y):
        self.coordenadas_raton.config(text=f"Coordenadas click ratón: {x} {y}")

    def click_izquierdo(self, event):
        self.actualizar_coordenadas_label(event.x, event.y)

    def agregar_nota(self):
        if self.controlador:
            self.controlador.agregar_nota()

    def eliminar_nota(self):
        if self.controlador:
            self.controlador.eliminar_nota()

    def guardar_notas(self):
        if self.controlador:
            self.controlador.guardar_notas()

    def cargar_notas(self):
        if self.controlador:
            self.controlador.cargar_notas()

    def descargar_imagen(self):
        if self.controlador:
            self.controlador.descargar_imagen()
