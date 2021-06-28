import pokebase
import random
from BattleSystem.move import Move

class Pokemon(object):
    def __init__(self, data, player):
        self.player = player
        self.data = data
        self.base_data = pokebase.pokemon(self.data['id'])
        self.name = self.data['nickname']
        self.moves = [Move(self.data['moves'][0]),
                      Move(self.data['moves'][1]),
                      Move(self.data['moves'][2]),
                      Move(self.data['moves'][3])]
        ##stat modifier
        self.crit_rate = 0
        ##volatile status
        self.bounded = 0
        self.trapped = False
        self.confused = 0
        self.cursed = False
        self.embargo = 0
        self.encore = 0
        self.healblocked = 0
        self.identified = False
        self.infatuated = False
        self.leechseeded = False
        self.nightmare = False
        self.perishsong = 0
        self.taunted = 0
        self.telekinesis = False
        self.tormented = False
        ##volatile battle status
        self.aquaring = False
        self.bracing = False
        self.charging = False
        self.center = False
        self.defensecurl = False
        self.roots = False
        self.magneticlev = False
        self.protect = False
        self.recharging = False
        self.dig = False
        self.fly = False
        self.dive = False
        self.disappear = False
        self.substitute = 0
        self.aimed = False
        self.withdraw = False

    def battle_menu(self, battle):
        if self.player.trainer_type == 0 or self.player.trainer_type == 1:
            self.move_menu(battle)

        if self.player.trainer_type == 2:
            print("What will", self.name, "do?")
            button = int(input("-- 0 move \n-- 1 switch\n-->"))
            if button == 0:
                self.move_menu(battle)

    def move_menu(self, battle):
        if self.player.trainer_type == 0 or self.player.trainer_type == 1:
            move_to_choose = []
            for i in range(4):
                if not self.moves[i].blank:
                    move_to_choose.append(i)
            move = random.choice(move_to_choose)
            targets = self.moves[move].select_target(self, battle)
            battle.moves_to_use.append([self, self.moves[move], targets])

        if self.player.trainer_type == 2:
            print("What move", self.name, "will use?")
            for i in range(4):
                if not self.moves[i].blank:
                    print("--", i, self.moves[i].base_data.name)
            print("--4 to cancel")
            button = int(input("-->"))
            if button == 4:
                self.battle_menu(battle)
            else:
                move = button
                ##select target
                targets = self.moves[move].select_target(self, battle)
                battle.moves_to_use.append([self, self.moves[move], targets])
        #[user, move_to_use, targets]
        ##self.moves[move - 1].use(self, battle, targets)

    def take_damage(self, damage):
        if damage > 0:
            damage_percentage = damage / self.data['hp']  *100
        else:
            damage_percentage = 0
        self.data['hp'] -= damage
        print(f"{self.player.name}'s {self.name} took {damage} of damage ! ({damage_percentage} %)")

    def receive_move(self, move, user, target_modifier):
        ##check for opponent battle side (light screen, hazards ...)
        ##check for pokemon (ability, protect, clone ...)
        ##apply damage or effect
        damage_class = move.base_data.damage_class.name
        base_power = move.base_data.power
        A = 1
        D = 1
        if damage_class == "physical":
            A = user.data['stats']['atk']
            D = self.data['stats']['def']

        elif damage_class == "special":
            A = user.data['stats']['spatk']
            D = self.data['stats']['spdef']

        crit_rate = move.base_data.meta.crit_rate + user.crit_rate
        if crit_rate == 0:
            crit_proba = 1/24
        elif crit_rate == 1:
            crit_proba = 1/8
        elif crit_rate == 2:
            crit_proba = 1/2
        elif crit_rate > 2:
            crit_proba = 1.0
        if (random.random() < crit_proba):
            crit = 1.5
        else:
            crit = 1.0
        roll = random.randrange(85, 100)/100
        stab = 1.0
        for user_type in user.base_data.types:
            if user_type.type.name == move.base_data.type.name:
                ##if user.ability == 'adaptability':
                    ##stab = 2
                ##else:
                    ##stab = 1.5
                stab = 1.5
        type_effectiveness = 1.0
        type_data = pokebase.type_(move.base_data.type.name)
        for target_type in self.base_data.types:
            for t in type_data.damage_relations.double_damage_from:
                if t['name'] == target_type.type.name:
                    type_effectiveness *= 2.0
            for t in type_data.damage_relations.half_damage_from:
                if t['name'] == target_type.type.name:
                    type_effectiveness *= 0.5
            for t in type_data.damage_relations.no_damage_from:
                if t['name'] == target_type.type.name:
                    type_effectiveness *= 0.0

        if type_effectiveness == 4.0:
            print("It's hyper effective !")

        if type_effectiveness == 2.0:
            print("It's very effective !")

        if type_effectiveness == 0.5:
            print("It's not very effective ...")

        if type_effectiveness == 0.25:
            print("It's barely effective ...")

        if type_effectiveness == 0.0:
            print("It's not effective at all ...")

        #Burn Modifier
        if type_effectiveness != 0.0:
            if damage_class != "status":
                damage = ((((user.data['level']*2/5) +2) * base_power * A / D) / 50 + 2) * crit * roll * stab * type_effectiveness
                self.take_damage(damage)



