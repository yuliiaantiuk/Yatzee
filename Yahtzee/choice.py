import pygame
from util import black, screen, font
class Choice:
    def __init__(self, x_pos, y_pos, text, select, is_possible, is_done, score1, score2):
        global selected_choice
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.text = text
        self.select = select
        self.is_possible = is_possible
        self.is_done = is_done
        self.score1 = score1
        self.score2 = score2

    def draw(self):
        pygame.draw.line(screen, black, (self.x_pos, self.y_pos), (self.x_pos + 290, self.y_pos), 2)
        pygame.draw.line(screen, black, (self.x_pos, self.y_pos + 30), (self.x_pos + 290, self.y_pos + 30), 2)

        if not self.is_done:
            if self.is_possible:
                my_text = my_text = font.render(self.text, True, (80, 200, 96))
            elif not self.is_possible:
                my_text = my_text = font.render(self.text, True, (250, 0, 55))
        else:
            my_text = font.render(self.text, True, black)
        if self.select:
            pygame.draw.rect(screen, (20, 35, 30), [self.x_pos, self.y_pos, 155, 30])
        screen.blit(my_text, (self.x_pos + 5, self.y_pos + 10))
        score_text1 = font.render(str(self.score1), True, (0, 0, 255))
        screen.blit(score_text1, (self.x_pos + 165, self.y_pos + 10))
        score_text2 = font.render(str(self.score2), True, (0, 0, 255))
        screen.blit(score_text2, (self.x_pos + 238, self.y_pos + 10))