def on_button_pressed_a():
    global posX, posY
    if choixfin == 0:
        if HAUTBAS == 0:
            led.unplot(posX, posY)
            posX += -1
            if posX < 0:
                posX += 1
            posY += 0
            led.plot(posX, posY)
        if HAUTBAS == 1:
            led.unplot(posX, posY)
            posY += 1
            if posY > 4:
                posY += -1
            posY += 0
            led.plot(posX, posY)
            led.plot(Xse1, Yse1)
            led.plot(Xse2, Yse2)
            led.plot(Xse3, Yse3)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global HAUTBAS, Xse1, Yse1, selec, verif, Yse2, Xse2, Yse3, Xse3, choixfin
    if HAUTBAS == 0:
        HAUTBAS = 1
    elif HAUTBAS == 1:
        if selec == 0:
            Xse1 = posX
            Yse1 = posY
            selec += 1
            HAUTBAS = 0
            verif += 1
        elif selec == 1:
            Yse2 = posY
            Xse2 = posX
            selec += 1
            HAUTBAS = 0
            verif += 1
        elif selec == 2:
            Yse3 = posY
            Xse3 = posX
            selec += 1
            HAUTBAS = 0
            verif += 1
        elif selec == 3:
            led.plot(Xse1, Yse1)
            led.plot(Xse2, Yse2)
            led.plot(Xse3, Yse3)
            choixfin = 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global posX, posY
    if choixfin == 0:
        if HAUTBAS == 0:
            led.unplot(posX, posY)
            posX += 1
            if posX > 4:
                posX += -1
            posY += 0
            led.plot(posX, posY)
        if HAUTBAS == 1:
            led.unplot(posX, posY)
            posY += -1
            if posY < 0:
                posY += 1
            posY += 0
            led.plot(posX, posY)
            led.plot(Xse1, Yse1)
            led.plot(Xse2, Yse2)
            led.plot(Xse3, Yse3)
input.on_button_pressed(Button.B, on_button_pressed_b)

Yse3 = 0
Yse2 = 0
Yse1 = 0
posY = 0
posX = 0
lancement1 = 0
lancement = 0
verif = 0
choixfin = 0
HAUTBAS = 0
selec = 0
Xse3 = 0
Xse2 = 0
Xse1 = 0
Xse1 = 70
Xse2 = 70
Xse3 = 70
selec = 0
HAUTBAS = 0
choixfin = 0
if verif == 0:
    lancement = 0
    lancement1 = 0
    lancement += 1
    posX = 2
    posY = 4
    led.plot(posX, posY)

def on_forever():
    global posX, posY, verif
    if verif == 1:
        posX = 2
        posY = 4
        led.plot(posX, posY)
        verif += 2
    if verif == 4:
        posX = 2
        posY = 4
        led.plot(posX, posY)
        verif += 2
    if verif == 7:
        posX = 2
        posY = 4
        led.plot(posX, posY)
        verif += 2
basic.forever(on_forever)



ce truc est impossible, je sais pas comment faire et quand j'ai reussi en block, il voulais plus le renvoyer en python, ça ma fait rager j'ai abandonner, le module radio c un enfer
# Grosse Force alors, si j'ai le temps je peux checker en vif