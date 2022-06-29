let b = 0
let a = 0
basic.forever(function () {
    if (input.soundLevel() > 200) {
        basic.showLeds(`
            # # # # #
            . . . . .
            # . . . #
            . . . . .
            # # # # #
            `)
        basic.pause(200)
        basic.showLeds(`
            # . . . #
            . # # # .
            # . . . #
            . # # # .
            # . . . #
            `)
        basic.pause(200)
        basic.showLeds(`
            . . . . .
            . # . # .
            # # # # #
            . # # # .
            . . # . .
            `)
    } else if (!(input.buttonIsPressed(Button.B)) && (a == 0 && input.buttonIsPressed(Button.A))) {
        basic.showLeds(`
            . . . . #
            . . . . .
            . . . . #
            . . . . .
            . . . . #
            `)
        basic.pause(100)
        basic.showLeds(`
            . . . . #
            . . . . .
            . . . # #
            . . . . .
            . . . . #
            `)
        basic.pause(100)
        basic.showLeds(`
            . . # . #
            . . . . .
            . . # # #
            . . . . .
            . . # . #
            `)
        if (!(input.buttonIsPressed(Button.B)) && (a == 0 && input.buttonIsPressed(Button.A))) {
            a = 1
        }
        basic.pause(100)
        basic.showLeds(`
            . . # . #
            . # . . .
            . # # # #
            . # . . .
            . . # . #
            `)
        basic.pause(100)
        basic.showLeds(`
            # . # . #
            . # . . .
            # # # # #
            . # . . .
            # . # . #
            `)
        basic.pause(200)
    } else if (!(input.buttonIsPressed(Button.A)) && (b == 0 && input.buttonIsPressed(Button.B))) {
        basic.showLeds(`
            # . . . .
            . . . . .
            # . . . .
            . . . . .
            # . . . .
            `)
        basic.pause(100)
        basic.showLeds(`
            # . . . .
            . . . . .
            # # . . .
            . . . . .
            # . . . .
            `)
        basic.pause(100)
        basic.showLeds(`
            # . # . .
            . . . . .
            # # # . .
            . . . . .
            # . # . .
            `)
        if (!(input.buttonIsPressed(Button.A)) && (b == 0 && input.buttonIsPressed(Button.B))) {
            b = 1
        }
        basic.pause(100)
        basic.showLeds(`
            # . # . .
            . . . # .
            # # # # .
            . . . # .
            # . # . .
            `)
        basic.pause(100)
        basic.showLeds(`
            # . # . #
            . . . # .
            # # # # #
            . . . # .
            # . # . #
            `)
        basic.pause(200)
    } else if (a == 1) {
        basic.showLeds(`
            . . . . #
            . . . . .
            . . . . #
            . . . . .
            . . . . #
            `)
        if (input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B)) {
            a = 0
        }
        basic.pause(100)
        basic.showLeds(`
            . . . . #
            . . . . .
            . . . # #
            . . . . .
            . . . . #
            `)
        if (input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B)) {
            a = 0
        }
        basic.pause(100)
        basic.showLeds(`
            . . # . #
            . . . . .
            . . # # #
            . . . . .
            . . # . #
            `)
        if (input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B)) {
            a = 0
        }
        basic.pause(100)
        basic.showLeds(`
            . . # . #
            . # . . .
            . # # # #
            . # . . .
            . . # . #
            `)
        if (input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B)) {
            a = 0
        }
        basic.pause(100)
        basic.showLeds(`
            # . # . #
            . # . . .
            # # # # #
            . # . . .
            # . # . #
            `)
        if (input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B)) {
            a = 0
        }
        basic.pause(100)
    } else if (input.isGesture(Gesture.Shake)) {
        led.setBrightness(255)
        for (let index = 0; index < 5; index++) {
            basic.showLeds(`
                . . # . .
                . # . # .
                # . # . #
                . # . # .
                . . # . .
                `)
            basic.pause(200)
            basic.clearScreen()
            basic.pause(200)
        }
    } else if (input.logoIsPressed()) {
        led.setBrightness(255)
        basic.showLeds(`
            # . . . #
            . # # # .
            # # # # #
            . # # # .
            # . . . #
            `)
    } else if (input.lightLevel() <= 128) {
        led.setBrightness(109)
        basic.showLeds(`
            # # # # #
            . . . . .
            # . . . #
            . . . . .
            # # # # #
            `)
    } else if (input.lightLevel() > 128) {
        basic.clearScreen()
    }
})
