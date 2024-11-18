import tkinter as tk
from tkinter import simpledialog
from tkinter import Toplevel

class GameView:
    def __init__(self, on_card_click_callbackk,update_move_count_callback,update_time_callback):
        self.window = None
        self.labels = {}
        self.on_card_click_callback = on_card_click_callbackk
        self.update_move_count_callback = update_move_count_callback
        self.update_time_callback = update_time_callback

    def create_board(self,model):
        pass
    def update_board(self,pos,image_id):
        pass
    def reset_cards(self,pos1,pos2):
        pass
    def update_move_count(self,moves):
        pass
    def update_time(self,time):
        pass
    def destroy(self):
        pass

class MainMenu:
    def __init__(self, root, start_game_callback, show_stats_callback, quit_callback):
        self.window=root
        self.window.title("Juego memoria")
        self.player_name=None
        (tk.Button(self.window,text="Jugar",command=start_game_callback).pack(pady=10))
        (tk.Button(self.window,text="Estadísticas",command=show_stats_callback).pack(pady=10))
        (tk.Button(self.window,text="Salir",command=quit_callback).pack(pady=10))


    def ask_player_name(self):
        player_name = simpledialog.askstring(title="Nombre del jugador",prompt="Por favor, introduce tu nombre:",parent=self.window)
        if player_name:
            print(player_name)
            self.player_name = player_name
        else:
            print("No se introdujo ningún nombre.")
            return None

    def show_stats(self,stats):
        pass