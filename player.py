class Player:
    def __init__(
        self, 
        id_, 
        username = "no username", 
        x_grid = 0, 
        y_grid = 0, 
        state = 0, 
        dir = 0,
        sprite = "boy",
        room = None) -> None:

        self.id_ = id_
        self.username = username
        self.x_grid = x_grid
        self.y_grid = y_grid
        self.state = state
        self.dir = dir
        self.sprite = sprite
        self.room = room
    
    def data_to_dict(self):
        return {
            'id': self.id_,
            'username': self.username,
            'x_grid': self.x_grid,
            'y_grid': self.y_grid,
            'state': self.state,
            'dir': self.dir,
            'sprite': self.sprite,
            'room': self.room.room_id
        }
    
    def get_data_from_keys(self, keys):
        d = {'id': self.id_,}
        data_dict = self.data_to_dict()
        for k in keys:
            if k in data_dict:
                d[k] = data_dict[k]
        
        return d
    
    def set_room(self, room):
        self.room = room
    
    def update_movement(self, mvt_data):
        self.x_grid = mvt_data['x_grid']
        self.y_grid = mvt_data['y_grid']
        self.state = mvt_data['state']
        self.dir = mvt_data['dir']

        if self.room is not None:
            self.room.emit_to_players_in_room("movement", 
                self.get_data_from_keys(['x_grid', 'y_grid', 'state', 'dir']))

    
    def leave_room(self):
        self.room.remove_player(self)