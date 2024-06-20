import pyray as ray

# Initialization
screenWidth = 800
screenHeight = 450
ray.init_window(screenWidth, screenHeight, "payraytest")

posv: ray.Vector2 = ray.Vector2(
    ray.get_screen_width() / 4.0, ray.get_screen_height() / 4.0
)
sizev: ray.Vector2 = ray.Vector2(
    ray.get_screen_width() / 2.0, ray.get_screen_height() / 2.0
)
speedv: ray.Vector2 = ray.Vector2(4.0, 5.0)

ray.set_target_fps(144)

while not ray.window_should_close():

    posv.x += speedv.x
    posv.y += speedv.y

    if (
        (posv.y >= (ray.get_screen_height() - sizev.y))
        or (posv.y <= 0)
        or (posv.y >= sizev.y)
    ):
        speedv.x *= -1.0
    print("test 1")
    if (
        (posv.y >= (ray.get_screen_height() - sizev.y))
        or (posv.y <= 0)
        or (posv.y >= sizev.y)
    ):
        speedv.y *= -1.0
    print("test 2")

    ray.begin_drawing()

    ray.clear_background(ray.RAYWHITE)

    ray.draw_rectangle_v(posv, sizev, ray.MAROON)

    ray.draw_fps(10, 10)

    ray.end_drawing()

# De-Initialization
ray.close_window()
