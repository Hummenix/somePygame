import pygame

pygame.init()


display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('MyGame')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False

playerSprite = pygame.image.load('./sprites/characters/player.')

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
