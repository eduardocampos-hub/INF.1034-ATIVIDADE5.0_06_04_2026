from pygame import *

init()

window = display.set_mode((1280,720))

window.fill((152,209,250))


while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
 
    draw.rect(window, (34, 139, 34), (0, 600, 1280, 120)) 

    # Casa
    draw.rect(window, (169, 169, 169), (500, 400, 300, 200))

    # Telhado
    draw.polygon(window, (139, 69, 19), [(500, 400), (650, 250), (800, 400)]) 

    # Porta
    draw.rect(window, (100, 50, 0), (620, 500, 60, 100))  

    # Janela
    draw.rect(window, (68, 161, 219), (530, 480, 50, 50))  

    # desenhar o sol
    draw.circle(window, (255, 255,0),(200,150),80)

    #Macaneta
    draw.circle(window,(255,215,0),(670,550),7)

    #nuvem
    draw.circle(window, (255, 255, 255), (1000, 100), 50)  
    draw.circle(window, (255, 255, 255), (1050, 100), 50)   
    draw.circle(window, (255, 255, 255), (1100, 100), 50)  
    draw.circle(window, (255, 255, 255), (1150, 100), 50)

    # Árvore
    draw.rect(window, (139, 69, 19), (900, 500, 30, 120))  
    draw.circle(window, (34, 139, 34), (915, 470), 80)  
    display.update()