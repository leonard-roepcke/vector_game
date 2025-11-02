class VectorHandler:
    def __init__(self,pygame_app):
        self.pygame_app = pygame_app
        self.vectors = []
    
    def update_vectors(self):
        dt = self.pygame_app.dt
        for vector in self.vectors:
            vector.update(dt)
            vector.draw()
    
    def draw_vector(self, pos):
        self.pygame_app.draw_vector(pos)
    
    def add_vector(self, pos):
        self.vectors.append(Vector(self,pos))

class Vector:
    def __init__(self, handler, pos):
        self.handler = handler
        self.pos = pos
        self.scaled_pos = (0,0)
        self.life = 0
        self.size = 0

    def update(self, dt):
        self.life += dt
        if self.life <=2000:
            self.size += dt/1000
            if self.size >1: self.size=1
        self.scaled_pos = (self.pos[0]*self.size,self.pos[1]*self.size)

    def draw(self):
        self.handler.draw_vector(self.scaled_pos)