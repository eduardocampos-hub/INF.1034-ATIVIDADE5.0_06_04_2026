from pygame import *
import sys
init()

#imagens

arroz_img = image.load("arroz.png")
arroz_img = transform.scale(arroz_img,(50,50))

#texto
newton_font = font.Font("ThisAppeal-FreeDemo.ttf", 30)
newton_text = newton_font.render("I am Arroz", True, (255,222,234))

#musica
mixer_music.load("Luan santana - Chuva De Arroz (Luan Santana Acústico - Vídeo Oficial) - Luan Santana (128k).mp3")
mixer_music.play(-1)
music = mixer.Sound("Luan santana - Chuva De Arroz (Luan Santana Acústico - Vídeo Oficial) - Luan Santana (128k).mp3")
music.set_volume(0.1)



window = display.set_mode((1280,720))

window.fill((152,209,250))

#margem 
margem_esquerda = 1
margem_direita = 1050 
margem_topo = 50
margem_base = 720 - 50

#nuvem andando
nuvem_x = 400
velocidade = 2


# definir
running = True

while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False

    #desenhar a partir daqui
     # NUVEM ANDANDO
    window.fill((151, 209, 250))


    # Movimento da nuvem com margens
    if nuvem_x > margem_direita:
        velocidade = -2
    if nuvem_x < margem_esquerda - 200: 
        velocidade = 2
    nuvem_x += velocidade
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
    draw.circle(window,(255, 255, 255), (nuvem_x, 100), 50)
    draw.circle(window,(255, 255, 255), (nuvem_x + 65, 100), 50)
    draw.circle(window,(255, 255, 255), (nuvem_x + 130, 100), 50)
    draw.circle(window,(255, 255, 255), (nuvem_x + 195, 100), 50)

    # Árvore
    draw.rect(window, (139, 69, 19), (900, 500, 30, 120))  
    draw.circle(window, (34, 139, 34), (915, 470), 80)  

    # Arroz
    window.blit(arroz_img,(1010, 390))

    #desenhar texto:
    window.blit(newton_text,(750, 650))

    # Oito linhas em volta do sol
    draw.line(window, (255, 255, 0), (200, 60), (200, 120), 7)   
    draw.line(window, (255, 255, 0), (200, 200), (200, 250), 7) 
    draw.line(window, (255, 255, 0), (150, 150), (100, 150), 7)  
    draw.line(window, (255, 255, 0), (250, 150), (300, 150), 7) 
    draw.line(window, (255, 255, 0), (170, 120), (120, 70), 7)  
    draw.line(window, (255, 255, 0), (230, 120), (280, 70), 7)  
    draw.line(window, (255, 255, 0), (170, 180), (120, 230), 7) 
    draw.line(window, (255, 255, 0), (230, 180), (280, 230), 7)

    music.play()
    display.update()
