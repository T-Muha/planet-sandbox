import pyglet
from pyglet import resource
from modules import resources

class Planet(pyglet.sprite.Sprite):
    def __init__(self, mass, vxi=0, vyi=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speedUp = 50000
        self.vx = vxi
        self.vy = vyi
        self.ax = 0
        self.ay = 0
        self.fx = 0
        self.fy = 0
        self.mass = mass

    def update(self, dt):
        self.ax = self.ax + self.fx / self.mass
        self.ay = self.ay + self.fy / self.mass
        self.vx = self.vx + self.ax * dt * self.speedUp
        self.vy = self.vy + self.ay * dt * self.speedUp
        self.x = self.x + self.vx * dt * self.speedUp
        self.y = self.y + self.vy * dt * self.speedUp
        self.fx = 0
        self.fy = 0
        self.ax = 0
        self.ay = 0

    def update_force(self, fx, fy):
        self.fx += fx
        self.fy += fy