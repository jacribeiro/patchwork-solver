class Player:
    def __init__(self, color: int):
        self._color: int = color
        self._buttons: int = 5
        self._time: int = 0
        self._is_above: bool = False

    def get_time(self) -> int:
        return self._time
    
    def is_above(self) -> bool:
        return self._is_above

class PatchworkGame:
    def __init__(self):
        self.next_player = 0

    def calculate_next_player(player_0: Player, player_1: Player) -> Player:
        if player_0.get_time() == player_1.get_time():
            if player_0.is_above():
                return player_0
            else: 
                return player_1
        elif player_0.get_time() > player_1.get_time():
            return player_1
        else:
            return player_0
        
class Piece:
    def __init__(self, button_cost, time_cost, gainable_buttons=0):
        self.button_cost = button_cost
        self.time_cost = time_cost
        self.gainable_buttons = gainable_buttons