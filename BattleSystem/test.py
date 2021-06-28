#import pokebase


# TRAINER TYPE 0: WILD 1: NPC 2: PLAYER
# STATUS 0: Nothing, 1: Para, 2: Sleep, 3: Burn, 4: Freeze, 5: Poison, 6: Toxic
Team0 = {'trainer_type': 2,'player_name': "Michel", 'client_id': 0,'pokemons':[{
    'id': 1,
    'form': 0,
    'nickname': 'Bulbizarre',
    'owner': None,
    'shiny': False,
    'gender': False,
    'level': 50,
    'xp': 0,
    'hapiness': 255,
    'item': None,
    'ability': 'overgrow',
    'status': 0,
    'hp': 120,
    'stats': {'hp': 120, 'atk': 69, 'def': 69, 'spatk': 85, 'spdef': 85, 'speed':65},
    'moves': [  {'name': 'tackle','pp_max': 10, 'pp': 10},
                {'name': 'earthquake','pp_max': 10, 'pp': 10},
                {'name': 'extreme-speed','pp_max': 10, 'pp': 10},
                None],
    'ev': {'hp': 0, 'atk': 0, 'def': 0, 'spatk': 0, 'spdef': 0, 'speed': 0},
    'iv': {'hp': 31, 'atk': 31, 'def': 31, 'spatk': 31, 'spdef': 31, 'speed': 31}},
    {
    'id': 7,
    'form': 0,
    'nickname': 'Carapuce',
    'owner': None,
    'shiny': False,
    'gender': False,
    'level': 50,
    'xp': 0,
    'hapiness': 255,
    'item': None,
    'ability': 'torrent',
    'status': 0,
    'hp': 10,
    'stats': {'hp': 10, 'atk': 10, 'def': 10, 'spatk': 10, 'spdef': 10, 'speed': 20},
    'moves': [  {'name': 'tackle','pp_max': 10, 'pp': 10},
                {'name': 'rain-dance','pp_max': 10, 'pp': 10},
                {'name': 'bullet-punch','pp_max': 10, 'pp': 10},
                None],
    'ev': {'hp': 0, 'atk': 0, 'def': 0, 'spatk': 0, 'spdef': 0, 'speed': 0},
    'iv': {'hp': 31, 'atk': 31, 'def': 31, 'spatk': 31, 'spdef': 31, 'speed': 31}}
    ]
}

Team1 = {'trainer_type': 1,'player_name': "Michel_NPC", 'client_id': -1, 'pokemons':[{
    'id': 4,
    'form': 0,
    'nickname': 'Salameche',
    'owner': None,
    'shiny': False,
    'gender': False,
    'level': 50,
    'xp': 0,
    'hapiness': 255,
    'item': None,
    'ability': 'overgrow',
    'status': 0,
    'hp': 114,
    'stats': {'hp': 114, 'atk': 72, 'def': 63, 'spatk': 80, 'spdef': 70, 'speed': 85},
    'moves': [  {'name': 'tackle','pp_max': 10, 'pp': 10},
                None,
                None,
                None],
    'ev': {'hp': 0, 'atk': 0, 'def': 0, 'spatk': 0, 'spdef': 0, 'speed': 0},
    'iv': {'hp': 31, 'atk': 31, 'def': 31, 'spatk': 31, 'spdef': 31, 'speed': 31}},
    {
    'id': 14,
    'form': 0,
    'nickname': 'Roocool',
    'owner': None,
    'shiny': False,
    'gender': False,
    'level': 50,
    'xp': 0,
    'hapiness': 255,
    'item': None,
    'ability': 'torrent',
    'status': 0,
    'hp': 10,
    'stats': {'hp': 10, 'atk': 10, 'def': 10, 'spatk': 10, 'spdef': 10, 'speed': 40},
    'moves': [  {'name': 'tackle','pp_max': 10, 'pp': 10},
                {'name': 'rain-dance','pp_max': 10, 'pp': 10},
                {'name': 'bullet-punch','pp_max': 10, 'pp': 10},
                None],
    'ev': {'hp': 0, 'atk': 0, 'def': 0, 'spatk': 0, 'spdef': 0, 'speed': 0},
    'iv': {'hp': 31, 'atk': 31, 'def': 31, 'spatk': 31, 'spdef': 31, 'speed': 31}}
    ]
}

#Team0_data = json.loads(Team0_data_json)
#Team1_data = json.loads(Team1_data_json)
