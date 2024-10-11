from Game import hero
from Game.hero import Hero
from Game.monster import Monster
from Game.treasure import Treasure
import random

class Dungeon:
    def __init__(self, hero):
        # Inicializa el héroe y crea una lista de monstruos y un tesoro
        self.hero = hero
        self.monsters = [Monster("Goblin"), Monster("Orc"), Monster("Devil")]
        self.treasure = Treasure()

    def play(self):
        # Comienza el juego y verifica si el héroe está vivo y hay monstruos vivos
        print("The hero enters the dungeon")
        while self.hero.is_alive() and any(monster.is_alive() for monster in self.monsters):
            alive_monsters = [monster for monster in self.monsters if monster.is_alive()]
            curr_monster = random.choice(alive_monsters)  # Selecciona un monstruo vivo al azar

            print("You've found a: " + curr_monster.monster_name)
            print("The battle begins!!!")
            self.fight_monster(curr_monster)  # Llama a la función de pelea con el monstruo
            self.treasure.find_treasure(self.hero)  # busca un tesoro después de la pelea

        # Verifica si el héroe ha muerto o si ha derrotado a todos los monstruos
        if not self.hero.is_alive():
            print("Game over! The hero has died.")
        else:
            print("All monsters have been defeated! Victory!")

    def fight_monster(self, monster):
        # Maneja el combate entre el héroe y el monstruo
        while self.hero.is_alive() and monster.is_alive():
            action = input("What are you going to do?\n 1.Attack\n 2.Block\n 3.Heal\n")

            if action == "1":
                self.hero.attack(monster)  # El héroe ataca al monstruo
                if monster.is_alive():
                    monster.attack(self.hero)  # El monstruo contraataca si sigue vivo
                else:
                    return  # Sale de la función si el monstruo ha sido derrotado
            elif action == "2":
                self.hero.block()  # El héroe se defiende
                monster.attack(self.hero)  # El monstruo ataca al héroe
                self.hero.reset_block()  # Restaura la defensa del héroe
            elif action == "3":
                self.hero.heal()  # El héroe se cura
                monster.attack(self.hero)  # El monstruo ataca después de que el heroe se cure
