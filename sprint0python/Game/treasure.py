from django.template.defaultfilters import random
import random

class Treasure:
    def __init__(self):
        # Inicializa la lista de beneficios que puede encontrar el héroe
        self.benefits = ["Potion of Strength", "Potion of Toughness", "Healing Potion"]

    def find_treasure(self, hero):
        # Selecciona un beneficio aleatorio de la lista de tesoros
        random_benefit = random.choice(self.benefits)
        print("The hero has found a treasure: " + random_benefit)

        # Aplica el beneficio encontrado al héroe
        if random_benefit == "Potion of Strength":
            hero.hero_attack_dmg += 10  # Aumenta el daño de ataque del héroe
            print(hero.hero_name + "'s attack increases to " + str(hero.hero_attack_dmg))
        elif random_benefit == "Potion of Toughness":
            hero.hero_defense_value += 10  # Aumenta la defensa del héroe
            print(hero.hero_name + "'s defense increases to " + str(hero.hero_defense_value))
        elif random_benefit == "Healing Potion":
            hero.hero_health = hero.hero_max_health  # Restaura la salud del héroe
            print(hero.hero_name + "'s health has been restored to " + str(hero.hero_max_health))
