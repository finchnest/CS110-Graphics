def make_creature(canvas, center: tuple, width: int = 100, primary_color: str = 'brown',
                  secondary_color: str = '#648d8e'):
    # head

    make_circle(canvas, center, width / 2, primary_color)

    # eyes

    make_oval(canvas, (center[0] - width / 7, center[1] - width / 7), width / 12, width / 12, "black")
    make_oval(canvas, (center[0] + width / 7, center[1] - width / 7), width / 12, width / 12, "black")

    # ears

    make_circle(canvas, (center[0] + width / 2.1, center[1] - width / 3), width / 5, secondary_color)
    make_circle(canvas, (center[0] - width / 2.1, center[1] - width / 3), width / 5, secondary_color)

    # nose

    make_polygon(canvas, (center[0] - width / 5, center[1]), (center[0] + width / 5, center[1]),
                 (center[0], center[1] + width / 5))

    # beardline

    make_curvy_line(canvas, (center[0] - width / 5, center[1] + width / 4), (center[0], center[1] + width / 5),
                    (center[0], center[1] + width / 7))

    make_curvy_line(canvas, (center[0] + width / 5, center[1] + width / 4), (center[0], center[1] + width / 5),
                    (center[0], center[1] + width / 7))

    # eye shadows

    make_oval(canvas, (center[0] + width / 7, center[1] - width / 7), width / 24, width / 24, "white")
    make_oval(canvas, (center[0] - width / 7, center[1] - width / 7), width / 24, width / 24, "white")


def make_oval(canvas, center: tuple, radius_x: float, radius_y: float, fill: str):
    canvas.create_oval(
        [
            (center[0] - radius_x, center[1] - radius_y),
            (center[0] + radius_x, center[1] + radius_y)
        ],
        fill=fill)


def make_circle(canvas, center: tuple, radius: int, fill: str):
    make_oval(canvas, center, radius, radius, fill)


def make_polygon(canvas, leftEnd: tuple, rightEnd: tuple, bottomEnd: tuple):
    canvas.create_polygon(
        [
            leftEnd,
            rightEnd,
            bottomEnd
        ],
        width=2,
        fill='#000000',
        smooth=True)


def make_curvy_line(canvas, leftE, rightE, bottomE):
    canvas.create_line(
        [
            leftE,
            rightE,
            bottomE,

        ],
        splinesteps=20,
        width=3,
        smooth=True)
