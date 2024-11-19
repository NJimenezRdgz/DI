import tkinter as tk
from controlador import GameController  # Controlador para manejar la lógica del juego.

if __name__ == "__main__":
    root = tk.Tk()  # Instancia de la ventana principal de Tkinter.

    controller = GameController(root)
    root.mainloop()
