from tkinter import Canvas, Tk
from creature import make_creature

# initialize window
gui = Tk()
gui.title('Creature')
canvas = Canvas(gui, width=550, height=550, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

# Call your creature function with different arguments here:
make_creature(canvas, (250, 250), width=300, primary_color='#aebb83', secondary_color='#227876')
# make_creature(canvas, (200, 200), width=150, primary_color='#aebb83', secondary_color='#227876')
# make_creature(canvas, (250, 250))
# make_creature(canvas, (250, 250), width=200)
# make_grid(canvas, 550, 550)


########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()
