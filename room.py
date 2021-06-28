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
                self.emit_to_players_in_room("room_data", {'players': self.players})
                time.sleep(self.WAITING_TIME)

    def emit_to_players_in_room(self, channel, data):
        for player in self.players:
            try:
                c = sgn.callvariablelist('id', player['id'])[0]
                sgn.emit(channel, data, c)
            except IndexError:
                pass

    def movement(self, data):
        for p in self.players:
            if p['id'] == data['id']:
                self.players.remove(p)
                self.players.append(data)
                return True
        self.add_player(data)

    def add_player(self, data):
        self.players.append(data)

    def remove_player(self, id_):
        for p in self.players:
            if p['id'] == id_:
                self.players.remove(p)
                self.emit_to_players_in_room("room_data_remove_player", {'id' : id_})
                return(p)
