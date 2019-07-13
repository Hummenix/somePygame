import pygame

pygame.init()


display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('MyGame')

black = (0, 0, 0)
white = (255, 255, 255)
pink  = (255, 90, 90)
light_blue = (180, 180, 255)

clock = pygame.time.Clock()
crashed = False

playerSprite = pygame.image.load('./sprites/characters/player.png')


def car(x, y):
    gameDisplay.blit(playerSprite, (x, y))


x = (display_width * 0.01)
y = (display_height * 0.01)


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    gameDisplay.fill(white)
    car(x, y)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
