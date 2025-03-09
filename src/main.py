class Player:
    def __init__(self, color: int):
        self.color: int = color
        self.buttons: int = 5
        self.time: int = 0
        self.is_above: bool = False

class PatchworkGame:
    def __init__(self):
        self.next_player = 0

    def calculate_next_player(player_0: Player, player_1: Player) -> Player:
        if player_0.time != player_1.time:
            return min(player_0, player_1, key=lambda p: p.time)
        return player_0 if player_0.is_above() else player_1
        
class Piece:
    def __init__(self, button_cost: int, time_cost: int, income_buttons: int, shape: list[tuple[int]]):
        self.button_cost: int = button_cost
        self.time_cost: int = time_cost
        self.income_buttons: int = income_buttons
        self.shape: list[tuple[int]] = self.normalize(shape)
        self.variations = self.generate_variations(self.shape)
    
    @staticmethod
    def normalize(shape: list[tuple[int]]) -> frozenset:
        min_x = min(x for x, _ in shape)
        min_y = min(y for _, y in shape)
        return frozenset((x - min_x, y - min_y) for x, y in shape)
    
    @staticmethod
    def rotate(shape: list[tuple[int]]) -> frozenset:
        return Piece.normalize([(y, -x) for x, y in shape])
    
    @staticmethod
    def flip(shape: list[tuple[int]]) -> frozenset:
        return Piece.normalize([(-x, y) for x, y in shape])
    
    def generate_variations(self, shape: list[tuple[int]]):
        variations = set()
        for _ in range(4):
            shape = Piece.rotate(shape)
            variations.add(shape)
            variations.add(Piece.flip(shape))
        return variations