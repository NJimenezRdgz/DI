from django.template.defaultfilters import random
import random

class Monster:
    def __init__(self, monster_name):
        # Inicializa las propiedades del monstruo
        self.monster_name = monster_name
        self.monster_attack_dmg = random.randint(5, 20)  # Daño de ataque aleatorio entre 5 y 20
        self.monster_defense_value = random.randint(3, 10)  # Valor de defensa aleatorio entre 3 y 10
        self.monster_health = random.randint(20, 40)  # Salud aleatoria entre 20 y 40

    def attack(self, hero):
        # Calcula el daño al héroe basándose en el ataque del monstruo y la defensa del héroe
        damage = self.monster_attack_dmg - hero.hero_defense_value
        print(self.monster_name + " attacks " + hero.hero_name)

        if damage > 0:
            # Si el daño es positivo, se aplica al héroe
            print(hero.hero_name + " has received " + str(damage) + " points of damage")
            hero.hero_health -= damage
            if hero.hero_health <= 0:
                print("You've died :(")  # Mensaje si el héroe muere
            else:
                print("Current hero's health: " + str(hero.hero_health))
        else:
            # Si el daño es cero o negativo, el ataque ha sido bloqueado
            print("The hero has blocked the attack")

    def is_alive(self):
        # Devuelve True si el monstruo está vivo, False si ha muerto
        return self.monster_health > 0
