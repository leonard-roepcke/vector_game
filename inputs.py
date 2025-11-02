import pygame
class InputHandler:
    def __init__(self, app):
        self.app = app
        self.num_x = None
        self.num_y = None
        self.prefix = 1
        self.lock = True

    def update(self):
        val = self.app.get_key_value()
        if val == None:
            self.lock = False
        if self.lock: return

        if None != self.num_x and None != self.num_y:
            vect = (self.num_x, self.num_y)
            self.num_x = None
            self.num_y = None
            return vect
        

        if val == -1:
            self.prefix = -1
            self.lock = True

        elif self.num_x == None:
            self.num_x = val*self.prefix
            self.lock = True

        elif self.num_y == None:
            self.num_y = val*self.prefix
            self.lock = True
        else:
            LookupError()
            
            
        
        