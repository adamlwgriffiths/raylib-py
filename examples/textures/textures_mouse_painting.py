# textures_mouse_painting.py
# ******************************************************************************************
#
#   raylib [textures] example - Mouse painting
#
#   This example has been created using raylib 2.5 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Example contributed by Chris Dill (@MysteriousSpace) and reviewed by Ramon Santamaria (@raysan5)
#
#   Copyright (c) 2019 Chris Dill (@MysteriousSpace) and Ramon Santamaria (@raysan5)
#
# *******************************************************************************************/

from typing import List
from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *

MAX_COLORS_COUNT = 23  # Number of colors available


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [textures] example - mouse painting")

    # Colours to choose from
    colors: List[Color] = [
        RAYWHITE, YELLOW, GOLD, ORANGE, PINK, RED, MAROON, GREEN, LIME, DARKGREEN,
        SKYBLUE, BLUE, DARKBLUE, PURPLE, VIOLET, DARKPURPLE, BEIGE, BROWN, DARKBROWN,
        LIGHTGRAY, GRAY, DARKGRAY, BLACK
    ]

    # Define colorsRecs data (for every rectangle)
    colors_recs: List[Rectangle] = [Rectangle() for _ in range(MAX_COLORS_COUNT)]

    for i in range(MAX_COLORS_COUNT):
        colors_recs[i].x = 10 + 30.0 * i + 2 * i
        colors_recs[i].y = 10
        colors_recs[i].width = 30
        colors_recs[i].height = 30

    color_selected: int = 0
    color_selected_prev: int = color_selected
    color_mouse_hover: int = 0
    brush_size: float = 20.0
    mouse_was_pressed: bool = False

    btn_save_rec: Rectangle = Rectangle(750, 10, 40, 30)
    btn_save_mouse_hover: bool
    show_save_message: bool = False
    save_message_counter: int = 0

    # Create a RenderTexture2D to use as a canvas
    target: RenderTexture2D = load_render_texture(screen_width, screen_height)

    # Clear render texture before entering the game loop
    with texture_mode(target):
        clear_background(colors[0])
    # end texture mode

    set_target_fps(120)  # Set our game to run at 120 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        mouse_pos: Vector2 = get_mouse_position()

        # Move between colors with keys
        if is_key_pressed(KEY_RIGHT):
            color_selected += 1
        elif is_key_pressed(KEY_LEFT):
            color_selected -= 1

        if color_selected >= MAX_COLORS_COUNT:
            color_selected = MAX_COLORS_COUNT - 1
        elif color_selected < 0:
            color_selected = 0

        # Choose color with mouse
        for i in range(MAX_COLORS_COUNT):
            if check_collision_point_rec(mouse_pos, colors_recs[i]):
                color_mouse_hover = i
                break
            else:
                color_mouse_hover = -1

        if color_mouse_hover >= 0 and is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
            color_selected = color_mouse_hover
            color_selected_prev = color_selected

        # Change brush size
        brush_size += get_mouse_wheel_move() * 5
        if brush_size < 2:
            brush_size = 2
        if brush_size > 50:
            brush_size = 50

        if is_key_pressed(KEY_C):
            # Clear render texture to clear color
            begin_texture_mode(target)
            clear_background(colors[0])
            end_texture_mode()

        if is_mouse_button_down(MOUSE_BUTTON_LEFT) or (get_gesture_detected() == GESTURE_DRAG):
            # Paint circle into render texture
            # NOTE: To avoid discontinuous circles, we could store
            # previous-next mouse points and just draw a line using brush size
            begin_texture_mode(target)
            if mouse_pos.y > 50:
                draw_circle(mouse_pos.x, mouse_pos.y, brush_size, colors[color_selected])
            end_texture_mode()

        if is_mouse_button_down(MOUSE_BUTTON_RIGHT):
            if not mouse_was_pressed:
                color_selected_prev = color_selected
                color_selected = 0

            mouse_was_pressed = True

            # Erase circle from render texture
            with texture_mode(target):
                if mouse_pos.y > 50:
                    draw_circle(mouse_pos.x, mouse_pos.y, brush_size, colors[0])
            # end texture mode
        elif is_mouse_button_released(MOUSE_BUTTON_RIGHT) and mouse_was_pressed:
            color_selected = color_selected_prev
            mouse_was_pressed = False

        # Check mouse hover save button
        if check_collision_point_rec(mouse_pos, btn_save_rec):
            btn_save_mouse_hover = True
        else:
            btn_save_mouse_hover = False

        # Image saving logic
        # NOTE: Saving painted texture to a default named image
        if btn_save_mouse_hover and is_mouse_button_released(MOUSE_BUTTON_LEFT) or is_key_pressed(KEY_S):
            image: Image = get_texture_data(target.texture)
            image_flip_vertical(image)
            export_image(image, "my_amazing_texture_painting.png")
            unload_image(image)
            show_save_message = True

        if show_save_message:
            # On saving, show a full screen message for 2 seconds
            save_message_counter += 1
            if save_message_counter > 240:
                show_save_message = False
                save_message_counter = 0
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        # NOTE: Render texture must be y-flipped due to default OpenGL coordinates (left-bottom)
        draw_texture_rec(target.texture, Rectangle(0, 0, target.texture.width, -target.texture.height), Vector2(),
                         WHITE)

        # Draw drawing circle for reference
        if mouse_pos.y > 50:
            if is_mouse_button_down(MOUSE_BUTTON_RIGHT):
                draw_circle_lines(mouse_pos.x, mouse_pos.y, brush_size, GRAY)
            else:
                draw_circle(get_mouse_x(), get_mouse_y(), brush_size, colors[color_selected])

        # Draw top panel
        draw_rectangle(0, 0, get_screen_width(), 50, RAYWHITE)
        draw_line(0, 50, get_screen_width(), 50, LIGHTGRAY)

        # Draw color selection rectangles
        for i in range(MAX_COLORS_COUNT):
            draw_rectangle_rec(colors_recs[i], colors[i])
        draw_rectangle_lines(10, 10, 30, 30, LIGHTGRAY)

        if color_mouse_hover >= 0:
            draw_rectangle_rec(colors_recs[color_mouse_hover], fade(WHITE, 0.6))

        draw_rectangle_lines_ex(
            Rectangle(colors_recs[color_selected].x - 2,
                      colors_recs[color_selected].y - 2,
                      colors_recs[color_selected].width + 4,
                      colors_recs[color_selected].height + 4),
            2, BLACK)

        # Draw save image button
        draw_rectangle_lines_ex(btn_save_rec, 2, RED if btn_save_mouse_hover else BLACK)
        draw_text("SAVE!", 755, 20, 10, RED if btn_save_mouse_hover else BLACK)

        # Draw save image message
        if show_save_message:
            draw_rectangle(0, 0, get_screen_width(), get_screen_height(), fade(RAYWHITE, 0.8))
            draw_rectangle(0, 150, get_screen_width(), 80, BLACK)
            draw_text("IMAGE SAVED:  my_amazing_texture_painting.png", 150, 180, 20, RAYWHITE)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    unload_render_texture(target)  # Unload render texture

    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()
