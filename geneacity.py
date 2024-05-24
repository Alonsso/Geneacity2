import pygame

def IniciarJuego():
    pygame.init()
    
    vtnJuego = pygame.display.set_mode((800,800)) 
    pygame.display.set_caption("GeneaCity")
    clock = pygame.time.Clock()
    
    imgMapa = pygame.image.load("imagenes/mpa2.png").convert_alpha()
    imgHombre = pygame.image.load("imagenes/hombre3.png").convert_alpha()
    
    rectHombre = imgHombre.get_rect()

    def jugador():    
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
            vtnJuego.blit(imgMapa, (0, 0))
            vtnJuego.blit(imgHombre, rectHombre) 
                
            tecla = pygame.key.get_pressed()
            if tecla[pygame.K_a] == True:
                rectHombre.x -= 5
            if tecla[pygame.K_d] == True:
                rectHombre.x += 5
            if tecla[pygame.K_w] == True:
                rectHombre.y -= 5
            if tecla[pygame.K_s] == True:
                rectHombre.y += 5
                
            pygame.display.update()
            clock.tick(60)
    jugador()

IniciarJuego()   




    
    
    

