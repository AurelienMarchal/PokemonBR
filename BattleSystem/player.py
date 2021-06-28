import pokebase
from BattleSystem.pokemon import Pokemon

class Player(object):
    def __init__(self, id_, name, trainer_type, pokemons):
        self.ID = id_
        self.side = None
        self.opponent_side = None
        self.name = name
        self.trainer_type = trainer_type # 0: WILD 1: NPC 2: PLAYER
        self.team = []
        for data in pokemons:
            self.team.append(Pokemon(data, self))
        self.battling_pokemons = []

    def switch(self):
        pass

    def send(self, num):
        print(self.name, "is sending", self.team[num].name)
        self.battling_pokemons.append(num)
        return self.team[num]
