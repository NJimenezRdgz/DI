import tkinter as tk
from controlador import GameController
from modelo import GameModel
from vista import MainMenu
from sprint4tkinter.vista import GameView



if __name__ == "__main__":
    root = tk.Tk()
    controller = GameController(root)
    root.mainloop()