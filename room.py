from threading import Thread
import time
import suspengine as sgn


class Room(Thread):
    WAITING_TIME = 0.01
    def __init__(self, room_id):
        Thread.__init__(self)

        self.room_id = room_id
        self.players = []

    def run(self):
        while True:
            if len(self.players) > 0:
                #A modif
                #self.emit_to_players_in_room("room_data", {'players': self.players})
                time.sleep(self.WAITING_TIME)

    def emit_to_players_in_room(self, channel, data):
        for player in self.players:
            try:
                c = sgn.callvariablelist('id', player.id_)[0]
                sgn.emit(channel, data, c)
            except IndexError:
                pass

    def add_player(self, player):
        self.players.append(player)
        player.set_room(self)

    def remove_player(self, player):
        self.players.remove(player)
        player.set_room(None)
        self.emit_to_players_in_room("room_data_remove_player", {'id' : player.id_})

