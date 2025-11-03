class VectorHandler:
    def __init__(self,pygame_app, enemy_handler):
        self.pygame_app = pygame_app
        self.enemy_handler = enemy_handler
        self.vectors = []
        self.vectors_to_rm = []
    
    def update_vectors(self):
        dt = self.pygame_app.dt
        enemys = self.enemy_handler.enemys

        for rm_vector in self.vectors_to_rm:
            for vector in self.vectors:
                if rm_vector == vector:
                    self.vectors.remove(vector)
                    break

        self.vectors_to_rm.clear() 
        for vector in self.vectors:
            vector.update(dt)
            vector.draw()
            for enemy in enemys:
                if vector.check_colision(enemy.pos, enemy.size):
                    self.enemy_handler.rm_enemy(enemy)
    
    def draw_vector(self, pos):
        self.pygame_app.draw_vector(pos)
    
    def add_vector(self, pos):
        self.vectors.append(Vector(self,pos))
    
    def rm_vector(self, vector):
        self.vectors_to_rm.append(vector)

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
        if self.life >=6000:
            self.handler.rm_vector(self)

    def draw(self):
        self.handler.draw_vector(self.scaled_pos)
    
    def check_colision(self, pos, radius):
        dist_qrt = (self.scaled_pos[0]-pos[0])**2 + (self.scaled_pos[1]-pos[1])**2
        if dist_qrt < 0.1: return True
        return False