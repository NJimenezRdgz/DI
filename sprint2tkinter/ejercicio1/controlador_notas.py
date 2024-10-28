import threading
import requests
from tkinter import messagebox

class ControladorNotas:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.vista.controlador = self
        self.modelo.cargar_notas()
        self.vista.actualizar_listbox(self.modelo.obtener_notas())

    def agregar_nota(self):
        nueva_nota = self.vista.entry_agregar_nota.get()
        if nueva_nota:
            self.modelo.agregar_nota(nueva_nota)
            self.vista.actualizar_listbox(self.modelo.obtener_notas())
            self.vista.entry_agregar_nota.delete(0, tk.END)

    def eliminar_nota(self):
        seleccion = self.vista.lista_notas.curselection()
        if seleccion:
            indice = seleccion[0]
            self.modelo.eliminar_nota(indice)
            self.vista.actualizar_listbox(self.modelo.obtener_notas())

    def guardar_notas(self):
        self.modelo.guardar_notas()
        messagebox.showinfo("Información", "Notas guardadas correctamente")

    def cargar_notas(self):
        self.modelo.cargar_notas()
        self.vista.actualizar_listbox(self.modelo.obtener_notas())

    def descargar_imagen(self):
        def tarea_descarga():
            url = "https://github.com/"  # Cambia esto por la URL real de la imagen
            respuesta = requests.get(url)
            if respuesta.status_code == 200:
                with open("imagen_descargada.jpg", "wb") as archivo:
                    archivo.write(respuesta.content)
                self.vista.mostrar_imagen("imagen_descargada.jpg")
            else:
                messagebox.showerror("Error", "No se pudo descargar la imagen")

        threading.Thread(target=tarea_descarga).start()

    def actualizar_coordenadas(self, event):
        self.vista.actualizar_coordenadas_label(event.x, event.y)
