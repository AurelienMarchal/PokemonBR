##import pygame
import random
import pokebase
from threading import Thread
from BattleSystem.side import Side

class Battle(Thread):
    WAITING_TIME = 0.01
    def __init__(self, teamsSide1, teamsSide2, size):
        Thread.__init__(self)
        self.name = "the field"
        self.side1 = Side(teamsSide1, size, 1)
        self.side2 = Side(teamsSide2, size,  2)
        self.side1.opponent_side = self.side2
        self.side2.opponent_side = self.side1
        for player in self.side1.players:
            player.side = self.side1
            player.opponent_side = self.side2
        for player in self.side2.players:
            player.side = self.side2
            player.opponent_side = self.side1
        self.size = size
        self.battle_over = True
        self.moves_to_use = []
        self.num_turn = 0
        self.weather = 0
        self.terrain = 0
        if self.size < self.side1.size or self.size < self.side2.size:
            print("The battle can't be started because the size of the teams are too big")

    def receive_move(self, move, user, target_modifier):
        pass

    def number_pokemon_alive(self):
        p1 = 0
        p2 = 0
        for player in self.side1.players:
            for pokemon_ in player.team:
                if pokemon_.data['hp'] > 0:
                    p1 += 1
        for player in self.side2.players:
            for pokemon_ in player.team:
                if pokemon_.data['hp'] > 0:
                    p2 += 1
        print("Team1 has", p1, "pokemon(s) alive")
        print("Team2 has", p2, "pokemon(s) alive")
        if p1 == 0 or p2 == 0:
            self.battle_over = True

    def run(self):
        self.battle_start()

        while not self.battle_over:
            self.num_turn += 1
            print("Turn", self.num_turn)
            for pokemon_ in self.side1.battling:
                if pokemon_ != 0:
                    pokemon_.battle_menu(self)
            for pokemon_ in self.side2.battling:
                if pokemon_ != 0:
                    pokemon_.battle_menu(self)
            self.turn_start()

        self.battle_end()

    def battle_start(self):
        self.battle_over = False
        print("starting battle ...")
        print("the battle is a", self.size, "vs", self.size)
        print("opposing", end=' ')
        for player in self.side1.players:
            print(player.name, end=', ')
        print("vs", end=' ')
        for player in self.side2.players:
            print(player.name, end=', ')
        print("")
        self.number_pokemon_alive()
        self.side1.send()
        self.side2.send()
        print("--------------------")

    def battle_end(self):
        pass

    def turn_start(self):
        print("starting turn ...")

        # [user, move_to_use, targets]
        ##sorting move to use in order
        for i in range(1, len(self.moves_to_use)):
            for j in range(len(self.moves_to_use) - i):
                if self.moves_to_use[j][1].base_data.priority > self.moves_to_use[j + 1][1].base_data.priority:
                    aux = self.moves_to_use[j + 1]
                    self.moves_to_use[j + 1] = self.moves_to_use[j]
                    self.moves_to_use[j] = aux
                elif self.moves_to_use[j][1].base_data.priority == self.moves_to_use[j + 1][1].base_data.priority:
                    if self.moves_to_use[j][0].data['stats']['speed'] > self.moves_to_use[j + 1][0].data['stats']['speed']:
                        aux = self.moves_to_use[j + 1]
                        self.moves_to_use[j + 1] = self.moves_to_use[j]
                        self.moves_to_use[j] = aux

        next_moves_to_use = []
        while len(self.moves_to_use) != 0:
            next_moves_to_use.append(self.moves_to_use[-1])
            self.moves_to_use.pop()
            while len(next_moves_to_use) != 0:
                move = random.randint(0, len(next_moves_to_use)-1)
                next_moves_to_use[move][1].use(next_moves_to_use[move][0], self, next_moves_to_use[move][2])
                next_moves_to_use.pop(move)

    def turn_end(self):
        pass
