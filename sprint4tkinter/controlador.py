import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, Label, Tk
from modelo import GameModel
from vista import MainMenu, GameView
import time


class GameController:
    def __init__(self,root):
        self.root = root
        self.difficulty="fácil"
        self.player_name="Jugador"
        self.model = GameModel(self.difficulty,self.player_name,100)
        self.main_menu = MainMenu(self.root,(lambda: self.start_game(self.show_difficulty_selection())),self.show_stats,exit)


    def show_difficulty_selection(self):
        while True:
            show_difficulty_button = simpledialog.askstring(title="Elige dificultad",prompt="fácil // medio // difícil",parent=self.root)
            if show_difficulty_button is None:
                return None
            elif show_difficulty_button in ["fácil", "medio", "difícil"]:
                self.difficulty=show_difficulty_button
                return show_difficulty_button
            else:
                messagebox.showerror(title="Entrada no válida",message="Por favor, introduce una opción válida: fácil, medio o difícil.")

    def start_game(self, difficulty):
        game_start_window = Toplevel(self.root)
        tk.Label(game_start_window, text=f"Dificultad: {difficulty}").pack(padx=10, pady=10)

        self.main_menu.ask_player_name()
        self.player_name = self.main_menu.player_name

        if self.player_name:
            self.model = GameModel(difficulty, self.player_name)
            self.show_loading_window("Cargando imágenes...")
            self.model._load_images()
            self.check_images_loaded()
        else:
            messagebox.showerror("Error", "El nombre del jugador es obligatorio para empezar el juego.")

    def show_loading_window(self, message):
        self.loading_window = Toplevel(self.root)
        self.loading_window.title("Cargando...")
        label = Label(self.loading_window, text=message)
        label.pack(padx=10, pady=10)

    def show_game_view(self):
        self.game_view = GameView(self.root,self.on_card_click,self.update_move_count,self.update_time,self.model)
        self.game_view.create_board(self.model)
    def check_images_loaded(self):
        def check():
            if self.model.images_are_loaded():
                self.loading_window.destroy()
                self.show_game_view()
            else:
                self.root.after(100, check)

        check()

    def on_card_click(self,position):
        print(f"Click en: ({position})")
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
    def update_time(self,time):
        print(time)
        pass