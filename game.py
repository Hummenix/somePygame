import pygame
import time
# from player import player

pygame.init()

# Colors
black       = (0, 0, 0)
white       = (255, 255, 255)
pink        = (255, 50, 90)
# light_blue  = (180, 180, 255)
light_blue  = (173,216,230)

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


def text_objects(text, font):
    textSurface = font.render(text, True, pink)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 40)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(3)

    gameLoop()


def exitedGameArea():
    message_display('You exited the game area. Restarting.')


def gameLoop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            print(event)
            # If game is intentionally quit
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # if button is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            # if button is released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        # change horizontal position
        x += x_change

        gameDisplay.fill(light_blue)
        player(x, y)
        # if player is at border
        if x > display_width - player_width or x < 0:
            exitedGameArea()
            # gameExit = True

        pygame.display.update()
        clock.tick(60)


gameLoop()
pygame.quit()
quit()
