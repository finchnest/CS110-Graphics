import time
from tkinter import Canvas, Tk

import helpers

gui = Tk()
gui.title('Animation')
canvas = Canvas(gui, width=500, height=800, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################


helpers.make_car(canvas, top_left=(-201, 50), tag='car1')
helpers.make_car(canvas, top_left=(501, 350), tag='car2')
helpers.make_car(canvas, top_left=(-201, 550), tag='car3')
helpers.make_creature(canvas, (-100, 250), width=100, primary_color='#aebb83', secondary_color='#227876', tag="panda")

speed = 0.05

while True:

    time.sleep(speed)
    helpers.update_position(canvas, 'car1', x=3, y=0)
    helpers.update_position(canvas, 'car2', x=-3, y=0)
    helpers.update_position(canvas, 'panda', x=3, y=0)
    helpers.update_position(canvas, 'car3', x=3, y=0)
    gui.update()

    cord = canvas.coords('car1')
    cord2 = canvas.coords('car2')
    cord3 = canvas.coords('panda')
    cord4 = canvas.coords('car3')

    if cord[0] % 551 == 0:
        canvas.delete('car1')
        helpers.make_car(canvas, top_left=(-201, 50), tag='car1')

    if cord2[0] + 198 < 0:
        canvas.delete('car2')
        helpers.make_car(canvas, top_left=(501, 350), tag='car2')

    print(cord3)
    if cord3[0] > 570:
        canvas.delete('panda')
        helpers.make_creature(canvas, (-100, 250), width=100, primary_color='#aebb83', secondary_color='#227876',
                              tag="panda")

    if cord4[0] % 551 == 0:
        canvas.delete('car3')
        helpers.make_car(canvas, top_left=(-201, 550), tag='car3')

    speed /= 3

########################## YOUR CODE ABOVE THIS LINE ##############################
# makes sure the canvas keeps running:
canvas.mainloop()
