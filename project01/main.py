import time
from tkinter import *

import helpers

from project01.demos.keycodes import *
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
KEY_PRESS = '<Key>'
canvas.create_text(
    (window_width / 10, window_height / 10),
    text='Click anywhere add a creature',
    font=("Purisa", 12)
)

canvas.create_text(
    (window_width / 5, window_height / 7),
    text='You can make the Black/white Panda FLY!!! Use up arrow continously',
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
# controlable
helpers.make_creature(canvas, (window_width / 2, window_height * 0.75),
                      width=random.uniform(40, 120), primary_color='white', secondary_color='black', tag="obj")

helpers.make_landscape_object(canvas, (window_width, window_height), size=100, tag="landscape")

creature_with_speed = {"panda1": 3, "panda2": 3, "panda3": 3, "panda4": 3, "panda5": 3, "obj": [0, 0]}

speed = 0.05


def updater(last):
    return "panda" + str(last + 1)


def pass_data(event):
    last_str = updater(len(list(creature_with_speed.keys())))

    helpers.make_creature(canvas, (event.x, event.y),
                          width=random.uniform(40, 120),
                          primary_color=random.choice(['brown', 'red', 'green', 'pink']),
                          secondary_color=random.choice(['brown', 'red', 'green', 'pink']),
                          tag=last_str)

    creature_with_speed[last_str] = 3


def jumper(event):
    if event.keycode == get_up_keycode() and canvas.coords("obj")[1] > 200:
        creature_with_speed["obj"][1] -= 3
        update_position(canvas, "obj", 0, creature_with_speed["obj"][1])

    if event.keycode == get_down_keycode() and canvas.coords("obj")[1] < 800:
        creature_with_speed["obj"][1] += 3
        update_position(canvas, "obj", 0, creature_with_speed["obj"][1])
    if event.keycode == get_left_keycode() and canvas.coords("obj")[0] > 200:
        creature_with_speed["obj"][0] -= 3
        update_position(canvas, "obj", creature_with_speed["obj"][0], 0)
    if event.keycode == get_right_keycode() and canvas.coords("obj")[0] < 1000:
        creature_with_speed["obj"][0] += 3
        update_position(canvas, "obj", creature_with_speed["obj"][0], 0)


canvas.bind(MOUSE_CLICK, pass_data)
canvas.focus_set()
canvas.bind(KEY_PRESS, jumper)
t0 = time.time()

while True:
    time.sleep(speed)

    temp_list = list(creature_with_speed.keys())
    for itemy in temp_list:
        if (temp_list.index(itemy) % 2 == 0) and (itemy != "obj"):
            update_position(canvas, itemy, creature_with_speed.get(itemy), y=random.choice([3, -3]))

        elif (itemy != "obj"):
            update_position(canvas, itemy, creature_with_speed.get(itemy), y=0)

    gui.update()
    print(canvas.coords("obj"))

    for key, value in creature_with_speed.items():
        temp = canvas.coords(key)
        if key != "obj" and (temp[0] > window_width - 50 or temp[0] < 0):
            creature_with_speed[key] = -1 * value + random.choice([1, -1])

    speed /= 3

    if time.time() - t0 > 3:
        t0 = time.time()
        last_str = updater(len(list(creature_with_speed.keys())))

        helpers.make_creature(canvas, (random.uniform(80, window_width), random.uniform(80, window_height * 0.75)),
                              width=random.uniform(40, 120),
                              primary_color=random.choice(['brown', 'red', 'green', 'pink']),
                              secondary_color=random.choice(['brown', 'red', 'green', 'pink']),
                              tag=last_str)
        creature_with_speed[last_str] = 3

        helpers.make_landscape_object(canvas, (window_width, window_height), size=100, tag="landscape")

########################## YOUR CODE ABOVE THIS LINE ##############################

# makes sure the canvas keeps running:
canvas.mainloop()
