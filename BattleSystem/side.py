import pokebase
from BattleSystem.player import Player

class Side(object):
    def __init__(self, teams, battle_size, num):
        self.name = "side" + str(num)
        self.opponent_side = None
        self.players = []
        for team in teams:
            self.players.append(Player(team['client_id'], team['player_name'], team['trainer_type'], team['pokemons']))
        self.size = len(self.players)
        self.battling = [0] * battle_size
        self.battle_size = battle_size

    def send(self):
        sent = 0
        for player in self.players:
            self.battling[sent] = player.send(0)
            #sent += 1
            #self.battling[sent] = player.send(1) ##debug

    def receive_move(self, move, user, target_modifier):
        pass
