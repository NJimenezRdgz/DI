import threading
import time
import random
import datetime
from sprint4tkinter.recursos import descargar_imagen
import tkinter as tk


class GameModel:
    def __init__(self, difficulty, player_name, cell_size=100):
        if difficulty == "fácil" or difficulty == "facil":
            self.difficulty = 4
        elif difficulty == "medio":
            self.difficulty = 6
        elif difficulty =="difícil":
            self.difficulty = 8

        self.name = player_name
        self.moves = 0
        self.start_time = None
        self.images_loaded = False
        self.cell_size = cell_size
        self.board = None
        self.cards = None
        self.hidden_image = None
        self.images = {}
        self.pairs = 0
        self.pairs_found = 0
        self.timer_start_time = 0
        self.start_time = time.time()
        self.timer_elapsed=0
        self.img_names = [
            'Bloodstone.png',
            'Blueprint.png',
            'Brainstorm.png',
            'Burnt_Joker.png',
            'Canio.png',
            'Cavendish.png',
            'Chicot.png',
            'Defect.png',
            'Driver27s_License.png',
            'Flower_Pot.png',
            'Glass_Joker.png',
            'Hanging_Chad.png',
            'Invisible_Joker.png',
            'Ironclad.png',
            'Isaac.png',
            'Lucky_Cat.png',
            'Oops21_All_6s.png',
            'Perkeo.png',
            'Photograph.png',
            'Shoot_the_Moon.png',
            'Showman.png',
            'Silent.png',
            'Smeared_Joker.png',
            'Sock_and_Buskin.png',
            'Spare_Trousers.png',
            'Stuntman.png',
            'The_Family.png',
            'The_Idol.png',
            'Trading_Card.png',
            'Triboulet.png',
            'Wee_Joker.png',
            'Yorick.png',
            'hidden.png'
        ]

        if self.name != "no":
            self._generate_board()
            self._load_images()


    def _generate_board(self):
        num_cards = int((self.difficulty * self.difficulty) // 2)
        self.pairs = num_cards
        random.shuffle(self.img_names)
        self.cards = self.img_names[:num_cards] * 2
        random.shuffle(self.cards)
        self.board = [[None for _ in range(self.difficulty)] for _ in range(self.difficulty)]
        index = 0
        for i in range(self.difficulty):
            for j in range(self.difficulty):
                self.board[i][j] = self.cards[index]
                print(self.cards[index])
                index += 1

    def _load_images(self):
        def load_images_thread():
            url_base = "https://raw.githubusercontent.com/NJimenezRdgz/DI/refs/heads/main/sprint4tkinter/res/"


            self.hidden_image = descargar_imagen(url_base + "hid/hidden.png", (self.cell_size, self.cell_size))

            unique_image_ids = []
            for i in range(self.difficulty):
                for j in range(self.difficulty):
                    if self.board[i][j] not in unique_image_ids:
                        unique_image_ids.append(self.board[i][j])

            for image_name in unique_image_ids:
                url = url_base + image_name
                if url != "https://raw.githubusercontent.com/NJimenezRdgz/DI/refs/heads/main/sprint4tkinter/res/hidden.png":
                    photo_image = descargar_imagen(url, (self.cell_size, self.cell_size))

                self.images[image_name] = photo_image

            self.images_loaded = True

        threading.Thread(target=load_images_thread, daemon=True).start()


    def images_are_loaded(self):
        return self.images_loaded

    def start_timer(self):
        self.start_time = time.time()
    def get_time(self):
        if self.start_time is None:
            return 0
        return int(time.time() - self.start_time)

    def check_match(self,pos1,pos2):
        pass

    def is_game_complete(self):
        pass

    def save_score(self):
        pass

    def load_scores(self):
        pass
