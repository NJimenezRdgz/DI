import tkinter as tk

from controlador_notas import ControladorNotas
from notas_model import NotasModel
from vista_notas import VistaNotas


def main():
    root = tk.Tk()
    modelo = NotasModel()
    vista = VistaNotas(root)
    controlador = ControladorNotas(modelo, vista)
    root.mainloop()


if __name__ == "__main__":
    main()