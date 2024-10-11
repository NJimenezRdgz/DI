import Monster


class Hero:
    name = None
    attack_dmg = 10
    defense_value = 20
    health = 20
    max_health = 100


    def attack(self,Monster):
        damage = Hero.attack_dmg - Monster.defense_value
        print("Héroe ataca a " + Monster.name)
        if damage>0:


            print("El enemigo" + Monster.name+ "ha recibido" + damage + "puntos de daño")

        else:
            print("El enemigo ha bloqueado el ataque")

    def heal(self):
        Hero.health + 10
        if Hero.health > Hero.max_health:
                Hero.health=100
        print("Héroe se ha curado. Salud actual:" + Hero.health)


    def block(self):
        Hero.defense_value + 5
        print("Héroe se defiende. Defensa aumentada temporalmente a " + Hero.defense_value)

    def reset_block(self):
        Hero.defense_value - 5
        print("La defensa de" + Hero.name + "vuelve a la normalidad")
    def is_alive(self):
        if Hero.health>0:
            return True
        else:
            return False