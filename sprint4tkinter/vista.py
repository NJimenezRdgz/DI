import tkinter as tk
from tkinter import simpledialog


class GameView:
    def __init__(self, root, on_card_click_callback, update_move_count_callback, update_time_callback,model):
        self.model = model
        self.root = root
        self.on_card_click_callback = on_card_click_callback
        self.update_move_count_callback = update_move_count_callback
        self.update_time_callback = update_time_callback

        self.board_frame = None
        self.cards = {}
        self.card_buttons = {}
        self.moves_label = None
        self.time_label = None
        self.moves=0
        self.time=0

    def create_board(self, model):
        self.board_frame = tk.Toplevel(self.root)

        self.model = model

        for i in range(self.model.difficulty):
            for j in range(self.model.difficulty):
                card_image = self.model.hidden_image
                button = tk.Button(
                    self.board_frame,
                    image=card_image,
                    command=lambda row=i, col=j: self.card_click(row, col)
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                self.card_buttons[(i, j)] = button
                self.cards[(i, j)] = None

        self.moves_label = tk.Label(self.board_frame, text="Movimientos: 0")
        self.moves_label.grid(row=j+1)

        self.time_label = tk.Label(self.board_frame, text="Tiempo: 00:00")
        self.time_label.grid(row=j+2)


        self.update_move_count_callback(self.model.moves)
        self.update_time_callback(self.model.get_time())

    def card_click(self, row, col):
        if self.cards.get((row, col)) is None:
            self.reveal_card(row, col)
            self.update_move_count(1)
            self.on_card_click_callback((row, col))

    def reveal_card(self, row, col):
        card_image = self.model.images.get(self.model.board[row][col], self.model.hidden_image)
        self.cards[(row, col)] = card_image
        self.card_buttons[(row, col)].config(image=card_image)

    def update_board(self, pos, image_id):
        row, col = pos
        image = self.model.images.get(image_id, self.model.hidden_image)
        self.cards[(row, col)] = image
        self.card_buttons[(row, col)].config(image=image)

    def reset_cards(self, pos1, pos2):
        row1, col1 = pos1
        row2, col2 = pos2

        self.card_buttons[row1][col1].config(image=self.model.hidden_image)
        self.card_buttons[row2][col2].config(image=self.model.hidden_image)

    def update_move_count(self, moves):
        if self.moves_label:
            self.moves+=moves
            self.moves_label.config(text=f"Movimientos: {int(self.moves/2)}")

    def update_time(self, time):
        if self.time_label:
            self.time_label.config(text=f"Tiempo: {str(time)}")

    def destroy(self):
        if self.board_frame:
            self.board_frame.destroy()
        if self.moves_label:
            self.moves_label.destroy()
        if self.time_label:
            self.time_label.destroy()


class MainMenu:
    def __init__(self, root, start_game_callback, show_stats_callback, quit_callback):
        self.window = root
        self.window.title("Juego de memoria")
        self.player_name = None
        tk.Button(self.window, text="Jugar", command=start_game_callback).pack(pady=10)
        tk.Button(self.window, text="Estadísticas", command=show_stats_callback).pack(pady=10)
        tk.Button(self.window, text="Salir", command=quit_callback).pack(pady=10)

    def ask_player_name(self):
        try:
            self.player_name = simpledialog.askstring(title="Nombre del jugador",prompt="Por favor, introduce tu nombre:",parent=self.window)
            print(self.player_name)
        except:
            print("No se introdujo ningún nombre.")
            return None
    def show_stats(self, stats):
        pass
