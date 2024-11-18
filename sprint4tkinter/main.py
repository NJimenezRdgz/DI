import tkinter as tk
from controlador import GameController
from modelo import GameModel
from vista import MainMenu
from sprint4tkinter.vista import GameView


def main():
    root = tk.Tk()
    model = GameModel("fácil","Jugador")
    controller = GameController(root)
    root.mainloop()


if __name__ == "__main__":
    main()