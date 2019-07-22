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

su = 1.989*10**30
au = 14959787070
heavenlyBodies = []

#planetOne = planet.Planet(img=resources.bluePlanetImage, x=400, y=400, batch=mainBatch, mass=0.000954588*su, vyi=-20)
#planetTwo = planet.Planet(img=resources.bluePlanetImage, x=900, y=500, batch=mainBatch, mass=0.000954588*su, vyi=-20)
#planetThree = planet.Planet(img=resources.bluePlanetImage, x=1100, y=300, batch=mainBatch, mass=0.000954588*su, vyi=20)

#holeOne = black_hole.BlackHole(img=resources.blackHoleImage, x=640, y=360, batch=mainBatch, mass=4.0*su)
#holeOne.scale = 0.1
#heavenlyBodies.append(holeOne)

for i in range(50):
    newPlanet = planet.Planet(img=resources.bluePlanetImage, x=random.randrange(1280), y=random.randrange(720), batch=mainBatch, mass=.989, vxi=random.randrange(-10,10), vyi=random.randrange(-10,10))
    heavenlyBodies.append(newPlanet)
    newPlanet.scale = 0.1


##sun = planet.Planet(img=resources.bluePlanetImage, x=640, y=360, batch=mainBatch, mass=su)
##earth = planet.Planet(img=resources.bluePlanetImage, x=800, y=360, batch=mainBatch, mass=0.000003003*su, vyi=30000 / au * 160 * 3.12) # * 3.12 arises from error. Need to find source
##heavenlyBodies.append(sun)
##heavenlyBodies.append(earth)
##sun.scale = 0.5
##earth.scale = 0.5

#orbitSample = pyglet.sprite.Sprite(img=resources.orbitSampleImage, x=640, y=360, batch=mainBatch)
#orbitSample.scale = 10


def update(dt):
    global au, paused
    if not paused:
        for index, heavenlyBody in enumerate(heavenlyBodies):
            for i in range(index+1,len(heavenlyBodies)):
                #print(index)
                #print(i)
                secondBody = heavenlyBodies[i]
                oneTwoX = (secondBody.x-heavenlyBody.x)
                oneTwoY = (secondBody.y-heavenlyBody.y)
                distance = math.sqrt(oneTwoX**2 + oneTwoY**2)
                fgPrime = 6.67408*10**-11 / au**3 * 160**3 * heavenlyBody.mass * secondBody.mass / distance**3
                fgx = fgPrime * oneTwoX
                fgy = fgPrime * oneTwoY
                #print(fgy)
                heavenlyBody.update_force(fgx, fgy)
                secondBody.update_force(-1*fgx, -1*fgy)

        #print('')

        for heavenlyBody in heavenlyBodies:
            heavenlyBody.update(dt)

def deletePlanet(planet):
    global heavenlyBodies
    heavenlyBodies.remove(planet)


pyglet.clock.schedule_interval(update, 1/60.0)

@MainWindow.event
def on_mouse_press(x, y, button, modifiers):
    global paused
    if x < 238 and y < 169:
        if not paused:
            #pyglet.clock.unschedule(update)
            pauseButton.image = resources.resumeImage
            paused = True
        else:
            #pyglet.clock.schedule_interval(update, 1/60.0)
            pauseButton.image = resources.pauseImage
            paused = False
    else:
        MainWindow.set_mouse_cursor(cursorAlt)
        newBody = planet.Planet(img=resources.bluePlanetImage, x=x, y=y, batch=mainBatch, mass=su)
        newBody.scale = 0.1
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