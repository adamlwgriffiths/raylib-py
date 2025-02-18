# core_input_keys.py
# ******************************************************************************************
#
#   raylib [core] example - Keyboard input
#
#   This example has been created using raylib 1.0 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Copyright (c) 2014 Ramon Santamaria (@raysan5)
#
# *******************************************************************************************/

from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [core] example - keyboard input")

    ball_position: Vector2 = Vector2(screen_width / 2, screen_height / 2)

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        if is_key_down(KEY_RIGHT):
            ball_position.x += 2.0
        if is_key_down(KEY_LEFT):
            ball_position.x -= 2.0
        if is_key_down(KEY_UP):
            ball_position.y -= 2.0
        if is_key_down(KEY_DOWN):
            ball_position.y += 2.0
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            draw_text("move the ball with arrow keys", 10, 10, 20, DARKGRAY)

            draw_circle_v(ball_position, 50, MAROON)

        # EndDrawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

