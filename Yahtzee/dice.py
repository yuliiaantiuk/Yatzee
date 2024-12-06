import pygame
from util import black, white, screen
class Dice:
    def __init__(self, x_pos, y_pos, num, key, player):
        global dice_selected
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.num = num
        self.key = key
        self.die = ''
        self.selected = player.dice_selected[key]
        self.player = player

    def draw(self):
        self.die = pygame.draw.rect(screen, white, [self.x_pos, self.y_pos, 100, 100], 0, 5)
        if self.num == 1:
            pygame.draw.circle(screen, black, [self.x_pos + 50, self.y_pos + 50], 10)
        if self.num == 2:
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 80], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 20], 10)
        if self.num == 3:
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 20], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 50, self.y_pos + 50], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 80], 10)
        if self.num == 4:
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 20], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 80], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 80], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 20], 10)
        if self.num == 5:
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 20], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 80], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 50, self.y_pos + 50], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 80], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 20], 10)
        if self.num == 6:
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 20], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 80], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 50], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 80], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 50], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 20], 10)
        if self.selected:
            self.die = pygame.draw.rect(screen, (255, 0, 0), [self.x_pos, self.y_pos, 100, 100], 4, 5)

    def check_click(self, coordinates):
        if self.die.collidepoint(coordinates):
            if self.player.dice_selected[self.key]:
                self.player.dice_selected[self.key] = False
            elif not self.player.dice_selected[self.key]:
                self.player.dice_selected[self.key] = True