from ursina import *
app = Ursina()


e1 = Entity(model='cube', texture='test.jpg',
            origin = (0.2, 0.2, 0.2))

e1.position = (0,0,0)

e1 = Entity(model='cube', texture='test.jpg',
            origin = (0.2, 0.2, 0.2))

e1.position = (1,0,0)

e1 = Entity(model='cube', texture='test.jpg',
            origin = (0.2, 0.2, 0.2))

e1.position = (1,0,1)

e1 = Entity(model='cube', texture='test.jpg',
            origin = (0.2, 0.2, 0.2))

e1.position = (0,0,1)

e2 = Entity(model='pers.obj', texture='tekst_pers.jpg',
            origin = (0, 0, 0))

e2.position = (0.3,0.7,0.3)


def update():
    e2.z += 1 * time.dt * held_keys['w']

def update():
    e2.x += 1 * time.dt * held_keys['d']






















EditorCamera()  # add camera controls for orbiting and moving the camera

app.run()

