import pygame
import time
from text import text_objects
import project_colors
import random
# from player import player

pygame.init()

# Display/Window dimensions and settings
# TODO: export as many functions and variables as possible
display_width   = 800
display_height  = 800
gameDisplay     = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('MyGame')
clock = pygame.time.Clock()

text_height_top     = display_height/6
text_height_center  = display_height/2

# Player width and looks
player_sprite   = pygame.image.load('./sprites/characters/player64.png')
player_width    = 64
player_height   = 64


def enemy(enemy_x, enemy_y, enemy_width, enemy_height, enemy_color):
    pygame.draw.rect(gameDisplay, enemy_color, [enemy_x, enemy_y, enemy_width, enemy_height])


def player(x, y):
    gameDisplay.blit(player_sprite, (x, y))


def message_display(text, height):
    largeText = pygame.font.Font('freesansbold.ttf', 40)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (height))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()


def exitedGameArea():
    message_display('You exited the game area. Restarting.', text_height_center)

    time.sleep(3)
    gameLoop()


def collidedWithEnemy():
    message_display('You collided with an enemy.', text_height_center)

    time.sleep(3)
    gameLoop()


def returnHighScore(score):
    message_display("Your Highscore is " + str(score), text_height_top)


def scoreCounter(score):
    font = pygame.font.SysFont(None, 20)
    text = font.render("Score: " + str(score), True, project_colors.black)
    gameDisplay.blit(text, (0, 0))


def gameLoop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    enemy_start_x = random.randrange(0, display_width)  # -enemy_width)
    enemy_start_y = -500
    enemy_speed = 20
    enemy_width = 100
    enemy_height = 100
    score = 0
    scoreCounter(score)
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
        gameDisplay.fill(project_colors.light_blue)
        # enemy(enemy_x, enemy_y, enemy_width, enemy_height, enemy_color)
        enemy_start_y += enemy_speed
        enemy(enemy_start_x, enemy_start_y, enemy_width, enemy_height, project_colors.light_gray)
        player(x, y)

        # if player is at border
        if x > display_width - player_width or x < 0:
            exitedGameArea()

        if enemy_start_y > display_height:
            enemy_start_y = 0 - enemy_height
            enemy_start_x = random.randrange(0, display_width-int(enemy_width))
            score += 1
            scoreCounter(score)
            print("Score: " + str(score))
            enemy_speed += 0.1
            enemy_width += (score * 0.2)

        if y < enemy_start_y + enemy_height and y + player_height > enemy_start_y:
            # print("y-coordinate crossover")
            # below if statement can be simplified bot this way it's more descriptive
            if enemy_start_x < x < enemy_start_x + enemy_width \
                    or enemy_start_x < x + player_width < enemy_start_x + enemy_width:
                # DEBUG: print("Enemy hit \nPlayer position: " + str(x) + " to " + str(x + player_width) + " at height "
                # + str(y) + "\nEnemy position: " + str(enemy_start_x) + " to " + str(enemy_start_x + enemy_width) +
                # " at height " + str(enemy_start_y))
                # print("collision")
                returnHighScore(score)
                collidedWithEnemy()

        pygame.display.update()
        clock.tick(60)


gameLoop()
pygame.quit()
quit()
