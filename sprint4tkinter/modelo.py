import threading
import time
import random
import datetime
from sprint4tkinter.recursos import descargar_imagen


class GameModel:
    def __init__(self, difficulty, player_name, cell_size=100):
        self.difficulty = difficulty
        self.player_name = player_name
        self.cell_size = cell_size
        self.board = self._generate_board()
        self.images = {}
        self.images_loaded = False
        self.images_loaded_event = threading.Event()


    def _generate_board(self):
            if self.difficulty=="fácil":
                columna=4
                fila = 4
            elif self.difficulty == "medio":
                columna = 6
                fila = 6
            elif self.difficulty == "difícil":
                columna = 8
                fila = 8

            total_cartas = fila*columna

            parejas = list(range(total_cartas//2))*2

            random.shuffle(parejas)
            return [parejas[i:i + columna] for i in range(0, total_cartas, columna)]

    def _load_images(self):
        def load_images_thread():
            try:
                url_base = "https://github.com/NJimenezRdgz/DI/tree/main/sprint4tkinter/res"
                self.hidden_image = descargar_imagen(f"{url_base}hidden.png", (100, 100))
                if self.hidden_image is None:
                    raise Exception("Error al cargar la imagen oculta.")
                unique_image_ids = []
                for row in self.board:
                    for image_id in row:
                        if image_id not in unique_image_ids:
                            unique_image_ids.append(image_id)
                for image_id in unique_image_ids:
                    image_url = f"{url_base}carta_{image_id}.png"
                    self.images[image_id] = descargar_imagen(image_url, (100, 100))
                    if self.images[image_id] is None:
                        raise Exception(f"Error al cargar la imagen de la carta {image_id}.")
                self.images_loaded = True
                self.images_loaded_event.set()
            except Exception as e:
                print(f"Error en load_images_thread: {e}")
                self.images_loaded_event.set()

        threading.Thread(target=load_images_thread, daemon=True).start()

    def images_are_loaded(self):
        return self.images_loaded
    def start_timer(self):
        pass
    def get_time(self):
        pass
    def check_match(self,pos1,pos2):
        pass
    def is_game_complete(self):
        pass
    def save_score(self):
        pass
    def load_scores(self):
        pass