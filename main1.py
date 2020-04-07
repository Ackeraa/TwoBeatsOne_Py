import pygame as pg
import random
from os import path
import time

pg.init()


display_width = 800
display_height = 600

gameDisplay = pg.display.set_mode((display_width, display_height))
pg.display.set_caption('A bit Racey')

white = (255, 255, 255)
black = (0, 0, 0)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

car_width = 73

clock = pg.time.Clock()
carImg = pg.image.load('racecar.png')

def things_dodged(count):
    font = pg.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))


def things(x, y, w, h, c):
    pg.draw.rect(gameDisplay, c, [x, y, w, h])

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pg.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pg.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pg.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def message_display(text):
    largeText = pg.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pg.display.update()

    time.sleep(2)

    game_loop()

def crash():
    message_display('You Crashed')

def game_intro():

    intro = True

    while intro:
        for event in pg.event.get():
            print(event)
            if event.type == pg.QUIT:
                pg.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pg.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,bright_green, game_loop)
        button("Quit",550,450,100,50, red,bright_red, quitgame)

        pg.display.update()
        clock.tick(15)


def game_loop():


    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    thingCount = 1

    dodged = 0

    game_Exit = False

    while not game_Exit:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameExit = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x_change = -20
                elif event.key == pg.K_RIGHT:
                    x_change = 20
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)
        
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed

        car(x, y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if y < thing_starty+thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and\
                x + car_width < thing_startx+thing_width:
                print('x crossover')
                crash()

        pg.display.update()
        clock.tick(60)

game_intro()
game_loop()
pg.quit()
quit()
