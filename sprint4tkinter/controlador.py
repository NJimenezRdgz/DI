import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, Label, Tk
from modelo import GameModel
from vista import MainMenu, GameView
import time


class GameController:
    def __init__(self,root):
        self.root = root
        self.model = GameModel
        self.main_menu = MainMenu(self.root,(lambda: self.start_game(self.show_difficulty_selection())),self.show_stats,exit)

    def show_difficulty_selection(self):
        while True:
            show_difficulty_button = simpledialog.askstring(title="Elige dificultad",prompt="fácil // medio // difícil",parent=self.root)
            if show_difficulty_button is None:
                return None
            elif show_difficulty_button in ["fácil", "medio", "difícil"]:
                return show_difficulty_button
            else:
                messagebox.showerror(title="Entrada no válida",message="Por favor, introduce una opción válida: fácil, medio o difícil.")
    def start_game(self,difficulty):
        game_start_window = Toplevel(self.root)
        tk.Label(game_start_window,text = "Dificultad: "+difficulty).pack(padx=10,pady=10)
        self.main_menu.ask_player_name()
    def show_loading_window(self,message):
        pass
    def check_images_loaded(self):
        pass
    def on_card_click(self):
        pass
    def handle_card_selection(self):
        pass
    def update_move_count(self,moves):
        pass
    def check_game_complete(self):
        pass
    def return_to_main_menu(self):
        pass
    def show_stats(self):
        stats_window = Toplevel(self.root)
        tk.Label(stats_window,text = "Stats: 0").pack(padx=10,pady=10)
    def update_time(self):
        pass