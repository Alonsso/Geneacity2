import pygame

def IniciarJuego():
    pygame.init()
    
    # Create the game window
    vtnJuego = pygame.display.set_mode((800,800))
    pygame.display.set_caption("GeneaCity")
    clock = pygame.time.Clock()

    # Load images for the map and the player character
    imgMapa = pygame.image.load("imagenes/mpa2.png").convert_alpha()
    imgHombre = pygame.image.load("imagenes/hombre3.png").convert_alpha()

    # Get the rectangle for the player character
    rectHombre = imgHombre.get_rect()

    def jugador():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            # Draw the map and the player character
            vtnJuego.blit(imgMapa, (0, 0))
            vtnJuego.blit(imgHombre, rectHombre)

            # Move the player character based on key presses
            tecla = pygame.key.get_pressed()
            if tecla[pygame.K_a]:
                rectHombre.x -= 5
            if tecla[pygame.K_d]:
                rectHombre.x += 5
            if tecla[pygame.K_w]:
                rectHombre.y -= 5
            if tecla[pygame.K_s]:
                rectHombre.y += 5

            pygame.display.update()
            clock.tick(60)

    jugador()

# Remove or comment out the call to IniciarJuego() here
# IniciarJuego()  # Commented out to prevent the game from starting automatically
