class Piece:
    def __init__(self, button_cost, time_cost, gainable_buttons=0):
        self.button_cost = button_cost
        self.time_cost = time_cost
        self.gainable_buttons = gainable_buttons