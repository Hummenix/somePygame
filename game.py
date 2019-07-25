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


class main:

    class enemy:
        def __init__(self):
            self.id = random.randrange(0, 100)
            self.internal_enemy_x = 0
            self.internal_enemy_y = 0
            self.internal_enemy_width = 0
            self.internal_enemy_height = 0
            self.internal_enemy_color = project_colors.light_blue

        def enemy(self, enemy_x, enemy_y, enemy_width, enemy_height, enemy_color):
            self.enemy_x = enemy_x
            self.enemy_y = enemy_y
            self.enemy_width = enemy_width
            self.enemy_height = enemy_height
            self.enemy_color = enemy_color
            pygame.draw.rect(gameDisplay, self.enemy_color,
                             [self.enemy_x, self.enemy_y,
                              self.enemy_width, self.enemy_height])
            return self

    @staticmethod
    def player(x, y):
        gameDisplay.blit(player_sprite, (x, y))

    @staticmethod
    def message_display(text, height):
        largeText = pygame.font.Font('freesansbold.ttf', 40)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((display_width / 2), height)
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()

    def gameResetAction(self, text):
        self.message_display(text, text_height_center)

        time.sleep(3)
        self.gameLoop()

    def returnHighScore(self, score):
        self.message_display("Your Highscore is " + str(score), text_height_top)

    @staticmethod
    def scoreCounter(score):
        font = pygame.font.SysFont(None, 30)
        text = font.render("Score: " + str(score), True, project_colors.black)
        gameDisplay.blit(text, (0, 0))

    def gameLoop(self):
        x = (display_width * 0.45)
        y = (display_height * 0.8)
        x_change = 0
        player_speed = 7
        enemy_start_x = random.randrange(0, display_width)  # -enemy_width)
        enemy_start_y = -500
        # TODO: make speed a per-enemy variable
        enemy_speed = 4
        enemy_width = 100
        enemy_height = 100
        enemy_list = []
        enemy_number = 2
        enemy_color = project_colors.light_gray
        for each in range(0, enemy_number):
            enemy = self.enemy()
            # enemy(enemy_x, enemy_y, enemy_width, enemy_height, enemy_color):
            enemy_list.append(enemy.enemy(enemy_start_x, enemy_start_y, enemy_width, enemy_height, enemy_color))
            print(str(enemy.id))

        score = 0

        self.scoreCounter(score)
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
                        x_change = 0-player_speed
                    elif event.key == pygame.K_RIGHT:
                        x_change = player_speed
                # if button is released
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

            # change horizontal position
            x += x_change
            gameDisplay.fill(project_colors.light_blue)
            # enemy(enemy_x, enemy_y, enemy_width, enemy_height, enemy_color)
            prev_enemy_x = -1  # identification
            for enemy in enemy_list:
                enemy.enemy_y += enemy_speed
                enemy.enemy(enemy.enemy_x, enemy.enemy_y, enemy.enemy_width, enemy.enemy_height, enemy.enemy_color)

                if enemy.enemy_y > display_height:
                    enemy.enemy_y = 0 - enemy.enemy_height
                    print("enemy width: " + str(enemy.enemy_width))
                    # TODO: make enemies not overlap by at least 1px
                    #  (enemy_x shouldn't be in range of enemy_x to enemy_x += enemy_width)
                    valid_position = False
                    # -1 is an invalid value set for identification
                    if prev_enemy_x == -1:
                        enemy.enemy_x = random.randrange(0, display_width - int(enemy.enemy_width))
                        #prev_enemy_x = enemy.enemy_x
                        #prev_enemy_width = enemy.enemy_width
                    else:
                        while not valid_position:
                            enemy.enemy_x = random.randrange(0, display_width - int(enemy.enemy_width))


                            margin = 10
                            if (prev_enemy.enemy_x - margin <= enemy.enemy_x <= prev_enemy.enemy_x + margin + prev_enemy.enemy_width
                                    or prev_enemy.enemy_x - margin <= enemy.enemy_x + enemy.enemy_width
                                        <= prev_enemy.enemy_x + margin + prev_enemy.enemy_width):
                                pass
                            else:
                                valid_position = True
                    prev_enemy = enemy

                    score += 1
                    print("Score: " + str(score))
                    if enemy_speed < 15:
                        enemy_speed += 0.2
                    print("enemy speed:" + str(enemy_speed))
                    if enemy.enemy_width >= 165:
                        enemy.enemy_width = 165
                    else:
                        enemy.enemy_width += (score * 0.1)

                if y < enemy.enemy_y + enemy.enemy_height and y + player_height > enemy.enemy_y:
                    # print("y-coordinate crossover")
                    if enemy.enemy_x < x < enemy.enemy_x + enemy.enemy_width \
                            or enemy.enemy_x  < x + player_width < enemy.enemy_x + enemy.enemy_width:
                        print(
                            "Enemy hit \nPlayer position: " + str(x) + " to " + str(x + player_width) + " at height " +
                            str(y) + "\nEnemy position: " + str(enemy.enemy_x) + " to " +
                            str(enemy.enemy_x + enemy.enemy_width)
                            + " at height " + str(enemy.enemy_y))
                        self.returnHighScore(score)
                        self.gameResetAction("You collided with an enemy.")

            self.player(x, y)
            self.scoreCounter(score)

            # if player is at border
            if x > display_width - player_width or x < 0:
                self.gameResetAction("You exited the game area. Restarting.")

            pygame.display.update()
            clock.tick(60)


main().gameLoop()
pygame.quit()
quit()
