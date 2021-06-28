import suspengine as sgn
import json
import room


iden = 0
rooms = []

#lol
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
    iden += 1


@sgn.channel("disconnect")
def disconnect(c, addr):
    print("Client with id :", sgn.callvariable('id', c), "disconnected from the server")


@sgn.channel("message")
def message(c, addr, data):
    pass


@sgn.channel("movement")
def movement(c, addr, data):
    #print("Receiving movement :", data)
    data = json.loads(data)
    r = find_room(data['room'])
    if r is not None:
        r.movement(data)


@sgn.channel("change_room")
def change_room(c, addr, data):
    data = json.loads(data)
    r_old = find_room(data['old_room'])
    print("Player with id", data['id'], "is leaving", data['old_room'])
    if r_old is not None:
        r_old.remove_player(data['id'])

@sgn.channel("battle")
def battle(c, addr, data):
        pass
