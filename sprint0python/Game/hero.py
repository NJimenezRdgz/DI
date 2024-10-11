from django.template.defaultfilters import random
import random

class Hero:
    def __init__(self, hero_name):
        # Inicializa las propiedades del héroe
        self.hero_name = hero_name
        self.hero_attack_dmg = random.randint(11, 30)  # Daño de ataque aleatorio entre 11 y 30
        self.hero_defense_value = random.randint(5, 15)  # Valor de defensa aleatorio entre 5 y 15
        self.hero_health = 100  # Salud inicial del héroe
        self.hero_max_health = 100  # Salud máxima del héroe

    def attack(self, monster):
        # Calcula el daño al monstruo basándose en el ataque del héroe y la defensa del monstruo
        damage = self.hero_attack_dmg - monster.monster_defense_value
        print("The hero attacks " + monster.monster_name)

        if damage > 0:
            # Si el daño es positivo, se aplica al monstruo
            print(monster.monster_name + " has received " + str(damage) + " points of damage")
            monster.monster_health -= damage
            if monster.monster_health <= 0:
                print("You've defeated the " + monster.monster_name)
            else:
                print("Current monster's health: " + str(monster.monster_health))
        else:
            # Si el daño es cero o negativo, el ataque ha sido bloqueado
            print("The monster has blocked the attack")

    def heal(self):
        # Aumenta la salud del héroe
        self.hero_health += 40
        if self.hero_health > self.hero_max_health:
            self.hero_health = self.hero_max_health  # Asegura que no supere la salud máxima
        print("The hero has healed up to 40hp. Current health: " + str(self.hero_health))

    def block(self):
        # Aumenta temporalmente el valor de defensa del héroe
        self.hero_defense_value += 10
        print("The hero defends themselves. Temporary defense increased to " + str(self.hero_defense_value))

    def reset_block(self):
        # Restaura el valor de defensa del héroe a su estado original
        self.hero_defense_value -= 10
        print(self.hero_name + "'s defense is back to: " + str(self.hero_defense_value))

    def is_alive(self):
        # Devuelve True si el héroe está vivo, False si está muerto
        return self.hero_health > 0
