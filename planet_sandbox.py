import math
import random
import pyglet
from pyglet import resource
from pyglet.window import key
from modules import resources, planet, black_hole

MainWindow = pyglet.window.Window(1280, 720)
mainBatch = pyglet.graphics.Batch()

cursor = pyglet.window.ImageMouseCursor(resources.cursorImage, 8, 8)
cursorAlt = pyglet.window.ImageMouseCursor(resources.cursorAltImage, 8, 8)
MainWindow.set_mouse_cursor(cursor)

background = pyglet.sprite.Sprite(img=resources.backgroundImage, x=0, y=0, batch=mainBatch)
background.scale_x = 12.8
background.scale_y = 7.2

pauseButton = pyglet.sprite.Sprite(img=resources.pauseImage, x=0, y=0, batch=mainBatch)
paused = False
pauseButton.scale = 0.5

sizeMenu = pyglet.sprite.Sprite(img=resources.sizeImage, x = 120, y = 0, batch=mainBatch)
showSizeMenu = False
sizeMenu.scale = 1.441

su = 1.989*10**30
au = 14959787070
heavenlyBodies = []
selector = 'planet'

#for i in range(50):
#    newPlanet = planet.Planet(img=resources.bluePlanetImage, x=random.randrange(1280), y=random.randrange(720), batch=mainBatch, mass=.989, vxi=random.randrange(-10,10), vyi=random.randrange(-10,10))
#    heavenlyBodies.append(newPlanet)
#    newPlanet.scale = 0.1

sun = planet.Planet(img=resources.starImage, x=640, y=360, batch=mainBatch, mass=su)
earth = planet.Planet(img=resources.planetImage, x=800, y=360, batch=mainBatch, mass=0.000003003*su, vyi=30000 / au * 160 * 3.12) # * 3.12 arises from error
heavenlyBodies.append(sun)
heavenlyBodies.append(earth)

def update(dt):
    global au, paused
    if not paused:
        for index, heavenlyBody in enumerate(heavenlyBodies):
            for i in range(index+1,len(heavenlyBodies)):
                secondBody = heavenlyBodies[i]
                oneTwoX = (secondBody.x-heavenlyBody.x)
                oneTwoY = (secondBody.y-heavenlyBody.y)
                distance = math.sqrt(oneTwoX**2 + oneTwoY**2)
                fgPrime = 6.67408*10**-11 / au**3 * 160**3 * heavenlyBody.mass * secondBody.mass / distance**3
                fgx = fgPrime * oneTwoX
                fgy = fgPrime * oneTwoY
                heavenlyBody.update_force(fgx, fgy)
                secondBody.update_force(-1*fgx, -1*fgy)

        for heavenlyBody in heavenlyBodies:
            heavenlyBody.update(dt)

def deletePlanet(planet):
    global heavenlyBodies
    heavenlyBodies.remove(planet)


pyglet.clock.schedule_interval(update, 1/60.0)

@MainWindow.event
def on_mouse_press(x, y, button, modifiers):
    global paused
    global selector
    if x < 119 and y < 135:
        if not paused:
            pauseButton.image = resources.resumeImage
            paused = True
        else:
            pauseButton.image = resources.pauseImage
            paused = False
            for body in tempBodies:
                heavenlyBodies.append(body)
            sizeMenu.image = resources.noImage
    elif x > 119 and x < 374 and y > 0 and y < 85:
        if math.sqrt((x - 152)**2 + (y - 42)**2) < 5.5:
            selector = 'moon'
        if math.sqrt((x - 198)**2 + (y - 42)**2) < 17.5:
            selector = 'planet'
        if math.sqrt((x - 265)**2 + (y - 42)**2) < 27.4:
            selector = 'star'
        if math.sqrt((x - 308)**2 + (y - 42)**2) < 9.5:
            selector = 'hole'
    else:
        MainWindow.set_mouse_cursor(cursorAlt)
        if selector == 'planet':
            newBody = planet.Planet(img=resources.planetImage, x=x, y=y, batch=mainBatch, mass=0.000003003*su)
        elif selector == 'moon':
            newBody = planet.Planet(img=resources.moonImage, x=x, y=y, batch=mainBatch, mass=0.0000000369397*su)
        elif selector == 'star':
            newBody = planet.Planet(img=resources.starImage, x=x, y=y, batch=mainBatch, mass=su)
        else:
            newBody = planet.Planet(img=resources.holeImage, x=x, y=y, batch=mainBatch, mass=su)
        heavenlyBodies.append(newBody)

@MainWindow.event
def on_mouse_release(x, y, button, modifiers):
    MainWindow.set_mouse_cursor(cursor)

@MainWindow.event
def on_draw():
    MainWindow.clear()
    mainBatch.draw()

if __name__ == '__main__':
    pyglet.app.run()