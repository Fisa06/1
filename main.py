b = 0
a = 0

def on_forever():
    global a, b
    if input.sound_level() > 200:
        basic.show_leds("""
            # # # # #
                        . . . . .
                        # . . . #
                        . . . . .
                        # # # # #
        """)
        basic.pause(200)
        basic.show_leds("""
            # . . . #
                        . # # # .
                        # . . . #
                        . # # # .
                        # . . . #
        """)
        basic.pause(200)
        basic.show_leds("""
            . . . . .
                        . # . # .
                        # # # # #
                        . # # # .
                        . . # . .
        """)
    elif not (input.button_is_pressed(Button.B)) and (a == 0 and input.button_is_pressed(Button.A)):
        basic.show_leds("""
            . . . . #
                        . . . . .
                        . . . . #
                        . . . . .
                        . . . . #
        """)
        basic.pause(100)
        basic.show_leds("""
            . . . . #
                        . . . . .
                        . . . # #
                        . . . . .
                        . . . . #
        """)
        basic.pause(100)
        basic.show_leds("""
            . . # . #
                        . . . . .
                        . . # # #
                        . . . . .
                        . . # . #
        """)
        if not (input.button_is_pressed(Button.B)) and (a == 0 and input.button_is_pressed(Button.A)):
            a = 1
        basic.pause(100)
        basic.show_leds("""
            . . # . #
                        . # . . .
                        . # # # #
                        . # . . .
                        . . # . #
        """)
        basic.pause(100)
        basic.show_leds("""
            # . # . #
                        . # . . .
                        # # # # #
                        . # . . .
                        # . # . #
        """)
        basic.pause(200)
    elif not (input.button_is_pressed(Button.A)) and (b == 0 and input.button_is_pressed(Button.B)):
        basic.show_leds("""
            # . . . .
                        . . . . .
                        # . . . .
                        . . . . .
                        # . . . .
        """)
        basic.pause(100)
        basic.show_leds("""
            # . . . .
                        . . . . .
                        # # . . .
                        . . . . .
                        # . . . .
        """)
        basic.pause(100)
        basic.show_leds("""
            # . # . .
                        . . . . .
                        # # # . .
                        . . . . .
                        # . # . .
        """)
        if not (input.button_is_pressed(Button.A)) and (b == 0 and input.button_is_pressed(Button.B)):
            b = 1
        basic.pause(100)
        basic.show_leds("""
            # . # . .
                        . . . # .
                        # # # # .
                        . . . # .
                        # . # . .
        """)
        basic.pause(100)
        basic.show_leds("""
            # . # . #
                        . . . # .
                        # # # # #
                        . . . # .
                        # . # . #
        """)
        basic.pause(200)
    elif a == 1:
        basic.show_leds("""
            . . . . #
                        . . . . .
                        . . . . #
                        . . . . .
                        . . . . #
        """)
        if input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
            a = 0
        basic.pause(100)
        basic.show_leds("""
            . . . . #
                        . . . . .
                        . . . # #
                        . . . . .
                        . . . . #
        """)
        if input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
            a = 0
        basic.pause(100)
        basic.show_leds("""
            . . # . #
                        . . . . .
                        . . # # #
                        . . . . .
                        . . # . #
        """)
        if input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
            a = 0
        basic.pause(100)
        basic.show_leds("""
            . . # . #
                        . # . . .
                        . # # # #
                        . # . . .
                        . . # . #
        """)
        if input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
            a = 0
        basic.pause(100)
        basic.show_leds("""
            # . # . #
                        . # . . .
                        # # # # #
                        . # . . .
                        # . # . #
        """)
        if input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
            a = 0
        basic.pause(500)
    elif False:
        pass
    elif False:
        pass
    elif False:
        pass
    elif False:
        pass
    elif False:
        pass
    elif input.button_is_pressed(Button.AB):
        led.set_brightness(255)
        basic.show_leds("""
            . . # . .
                        . # . # .
                        # . # . #
                        . # . # .
                        . . # . .
        """)
        basic.pause(200)
        basic.clear_screen()
        basic.pause(200)
    elif input.is_gesture(Gesture.SHAKE):
        led.set_brightness(255)
        for index in range(5):
            basic.show_leds("""
                . . # . .
                                . # . # .
                                # . # . #
                                . # . # .
                                . . # . .
            """)
            basic.pause(200)
            basic.clear_screen()
            basic.pause(200)
    elif input.logo_is_pressed():
        led.set_brightness(255)
        basic.show_leds("""
            # . . . #
                        . # # # .
                        # # # # #
                        . # # # .
                        # . . . #
        """)
    elif input.light_level() <= 128:
        led.set_brightness(109)
        basic.show_leds("""
            # # # # #
                        . . . . .
                        # . . . #
                        . . . . .
                        # # # # #
        """)
    elif input.light_level() > 128:
        basic.clear_screen()
    else:
        pass
basic.forever(on_forever)
