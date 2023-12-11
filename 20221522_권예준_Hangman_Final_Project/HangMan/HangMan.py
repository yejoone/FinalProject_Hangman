import pygame

from utils.util import utils


class HangMan():

    def __init__(self,x = 280,y = 280,wrongCount = 0):
        self.wrongCount = wrongCount
        self.x = x
        self.y = y

    def draw(self):

        color = (11,11,11)
        x = self.x
        y = self.y

        if self.wrongCount > 0:
            pygame.draw.line(utils.screen, color, (x, y), (x + 80, y),width= 5)

        if self.wrongCount > 1:
            pygame.draw.line(utils.screen, color, (x + 40, y), (x + 40, y - 240), width=5)

        if self.wrongCount > 2:
            pygame.draw.line(utils.screen, color, (x + 40, y - 180), (x + 120, y - 240), width=5)

        if self.wrongCount > 3:
            pygame.draw.line(utils.screen, color, (x + 40, y - 240), (x + 200, y - 240), width=5)

        if self.wrongCount > 4:
            pygame.draw.circle(utils.screen, color,(x + 200,y - 160), 20, 5)

        if self.wrongCount > 5:
            pygame.draw.line(utils.screen, color, (x + 200, y - 140), (x + 200, y - 80), width=5)

        if self.wrongCount > 6:
            pygame.draw.line(utils.screen, color, (x + 200, y - 140), (x + 240, y - 100), width=5)

        if self.wrongCount > 7:
            pygame.draw.line(utils.screen, color, (x + 200, y - 140), (x + 160, y - 100), width=5)

        if self.wrongCount > 8:
            pygame.draw.line(utils.screen, color, (x + 200, y - 80), (x + 240, y - 40), width=5)

        if self.wrongCount > 9:
            pygame.draw.line(utils.screen, color, (x + 200, y - 80), (x + 160, y - 40), width=5)

        if self.wrongCount > 10:
            pygame.draw.line(utils.screen, color, (x + 200, y - 240), (x + 200, y - 180), width=5)
