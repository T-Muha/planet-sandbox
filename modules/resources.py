import pyglet
from pyglet import resource

pyglet.resource.path = ['resources']
pyglet.resource.reindex()

backgroundImage = pyglet.resource.image('background.png')
bluePlanetImage = pyglet.resource.image('blue_planet.png')
blackHoleImage = pyglet.resource.image('black_hole.png')
orbitSampleImage = pyglet.resource.image('orbit_sample.png')
cursorImage = pyglet.resource.image('cursor.png')
cursorAltImage = pyglet.resource.image('cursor_alt.png')
pauseImage = pyglet.resource.image('pause.png')
resumeImage = pyglet.resource.image('resume.png')

def CenterImage(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

CenterImage(bluePlanetImage)
CenterImage(orbitSampleImage)