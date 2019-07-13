import pygame
# from player import player

pygame.init()

# Colors
black       = (0, 0, 0)
white       = (255, 255, 255)
pink        = (255, 90, 90)
light_blue  = (180, 180, 255)

# Display/Window dimensions and settings
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('MyGame')
clock = pygame.time.Clock()

# Player width and looks
player_sprite = pygame.image.load('./sprites/characters/player64.png')
player_width = 64


def player(x, y):
    gameDisplay.blit(player_sprite, (x, y))


def gameLoop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)
        player(x, y)
        if x > display_width - player_width or x < 0:
            gameExit = True

        pygame.display.update()
        clock.tick(60)


gameLoop()
pygame.quit()
quit()
