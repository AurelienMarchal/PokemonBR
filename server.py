import channels
#import BattleSystem.battle as battle
#import BattleSystem.test as test


#STARTING SERVER

rooms_to_create = ['room_Overworld', 'room_House1']

for r in rooms_to_create:
    channels.rooms.append(channels.room.Room(r))

for r in channels.rooms:
    r.start()
    #r.join()
    pass

#battle_size = 1 ##1 pokemon vs 1 pokemon

#battle = battle.Battle([test.Team0], [test.Team1], battle_size)
#battle.start() #Test


channels.sgn.server("", 5000)
