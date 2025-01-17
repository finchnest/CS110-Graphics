'''
This demo shows you how you can create a new image by clicking the screen.
'''
from tkinter import Canvas, Tk
import helpers
import utilities
import time
import random
import keycodes

gui = Tk()
gui.title('Tour of options...')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
canvas = Canvas(gui, width=window_width, height=window_height, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################
MOUSE_CLICK = '<Button-1>'
KEY_PRESS = '<Key>'
canvas.create_text(
    (window_width / 2, window_height / 2), 
    text='Click anywhere add a circle. Press arrow keys to move circle', 
    font=("Purisa", 32)
)

def make_circle(event):
    utilities.make_circle(
        canvas,
        (event.x, event.y),
        20, 
        color='hotpink',
        tag='circle'
    )
    canvas.focus_set()

def move_circle(event):
    # NOTE: Because Windows and Mac have different keycodes, use the functions
    # from the keycode module to detect the different keys
    distance = 10
    if event.keycode == keycodes.get_up_keycode():
        utilities.update_position_by_tag(canvas, tag='circle', x=0, y=-distance)
    elif event.keycode == keycodes.get_down_keycode():
        utilities.update_position_by_tag(canvas, tag='circle', x=0, y=distance)
    elif event.keycode == keycodes.get_left_keycode():
        utilities.update_position_by_tag(canvas, tag='circle', x=-distance, y=0)
    elif event.keycode == keycodes.get_right_keycode():
        utilities.update_position_by_tag(canvas, tag='circle', x=distance, y=0)
    else:
        print('Keycode:', event.keycode, 'not handled by this if/elif/else statement.')

canvas.bind(MOUSE_CLICK, make_circle) 
canvas.bind(KEY_PRESS, move_circle)


########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()