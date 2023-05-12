def on_received_number(receivedNumber):
    global omelette
    omelette = receivedNumber
radio.on_received_number(on_received_number)

def on_button_pressed_ab():
    global omelette
    omelette = randint(10, 20)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_gesture_shake():
    global omelette
    if omelette > 0:
        radio.send_number(omelette)
        omelette = -1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

omelette = 0
radio.set_group(68)
omelette = -1

def on_forever():
    global omelette
    if omelette == 0:
        basic.show_leds("""
            # # # # #
                        . . # . .
                        . # # # .
                        . . # . .
                        . # . # .
        """)
    if omelette < 0:
        basic.clear_screen()
    if omelette > 0:
        basic.show_leds("""
            . . . . .
                        . # # # .
                        # # # # #
                        . # # # .
                        . . . . .
        """)
        omelette += -1
basic.forever(on_forever)
