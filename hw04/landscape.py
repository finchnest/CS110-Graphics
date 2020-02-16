from tkinter import messagebox, Canvas, Tk
import random
import helpers
import time

gui = Tk()
gui.title('Starry Night')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
canvas = Canvas(gui, width=window_width, height=window_height, background='#000022')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

# TODO: the code below (lines 28-50) is repetitive. Replace it with a loop to make
# 1,000 stars that fill the entire canvas. Hints:
#   a) use a loop
#   b) use the random module, and in particular the random.uniform function to
#      to give each star a random (x, y) position and a random width.
#   c) bonus: Draw a constellation (Orion's Belt, Big Dipper, etc.)

# constellations
ctr = 0
while ctr < 7:
    helpers.make_circle(canvas, (
        random.uniform(window_width * 0.3,
                       window_width * 0.6),
        random.uniform(window_height * 0.15,
                       window_height * 0.25)),
                        random.uniform(10, 20), "blue")
    ctr += 1

# stars
counter = 0
while counter < 100:
    helpers.make_circle(canvas, (random.uniform(0, window_width), random.uniform(0, window_height)),
                        random.uniform(5, 15), tag="comets")
    counter += 1

while True:

    time.sleep(0.05)
    helpers.update_position(canvas, 'comets', x=3, y=0)
    gui.update()

    for x in range(4):
        helpers.make_circle(canvas, (random.uniform(0, window_width), random.uniform(0, window_height)),
                            random.uniform(5, 15), tag="comets")

########################## YOUR CODE ABOVE THIS LINE ##############################

# makes sure the canvas keeps running:
canvas.mainloop()
