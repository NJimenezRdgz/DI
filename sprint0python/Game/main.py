from Game.hero import Hero
from Game.dungeon import Dungeon

def main():
    # solicita el nombre del héroe al usuario
    hero_name = input("Name?: ")
    hero = Hero(hero_name)  # Crea una instancia del héroe

    dungeon = Dungeon(hero)  # Crea una instancia de la clase Dungeon
    dungeon.play()  # Inicia el juego

if __name__ == "__main__":
    main()  # Llama a la función main
