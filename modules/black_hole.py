import pyglet
from pyglet import resource

#simple implementation of a black hole, does not account for any real calculations, Schwartzchild radii, mass, etc

class BlackHole(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.fx = 0
        self.fy = 0
        self.mass = 50 * 1.989*10**30

    def update(self, dt):
        self.ax = self.ax + self.fx / self.mass * dt
        self.ay = self.ay + self.fy / self.mass * dt
        self.vx = self.vx + self.ax * dt
        self.vy = self.vy + self.ay * dt
        self.x = self.x + self.vx * dt
        self.y = self.y + self.vy  *dt

    def update_force(self, fx, fy):
        self.fx += fx
        self.fy += fy

    def C_O_N_S_U_M_E(planet):
        self.mass += planet.mass
        #also add radius increase