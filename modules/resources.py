import pyglet
from pyglet import resource

pyglet.resource.path = ['resources']
pyglet.resource.reindex()

backgroundImage = pyglet.resource.image('background.png')
cursorImage = pyglet.resource.image('cursor.png')
cursorAltImage = pyglet.resource.image('cursor_alt.png')
pauseImage = pyglet.resource.image('pause.png')
resumeImage = pyglet.resource.image('resume.png')

moonImage = pyglet.resource.image('moon.png')
planetImage = pyglet.resource.image('planet.png')
starImage = pyglet.resource.image('star.png')
holeImage = pyglet.resource.image('hole.png')

sizeImage = pyglet.resource.image('size.png')
noImage = pyglet.resource.image('noImage.png')

moonSelectedImage = pyglet.resource.image('moon_selected.png')
planetSelectedImage = pyglet.resource.image('planet_selected.png')
starSelectedImage = pyglet.resource.image('star_selected.png')
holeSelectedImage = pyglet.resource.image('hole_selected.png')

def CenterImage(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2


CenterImage(moonImage)
CenterImage(planetImage)
CenterImage(starImage)
CenterImage(holeImage)