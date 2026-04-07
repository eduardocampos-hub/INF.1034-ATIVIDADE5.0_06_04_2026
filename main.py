from pygame import *
import sys
init()

window = display.set_mode((1280,720))

window.fill((152,209,250))


while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()

    #desenhar a partir daqui
 
    draw.rect(window, (34, 139, 34), (0, 600, 1280, 120)) 

    # Casa
    draw.rect(window, (169, 169, 169), (500, 400, 300, 200))

    # Telhado
    draw.polygon(window, (139, 69, 19), [(500, 400), (650, 250), (800, 400)]) 

    # Porta
    draw.rect(window, (100, 50, 0), (620, 500, 60, 100))  

    # Janela
    draw.rect(window, (68, 161, 219), (530, 480, 50, 50))  

    # sol
    draw.circle(window, (255, 255,0),(200,150),50)

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

        # Oito linhas em volta do sol
    draw.line(window, (255, 255, 0), (200, 60), (200, 120), 7)   
    draw.line(window, (255, 255, 0), (200, 200), (200, 250), 7) 
    draw.line(window, (255, 255, 0), (150, 150), (100, 150), 7)  
    draw.line(window, (255, 255, 0), (250, 150), (300, 150), 7) 
    draw.line(window, (255, 255, 0), (170, 120), (120, 70), 7)  
    draw.line(window, (255, 255, 0), (230, 120), (280, 70), 7)  
    draw.line(window, (255, 255, 0), (170, 180), (120, 230), 7) 
    draw.line(window, (255, 255, 0), (230, 180), (280, 230), 7)
    display.update()
