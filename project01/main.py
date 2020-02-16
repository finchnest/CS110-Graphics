import random
import time
from tkinter import Canvas, Tk

import helpers

from project01.utilities import *

gui = Tk()
gui.title('My Terrarium')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
canvas = Canvas(gui, width=window_width, height=window_height, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################
MOUSE_CLICK = '<Button-1>'
canvas.create_text(
    (window_width / 10, window_height / 10),
    text='Click anywhere add a creature',
    font=("Purisa", 12)
)

helpers.make_creature(canvas, (random.uniform(80, window_width), random.uniform(80, window_height * 0.75)),
                      width=random.uniform(50, 100), primary_color='#aebb83', secondary_color='#227876', tag="panda1")
helpers.make_creature(canvas, (random.uniform(80, window_width), random.uniform(80, window_height * 0.75)),
                      width=random.uniform(50, 100), primary_color='red', secondary_color='#227876', tag="panda2")
helpers.make_creature(canvas, (random.uniform(80, window_width), random.uniform(80, window_height * 0.75)),
                      width=random.uniform(50, 100), primary_color='green', secondary_color='#227876', tag="panda3")
helpers.make_creature(canvas, (random.uniform(80, window_width), random.uniform(80, window_height * 0.75)),
                      width=random.uniform(50, 100), primary_color='#aebb83', secondary_color='#227876', tag="panda4")
helpers.make_creature(canvas, (random.uniform(80, window_width), random.uniform(80, window_height * 0.75)),
                      width=random.uniform(40, 120), primary_color='brown', secondary_color='#227876', tag="panda5")

helpers.make_landscape_object(canvas, (window_width, window_height), size=100, tag="landscape")

creature_with_speed = {"panda1": 3, "panda2": 3, "panda3": 3, "panda4": 3, "panda5": 3}

speed = 0.05


def updater(last):
    return "panda" + str(last + 1)


def pass_data(event):
    last_str = updater(len(list(creature_with_speed.keys())))

    helpers.make_creature(canvas, (event.x, event.y),
                          width=random.uniform(40, 120), primary_color=random.choice(['brown', 'red', 'green', 'pink']),
                          secondary_color=random.choice(['brown', 'red', 'green', 'pink']),
                          tag=last_str)

    creature_with_speed[last_str] = 3


canvas.bind(MOUSE_CLICK, pass_data)

while True:
    time.sleep(speed)

    temp_list = list(creature_with_speed.keys())
    for itemy in temp_list:
        if temp_list.index(itemy) % 2 == 0:
            update_position(canvas, itemy, creature_with_speed.get(itemy), y=random.choice([3, -3]))

        else:
            update_position(canvas, itemy, creature_with_speed.get(itemy), y=0)

    gui.update()

    for key, value in creature_with_speed.items():
        temp = canvas.coords(key)
        if temp[0] > window_width - 50 or temp[0] < 0:
            creature_with_speed[key] = -1 * value + random.choice([1, -1])

    speed /= 3

########################## YOUR CODE ABOVE THIS LINE ##############################

# makes sure the canvas keeps running:
canvas.mainloop()
