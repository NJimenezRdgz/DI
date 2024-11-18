import tkinter as tk
from controlador import GameController
from modelo import GameModel
from vista import MainMenu
from sprint4tkinter.vista import GameView


def main():
    root = tk.Tk()
    #model = GameModel("easy","Name")
    controller = GameController(root)
    #vista = MainMenu(root,None,None,None)
    root.mainloop()


if __name__ == "__main__":
    main()