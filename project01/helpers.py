from project01.utilities import *


def make_creature(canvas, center: tuple, width: int = 100, primary_color: str = 'brown',
                  secondary_color: str = '#648d8e', tag=None):
    # head

    my_make_circle(canvas, center, width / 2, primary_color, tag)

    # eyes

    my_make_oval(canvas, (center[0] - width / 7, center[1] - width / 7), width / 12, width / 12, "black", tag)
    my_make_oval(canvas, (center[0] + width / 7, center[1] - width / 7), width / 12, width / 12, "black", tag)

    # ears

    my_make_circle(canvas, (center[0] + width / 2.1, center[1] - width / 3), width / 5, secondary_color, tag)
    my_make_circle(canvas, (center[0] - width / 2.1, center[1] - width / 3), width / 5, secondary_color, tag)

    # nose

    my_make_polygon(canvas, (center[0] - width / 5, center[1]), (center[0] + width / 5, center[1]),
                    (center[0], center[1] + width / 5), tag)

    # beardline

    my_make_curvy_line(canvas, (center[0] - width / 5, center[1] + width / 4), (center[0], center[1] + width / 5),
                       (center[0], center[1] + width / 7), 3, tag)

    my_make_curvy_line(canvas, (center[0] + width / 5, center[1] + width / 4), (center[0], center[1] + width / 5),
                       (center[0], center[1] + width / 7), 3, tag)

    # eye shadows

    my_make_oval(canvas, (center[0] + width / 7, center[1] - width / 7), width / 24, width / 24, "white", tag)
    my_make_oval(canvas, (center[0] - width / 7, center[1] - width / 7), width / 24, width / 24, "white", tag)


def my_make_oval(canvas, center: tuple, radius_x: float, radius_y: float, fill: str, tag=None):
    canvas.create_oval(
        [
            (center[0] - radius_x, center[1] - radius_y),
            (center[0] + radius_x, center[1] + radius_y)
        ],
        tags=tag,
        fill=fill)


def my_make_circle(canvas, center: tuple, radius: int, fill: str, tag=None):
    my_make_oval(canvas, center, radius, radius, fill, tag)


def my_make_polygon(canvas, leftEnd: tuple, rightEnd: tuple, bottomEnd: tuple, tag=None):
    canvas.create_polygon(
        [
            leftEnd,
            rightEnd,
            bottomEnd
        ],
        width=2,
        fill='#000000',
        tags=tag,
        smooth=True)


def my_make_curvy_line(canvas, leftE, rightE, bottomE, thickness, tag=None):
    canvas.create_line(
        [
            leftE,
            rightE,
            bottomE,

        ],
        splinesteps=20,
        width=thickness,
        tags=tag,
        smooth=True)


def make_landscape_object(canvas, center, size=100, tag="landscape"):
    # calls to curve line maker functions with different arguments to create branches.
    make_rectangle(canvas, (center[0] * 0.20, center[1] * 0.6), 20, center[1] * 0.22, "black", tag)

    my_make_curvy_line(canvas, (center[0] * 0.2 - 50, center[1] * 0.6 + 10),
                       (center[0] * 0.2 - 10, center[1] * 0.6 + 20), (center[0] * 0.2 + 10, center[1] * 0.6 + 50), 15,
                       tag)
    my_make_curvy_line(canvas, (center[0] * 0.2, center[1] * 0.6 + 50), (center[0] * 0.2 + 20, center[1] * 0.6 + 20),
                       (center[0] * 0.2 + 70, center[1] * 0.6 + 10), 15, tag)

    my_make_curvy_line(canvas, (center[0] * 0.2 - 50, center[1] * 0.6 + 60),
                       (center[0] * 0.2 - 10, center[1] * 0.6 + 70), (center[0] * 0.2 + 10, center[1] * 0.6 + 100), 15,
                       tag)
    my_make_curvy_line(canvas, (center[0] * 0.2, center[1] * 0.6 + 100), (center[0] * 0.2 + 20, center[1] * 0.6 + 70),
                       (center[0] * 0.2 + 70, center[1] * 0.6 + 60), 15, tag)
    my_make_curvy_line(canvas, (center[0] * 0.2, center[1] * 0.6 + 0), (center[0] * 0.2 + 20, center[1] * 0.6 + 40),
                       (center[0] * 0.2 + 70, center[1] * 0.6 + 10), 15, tag)
    ###################
    make_rectangle(canvas, (center[0] * 0.80, center[1] * 0.6), 20, center[1] * 0.22, "black", tag)
    make_rectangle(canvas, (0, center[1] * 0.82), center[0], center[1] * 0.18, "brown", tag)
    my_make_curvy_line(canvas,
                       (center[0] * 0.8 - 50, center[1] * 0.6 + 10),
                       (center[0] * 0.8 - 10, center[1] * 0.6 + 20),
                       (center[0] * 0.8 + 10, center[1] * 0.6 + 50),
                       15,
                       tag)
    my_make_curvy_line(canvas,
                       (center[0] * 0.8, center[1] * 0.6 + 50),
                       (center[0] * 0.8 + 20, center[1] * 0.6 + 20),
                       (center[0] * 0.8 + 70, center[1] * 0.6 + 10),
                       15,
                       tag)

    my_make_curvy_line(canvas,
                       (center[0] * 0.8 - 50, center[1] * 0.6 + 60),
                       (center[0] * 0.8 - 10, center[1] * 0.6 + 70),
                       (center[0] * 0.8 + 10, center[1] * 0.6 + 100),
                       15,
                       tag)
    my_make_curvy_line(canvas,
                       (center[0] * 0.8, center[1] * 0.6 + 100),
                       (center[0] * 0.8 + 20, center[1] * 0.6 + 70),
                       (center[0] * 0.8 + 70, center[1] * 0.6 + 60),
                       15,
                       tag)
    my_make_curvy_line(canvas,
                       (center[0] * 0.8, center[1] * 0.6 + 0),
                       (center[0] * 0.8 + 20, center[1] * 0.6 + 40),
                       (center[0] * 0.8 + 70, center[1] * 0.6 + 10),
                       15,
                       tag)

    make_rectangle(canvas, (0, center[1] * 0.82), center[0], center[1] * 0.18,
                   random.choice(['brown', 'pink', 'green']), tag)
