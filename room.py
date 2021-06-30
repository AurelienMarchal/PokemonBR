from threading import Thread
import time
import suspengine as sgn


class Room(Thread):
    WAITING_TIME = 1
    def __init__(self, room_id):
        Thread.__init__(self)

        self.room_id = room_id
        self.players = []

    def run(self):
        while True:
            if len(self.players) > 0:
                #A modif
                #self.emit_to_players_in_room("room_data", {'players': self.players})

                print(self.players)
                time.sleep(self.WAITING_TIME)

    def emit_to_players_in_room(self, channel, data):
        for player in self.players:
            try:
                c = sgn.callvariablelist('id', player.id_)[0]
                sgn.emit(channel, data, c)
            except IndexError:
                pass

    def add_player(self, player):
        # Add player to the list
        self.players.append(player)

        # Modify the player data with this room
        player.set_room(self)

        # Send the new player data to all the players already in the room
        self.emit_to_players_in_room('player_data', player.data_to_dict())

        # Send to the new player the data from all the players already in the room
        self.send_other_players_data(player)

    def remove_player(self, player):
        # Remove player from the list
        self.players.remove(player)

        # Reset room of player
        player.set_room(None)

        # Send to all player left in the room that the player left
        self.emit_to_players_in_room("remove_player", {'id' : player.id_})
        

    def send_other_players_data(self, player_reciever):
        try:
            c = sgn.callvariablelist('id', player_reciever.id_)[0]
        except IndexError:
            pass
        
        for player in self.players:
            if player != player_reciever:
                sgn.emit("player_data", player.data_to_dict(), c)
        