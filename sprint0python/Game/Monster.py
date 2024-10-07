import Hero


class Monster:
    name = "Pepe"
    attack_dmg = 10
    defense_value = 10
    health = 20

    def attack(self,Hero):
        damage = Monster.attack_dmg-Hero.defense_value
        print("El monstruo ataca a " + Hero.name)
        if damage > 0:

            print("El héroe" + Hero.name + "ha recibido" + damage + "puntos de daño")

        else:
            print("El héroe ha bloqueado el ataque")

    def is_alive(self):
        if Monster.health>0:
            return True
        else:
            return False
