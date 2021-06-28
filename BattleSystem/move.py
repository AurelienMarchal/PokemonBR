import pokebase
import random

class Move(object):
    def __init__(self, data):
        if data is None:
            self.blank = True
        else:
            self.blank = False
            self.data = data
            self.base_data = pokebase.move(self.data['name'])
            self.disabled = False

    def use(self, user, battle, targets):
        if len(targets) == 0:
            print("the move fails")
        else:
            target_modifier = 1
            if len(targets) > 1:
                target_modifier = 0.75
            for target in targets:
                if target == user:
                    print(user.name, "uses", self.base_data.name, "on himself")
                else:
                    print(user.name, "uses", self.base_data.name, "on", target.name)
                target.receive_move(self, user, target_modifier)
        move_category = self.base_data.meta.category.name
        if move_category == "damage":
            pass



        ##base_power = self.data.power
        ##if len(targets) > 1:
        ##    target_modifier = 0.75
        ##else:
        ##    target_modifier = 1.0
        ##crit_rate = self.data.meta.crit_rate + user.crit_rate
        ##if crit_rate == 0:
        ##    crit_proba = 1/24
        ##elif crit_rate == 1:
        ##    crit_proba = 1/8
        ##elif crit_rate == 2:
        ##    crit_proba = 1/2
        ##else:
        ##    crit_proba = 1.0
        ##crit = (random.random() < crit_proba) * 1.5
        ##roll = random.randrange(85, 100)
        ##stab = 1.0
        ##for user_type in user.data.types:
        ##    if user_type.type.name == self.data.type.name:
        ##        if user.ability == 'adaptability':
        ##            stab = 2
        ##        else:
        ##            stab = 1.5

    def select_target(self, user, battle):
        move_target = self.base_data.target.name
        ID = pokebase.move_target(move_target).id
        choose_targets = [] ##list of tuple : (target,is_ally)
        targets = []
        if ID == 1:
            pass
        elif ID == 2:
            pass
        elif ID == 3:
            for ally_pokemon_ in user.player.side.battling:
                if ally_pokemon_ != 0:
                    if ally_pokemon_ != user:
                        choose_targets.append((ally_pokemon_, True))

        elif ID == 4:
            targets.append(user.player.side)

        elif ID == 5:
            for ally_pokemon_ in user.player.side.battling:
                if ally_pokemon_ != 0:
                    choose_targets.append((ally_pokemon_, True))

        elif ID == 6:
            targets.append(user.player.opponent_side)

        elif ID == 7:
            targets.append(user)

        elif ID == 8:
            possible_targets = []
            for opponent_pokemon_ in user.player.opponent_side.battling:
                if opponent_pokemon_ != 0:
                    possible_targets.append(opponent_pokemon_)
            targets.append(random.choice(possible_targets))

        elif ID == 9:
            for opponent_pokemon_ in user.player.opponent_side.battling:
                if opponent_pokemon_ != 0:
                    targets.append(opponent_pokemon_)
            for ally_pokemon_ in user.player.side.battling:
                if ally_pokemon_ != 0:
                    if ally_pokemon_ != user:
                        targets.append(ally_pokemon_)

        elif ID == 10:
            for opponent_pokemon_ in user.player.opponent_side.battling:
                if opponent_pokemon_ != 0:
                    choose_targets.append((opponent_pokemon_, False))
            for ally_pokemon_ in user.player.side.battling:
                if ally_pokemon_ != 0:
                    if ally_pokemon_ != user:
                        choose_targets.append((ally_pokemon_, True))

        elif ID == 11:
            for opponent_pokemon_ in user.player.opponent_side.battling:
                if opponent_pokemon_ != 0:
                    targets.append(opponent_pokemon_)

        elif ID == 12:
            targets.append(battle)

        elif ID == 13:
            for ally_pokemon_ in user.player.side.battling:
                if ally_pokemon_ != 0:
                    targets.append(ally_pokemon_)

        elif ID == 14:
            for opponent_pokemon_ in user.player.opponent_side.battling:
                if opponent_pokemon_ != 0:
                    targets.append(opponent_pokemon_)
            for ally_pokemon_ in user.player.side.battling:
                if ally_pokemon_ != 0:
                    targets.append(ally_pokemon_)

        else:
            print("Move target is not correct")

        if len(choose_targets) == 1:
            targets.append(choose_targets[0][0])

        elif len(choose_targets) > 1:
            if user.player.trainer_type == 0 or user.player.trainer_type == 1:
                target_to_choose = []
                for i in range(len(choose_targets)):
                    if not choose_targets[i][1]:
                        target_to_choose.append(i)
                if len(target_to_choose) == 0:
                    for i in range(len(choose_targets)):
                        target_to_choose.append(i)
                targets.append(choose_targets[random.choice(target_to_choose)][0])

            if user.player.trainer_type == 2:
                print("choose a target : ")
                for i in range(len(choose_targets)):
                    print("--", i, end=' ')
                    if choose_targets[i][1]:
                        print("ally", end=' ')
                    if not choose_targets[i][1]:
                        print("opponent", end=' ')
                    print(choose_targets[i][0].name)
                print("--4 to cancel")
                button = int(input("-->"))
                if button == 4:
                    user.move_menu(battle)
                else:
                    targets.append(choose_targets[button][0])

        return targets