import suspengine as sgn
import json
import room
from player import Player

iden = 0
rooms = []

def verify_id(client, _id):
    assert sgn.callvariable('id', client) == _id, f"No client with id {_id}"

def find_room(room_id):
    global rooms
    for r in rooms:
        if r.room_id == room_id:
            return r
    return None


@sgn.channel("connect")
def connect(c, addr):
    global iden
    sgn.savevariable('id', iden, c)
    sgn.emit("connect", {'id': int(iden)}, c)
    player = Player(iden)
    sgn.savevariable('player', player, c)
    iden += 1


@sgn.channel("disconnect")
def disconnect(c, addr):
    print("Client with id :", sgn.callvariable('id', c), "disconnected from the server")


@sgn.channel("message")
def message(c, addr, data):
    pass


@sgn.channel("movement")
def movement(c, addr, data):
    data = json.loads(data)
    verify_id(c, data[id])
    print("Receiving movement :", data)
    player = sgn.callvariable('player', c)
    player.update_movement()


@sgn.channel("leave_room")
def leave_room(c, addr, data):
    data = json.loads(data)
    verify_id(c, data[id])
    r = find_room(data['room'])
    player = sgn.callvariable('player', c)
    print("Player ", player, "is leaving", data['room'])
    if r is not None:
        r.remove_player(player)

@sgn.channel("enter_room")
def enter_room(c, addr, data):
    data = json.loads(data)
    verify_id(c, data[id])
    r = find_room(data['room'])
    player = sgn.callvariable('player', c)
    print("Player", player, "is entering", data['room'])
    if r is not None:
        r.add_player(player)

"""
@sgn.channel("update_data")
def update_data(c, addr, data):
    data = json.loads(data)
    verify_id(c, data[id])

    for _item in data:
        if _item != 'id':
            sgn.savevariable('id', _item, c)
    
"""
@sgn.channel("battle")
def battle(c, addr, data):
        pass
