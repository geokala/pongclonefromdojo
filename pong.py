
box = Rect((0,0), (20,40))
colour = (200,0,0)

def draw():
    screen.clear()
    screen.draw.filled_rect(box, colour)

def update():
    pass 

def on_key_down(key):
    if key == keys.UP:
        box.top -= 2
    if key == keys.DOWN:
        box.top += 2
