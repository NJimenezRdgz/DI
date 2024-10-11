import Hero
import random

class Treasure:
    benefits = ["+Atk", "+Def","+HP"]

    def find_treasure(self,Hero):
        random_benefit = random.choice(Treasure.benefits)
        print("Héroe ha encontrado un tesoro" + Treasure.benefits)

        if random_benefit == "+Atk":
            Hero.attack_dmg + 10
            print("El ataque de" + Hero.name + "aumenta a"+Hero.attack_dmg)
        elif random_benefit == "+Def":
            Hero.defense_value +10
            print("La defensa de" + Hero.name + "aumenta a"+Hero.defense_value)
        elif random_benefit == "+HP":
            Hero.health = Hero.max_health
            print("La salud de" + Hero.name + "ha sido restaurada a "+Hero.max_health)


