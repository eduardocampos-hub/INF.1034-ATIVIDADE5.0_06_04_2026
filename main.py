from pygame import *

init()

window = display.set_mode((1280,720))

window.fill((152,209,250))


while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()

    #desenhar a partir daqui
    draw.rect(window,(255,0,0),(100,100,200,200),0)
    draw.circle(window,(255,255,0),(400,400),100,0)
    draw.polygon(window,(255,0,255),((500,100),(600,200),(400,200)),0)

    display.update()
