def _get_coordinates(canvas, id):
    return canvas.coords(id)


def _set_coordinates(canvas, id, coordinates):
    canvas.coords(id, coordinates)


def _update_position_by_id(canvas, id, x=2, y=0):
    coords = _get_coordinates(canvas, id)
    # update coordinates:
    for i in range(0, len(coords)):
        if i % 2 == 0:
            coords[i] += x
        else:
            coords[i] += y
    # set the coordinates:
    _set_coordinates(canvas, id, coords)


def _get_x_coordinates(canvas, tag):
    return _get_coordinates_by_dimension(canvas, tag, dimension='x')


def _get_y_coordinates(canvas, tag):
    return _get_coordinates_by_dimension(canvas, tag, dimension='y')


def make_circle(canvas, center, radius, color='white', tag=None, stroke_width=2, outline=None):
    make_oval(
        canvas, center, radius, radius, color=color, tag=tag,
        stroke_width=stroke_width, outline=outline
    )


def make_oval(canvas, center, radius_x, radius_y, color='#FF4136', tag=None, stroke_width=1, outline=None):
    x, y = center
    return canvas.create_oval(
        [x - radius_x, y - radius_y, x + radius_x, y + radius_y],
        fill=color,
        width=stroke_width,
        tags=tag,
        outline=outline
    )


def make_rectangle(canvas, top_left, width, height, color="#3D9970", tag=None):
    x, y = top_left
    return canvas.create_rectangle(
        [(x, y), (x + width, y + height)],
        fill=color,
        width=0,
        tags=tag
    )


def _get_coordinates_by_dimension(canvas, tag, dimension='x'):
    '''
    updates the x and y position of all shapes that have been tagged
    with the tag argument
    '''
    if dimension == 'x':
        pos = 0
    else:
        pos = 1
    shape_ids = canvas.find_withtag(tag)
    coords = []
    for id in shape_ids:
        shape_coords = _get_coordinates(canvas, id)
        for i in range(0, len(shape_coords)):
            if i % 2 == pos:
                coords.append(shape_coords[i])
    return coords


def update_position(canvas, tag, x=2, y=0):
    '''
    updates the x and y position of all shapes that have been tagged
    with the tag argument
    '''
    shape_ids = canvas.find_withtag(tag)
    for id in shape_ids:
        _update_position_by_id(canvas, id, x, y)


def get_left(canvas, tag):
    '''
    returns the left boundary of the shape group
    '''
    return min(*_get_x_coordinates(canvas, tag))


def get_right(canvas, tag):
    '''
    returns the right boundary of the shape group
    '''
    return max(*_get_x_coordinates(canvas, tag))


def get_top(canvas, tag):
    '''
    returns the top boundary of the shape group
    '''
    return min(*_get_y_coordinates(canvas, tag))


def get_bottom(canvas, tag):
    '''
    returns the bottom boundary of the shape group
    '''
    return max(*_get_y_coordinates(canvas, tag))


def get_width(canvas, tag):
    '''
    returns the width of the shape group
    '''
    x_coords = _get_x_coordinates(canvas, tag)
    return max(*x_coords) - min(*x_coords)


def get_height(canvas, tag):
    '''
    returns the height of the shape group
    '''
    y_coords = _get_y_coordinates(canvas, tag)
    return max(*y_coords) - min(*y_coords)


def make_car(canvas, top_left=(0, 0), color="#3D9970", tag=None):
    '''
    demo function that show you how to draw a car, given the convenience
    functions that are available in this module
    '''
    x, y = top_left
    make_rectangle(canvas, (x + 50, y), 100, 40, color=color, tag=tag)
    make_rectangle(canvas, (x, y + 30), 200, 45, color=color, tag=tag)
    make_circle(canvas, (x + 50, y + 80), 20, color='black', tag=tag)
    make_circle(canvas, (x + 150, y + 80), 20, color='black', tag=tag)


def make_star(canvas, center, diameter):
    '''
    demo function that show you how to draw a star, given the convenience
    functions that are available in this module
    '''
    make_circle(
        canvas,
        center,
        diameter / 2,
        stroke_width=0,
        outline='white',
        color='white'
    )


def make_bubble(canvas, center, diameter):
    '''
    demo function that show you how to draw a bubble, given the convenience
    functions that are available in this module
    '''
    make_circle(
        canvas,
        center,
        diameter / 2,
        stroke_width=1,
        outline='white',
        color=None
    )


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
                       (center[0], center[1] + width / 7), tag)

    my_make_curvy_line(canvas, (center[0] + width / 5, center[1] + width / 4), (center[0], center[1] + width / 5),
                       (center[0], center[1] + width / 7), tag)

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
    make_oval(canvas, center, radius, radius, fill, tag)


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


def my_make_curvy_line(canvas, leftE, rightE, bottomE, tag=None):
    canvas.create_line(
        [
            leftE,
            rightE,
            bottomE,

        ],
        splinesteps=20,
        width=3,
        tags=tag,
        smooth=True)
