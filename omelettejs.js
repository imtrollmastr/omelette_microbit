radio.onReceivedNumber(function (receivedNumber) {
    omelette = receivedNumber
})
input.onButtonPressed(Button.AB, function () {
    omelette = randint(10, 20)
})
input.onGesture(Gesture.Shake, function () {
    if (omelette > 0) {
        radio.sendNumber(omelette)
        omelette = -1
    }
})
let omelette = 0
radio.setGroup(68)
omelette = -1
basic.forever(function () {
    if (omelette == 0) {
        basic.showLeds(`
            # # # # #
            . . # . .
            . # # # .
            . . # . .
            . # . # .
            `)
    }
    if (omelette < 0) {
        basic.clearScreen()
    }
    if (omelette > 0) {
        basic.showLeds(`
            . . . . .
            . # # # .
            # # # # #
            . # # # .
            . . . . .
            `)
        omelette += -1
    }
})
