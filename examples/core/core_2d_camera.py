# core_2d_camera.py

from raylibpy import *
# from raylibpy.structures import *
# from raylibpy.constants import *
# from raylibpy.colors import *
# from raylibpy.core import *
# from raylibpy.text import *
# from raylibpy.shapes import *

MAX_BUILDINGS = 100

def main():

    # Initialization
    # ---------------------------------------------------------------
    screen_width = 800
    screen_height = 450

    init_window(screen_width, screen_height, b"raylib [core] example - 2d camera")

    player = Rectangle(400, 280, 40, 40)
    buildings = []
    build_colors = []

    spacing = 0

    for i in range(MAX_BUILDINGS):
        width = get_random_value(50, 200)
        height = get_random_value(100, 800)
        y = screen_height - 130 - height
        x = -6000 + spacing

        buildings.append(Rectangle(x, y, width, height))

        spacing += width

        build_colors.append(Color(
                get_random_value(200, 240),
                get_random_value(200, 240),
                get_random_value(200, 250),
                255
            )
        )

    camera = Camera2D()

    camera.offset = Vector2(0, 0)
    camera.target = Vector2(player.x + 20, player.y + 20)
    camera.rotation = 0.0
    camera.zoom = 1.0

    print(camera.__class__, Camera2D.__class__)

    set_target_fps(60)
    # ---------------------------------------------------------------

    # Main game loop
    while not window_should_close():

        # Update
        # -----------------------------------------------------------
        if is_key_down(KEY_RIGHT):
            player.x += 2           # player movement
            camera.offset.x -= 2    # camera displacement with player movement

        elif is_key_down(KEY_LEFT):
            player.x -= 2
            camera.offset.x += 2

        # camera follows player
        camera.target = Vector2(player.x + 20, player.y + 20)

        # camera rotation controls
        if is_key_down(KEY_A):
            camera.rotation -= 1
        elif is_key_down(KEY_S):
            camera.rotation += 1

        # limit camera rotation to 80 degrees (-40 to 40)
        camera.rotation = max(-40, min(camera.rotation, 40))

        # camera zoom controls
        camera.zoom += get_mouse_wheel_move() * 0.05

        camera.zoom = max(0.1, min(camera.zoom, 3.0))

        # camera reset (zoom and rotation)
        if is_key_pressed(KEY_R):
            camera.zoom = 1.0
            camera.rotation = 0.0
        # -----------------------------------------------------------

        # Draw
        # -----------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        begin_mode2d(camera)

        draw_rectangle(-6000, 300, 13000, 8000, DARKGRAY)

        for i, rec in enumerate(buildings):
            draw_rectangle_rec(rec, build_colors[i])

        draw_rectangle_rec(player, RED)

        draw_rectangle(int(camera.target.x), int(-500), 1, screen_height * 4, GREEN)
        draw_rectangle(int(-500), int(camera.target.y), screen_width * 4, 1, GREEN)

        end_mode2d()

        draw_text(b"SCREEN AREA", 640, 10, 20, RED)

        draw_rectangle(0, 0, screen_width, 5, RED)
        draw_rectangle(0, 5, 5, screen_height - 10, RED)
        draw_rectangle(screen_width - 5, 5, 5, screen_height - 10, RED)
        draw_rectangle(0, screen_height - 5, screen_width, 5, RED)

        draw_rectangle( 10, 10, 250, 113, fade(SKYBLUE, 0.5))
        draw_rectangle_lines( 10, 10, 250, 113, BLUE)

        draw_text(b"Free 2d camera controls:", 20, 20, 10, BLACK)
        draw_text(b"- Right/Left to move Offset", 40, 40, 10, DARKGRAY)
        draw_text(b"- Mouse Wheel to Zoom in-out", 40, 60, 10, DARKGRAY)
        draw_text(b"- A / S to Rotate", 40, 80, 10, DARKGRAY)
        draw_text(b"- R to reset Zoom and Rotation", 40, 100, 10, DARKGRAY)

        end_drawing()
        # -----------------------------------------------------------

    # De-Initialization
    # ---------------------------------------------------------------
    close_window()       # Close window and OpenGL context
    # ---------------------------------------------------------------


if __name__ == '__main__':
    main()
