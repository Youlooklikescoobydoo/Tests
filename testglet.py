import pyglet

batch = pyglet.graphics.Batch()
character = pyglet.graphics.Group(order=0)
window = pyglet.window.Window()

character = pyglet.sprite.Sprite(pyglet.shapes.Rectangle(200, 200, 50, 50, color=(30, 255, 255, 255), batch=batch, group=character),
									pyglet.shapes.Rectangle(200, 200, 50,40, color=(255,0,0), batch=batch, group=character))

@window.event
def on_draw():
    window.clear()
    batch.draw()

pyglet.app.run()
