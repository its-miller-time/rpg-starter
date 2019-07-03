import random

def main():
    #GLOBAL FUNCTIONS
    ##ASK QUESTION FUNCTION
    def ask(question,answers):
        answer = input(question)
        if answer not in answers:
            print("Not a valid answer!")
            return ask(question,answers)
        return answer

    #ALL ITEM CLASSES
    # class Store:
    #     def __init__(self):
    #         pass
    #     def sell_item(self):
    #         pass
    #     def buy_item(self):
    #         pass
    
    class Item(): 
        def __init__(self,name,price):
            self.name = name
            self.price = price

    sword = {"name":"sword", "price":10,"dmg":10}


    class Sword(Item):
        def __init__(self,name,price,dmg_bonus):
            super().__init__(name,price)
            self.dmg_bonus = dmg_bonus
    
    class Armor(Item):
        def __init__(self,name,price,dmg_reduction):
            super().__init__(name,price)
            self.dmg_reduction = dmg_reduction

    class SuperTonic(Item):
        def __init__(self,name,price,hp_bonus):
            super().__init__(name,price)
            self.hp_bonus = hp_bonus

    class EvadePotion(Item):
            def __init__(self,name,price,evade_bonus):
                super().__init__(name,price)
                self.evade_bonus = evade_bonus


    #STORE DICTIONARY

    def store()
        #store_items 
        excalibur = Sword("Excalibur",50,5), 
        rusty_sword = Sword("Rusty Sword",10,1),
        ##Potions
        super_tonic = SuperTonic("Super Tonic",10,10),
        evade_potion = EvadePotion("Evade Potion",15,1),
        ##Armor
        chest_plate = Armor("Chest Plate",15,3)
        

        item = input("""
        Choose and item to purchase:
        1 = Excalibur    | 50 coins | +5 damage
        2 = Rusty Sword  | 10 coins | +1 damage
        3 = Super Tonic  | 10 coins | +1 health
        4 = Evade Potion | 15 coins | +1 evade
        5 = Chest Plate  | 15 coins | +3 armor
        """)
        if item == "1":
            user_char.inventory.append(excalibur)
            print(f"You have purchased 1 {excalibur.name} ")
        elif item == "2"
            user_char.inventory.append(rusty_sword)
            print(f"You have purchased 1 {rusty_sword.name} ")
        elif item == "3":
            user_char.inventory.append(super_tonic)
            print(f"You have purchased 1 {super_tonic.name} ")
        elif item == "4":
            user_char.inventory.append(evade_potion)
            print(f"You have purchased 1 {super_tonic.name} ")
        elif item == "5":
            user_char.inventory.append(super_tonic)
            print(f"You have purchased 1 {rusty_sword.name} ")
        else: 
            print("Sorry, we don't carry that item.")
            store()

    # ALL CHARACTER CLASSES
    # character_attributes = {
    #     name : 
    #     health : 
    #     power : 
    #     coins :
    #     armor :
    # }
    
    class Character:
        def __init__(self,name,health,power,coins,armor,inventory):
            self.name = name
            self.health = health
            self.power = power
            self.coins = coins
            self.armor = armor
            self.inventory = inventory

        def attack(self,enemy):
            enemy.health -= (self.power - enemy.armor)
            print(f"You do {self.power} damage to the {enemy.name}.")
            print(f"You have {self.coins} coins ")
            if enemy.alive() != True:
                self.coins += enemy.coins
                print(f"The {self.name} is dead. {self.name} have {self.coins} coins.")
            print(f"The {enemy.name} has {enemy.health} health.")
        
        def alive(self):
            return (self.health > 0)
        
        def print_status(self):
            print("You have %d health and %d power." % (self.health, self.power))
        
        def use_item(self):
            print("What item would you like to use? ")
            print(user_char.inventory)

    class Hero(Character):
        def __init__(self,name,health,power,sp_att_dmg,coins,evade,armor,inventory):
            super().__init__(name,health,power,coins,armor,inventory)
            self.sp_att_dmg = sp_att_dmg
            self.evade = evade

        def attack(self,enemy):
            attack_roll = 1
            sp_att = input("Do you want to do a special attack? (Y or N)" )
            if sp_att == "Y":
                if attack_roll == random.randint(0,4):
                    enemy.health -= self.sp_att_dmg
                    print("You do %d damage to the enemy." % self.sp_att_dmg)
                else:
                    print("Hero misses attack")
            else:
                enemy.health -= self.power

    class Medic(Character):
        def __init__(self,name,health,power,heal_dmg,coins,evade,armor,inventory):
            super().__init__(name,health,power,coins,armor,inventory)
            self.heal_dmg = heal_dmg
            self.coins = coins
            self.evade = evade

        def heal(self):
            heal_roll = 1
            if heal_roll == random.randint(0,4):
                self.health += self.heal_dmg
                print(f"You heal for {self.heal_dmg} health!")

    class Shadow(Character):
        def __init__(self,name,health,power,coins,evade,armor,inventory):
            super().__init__(name,health,power,coins,armor,inventory)
            self.evade = evade
        
        def dodge(self):
            if random.randint(1, 10)==1:
                enemy_char.attack(user_char)
            else:
                print('You dodge the attack.')

    class Goblin(Character):
        def __init__(self,name,health,power,coins,armor,inventory):
            super().__init__(name,health,power,coins,armor,inventory)

    class Zombie(Character):
        def __init__(self,name,health,power,coins,armor,inventory):
            super().__init__(name,health,power,coins,armor,inventory)

        def alive(self):
            return (True)

    #Create Characters Here
    user_select = input("""
    Select your character! 
    1 = Hero  
    2 = Medic
    3 = Shadow) 
    """)
    if user_select == "1":
        user_char = Hero('Ian',45,5,10,0,0,0,[])
    elif user_select == "2":
        user_char = Medic('Hypocrates',15,2,2,0,0,1,[])
    elif user_select == "3":
        user_char = Shadow("Shadow",1,20,0,2,0,[])
    else:
        print("Not a valid character")

    #Select Enemy 
    enemy_select = input("""
    Select your enemy 
    1 = goblin 
    2 = zombie)
    """)
    if enemy_select == "1":
        enemy_char = Goblin('Goblin',25,5,20,2,[])
    if enemy_select == "2":
        enemy_char = Zombie('Zombie',100,2,50,0,[])

    while user_char.alive() == True and enemy_char.alive() == True:
        print()
        print("What do you want to do?")
        print(f"1. Fight {enemy_select}")
        print("2. Do nothing")
        print("3. Flee")
        print("4. Store")
        print("5. Use Item")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks enemy
            user_char.attack(enemy_char)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        elif user_input == "4":
            store()
        else:
            print("Invalid input %r" % user_input)
        
        if enemy_char.alive() == True:
            # Enemy attacks hero
            if type(user_char) == Shadow:
                user_char.dodge()
            elif type(user_char) == Medic:
                user_char.heal()
            elif user_char.health <= 0:
                print("You are dead.") 
            else:
                enemy_char.attack(user_char)
            print("Enemy Round Over")

main()

