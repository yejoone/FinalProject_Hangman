
import pygame
import math
from pygame.locals import *

from pygame import Vector2, mixer, time

from utils.sounds import sounds


class Utils():

    def __init__(self):

        pygame.init()

        self.width = 800
        self.height = 600

        self.gameOver = False
        self.currentLevel = 0
        self.screen = pygame.display.set_mode((self.width, self.height), DOUBLEBUF, 16)
        pygame.display.set_caption("Hang man")
        self.dt = 0
        self.clock = pygame.time.Clock()

        self.currentScreen = None

        self.fps = 0
        self.fpsCounter = 0
        self.fpsTimeCount = 0

        self.font8 = pygame.font.Font('assets/Unicorn.ttf', 8)
        self.font12 = pygame.font.Font('assets/Unicorn.ttf', 12)
        self.font16 = pygame.font.Font('assets/Unicorn.ttf', 16)
        self.font24 = pygame.font.Font('assets/Unicorn.ttf', 24)
        self.font32 = pygame.font.Font('assets/Unicorn.ttf', 32)
        self.font48 = pygame.font.Font('assets/Unicorn.ttf', 48)

        self.camera = Vector2(0, 900)
        self.mousePos = Vector2(0,0)

        # world grid, path finding global variables
        self.rows = 100
        self.cols = 50
        self.grid = None
        self.astar = None

    def initDeltaTime(self):  # calculate deltaTime
        t = self.clock.tick(60)
        self.dt = t / 1000

    def deltaTime(self):
        return self.dt

    def showFps(self):
        self.fpsTimeCount += self.deltaTime()
        self.fpsCounter += 1
        if self.fpsTimeCount > 1:
            self.fpsTimeCount = 0
            self.fps = self.fpsCounter
            self.fpsCounter = 0

        if self.fps >= 50:
            self.drawText(Vector2(0, 0), "fps: " + str(self.fps), (23, 23, 233), self.font16)
        else:
            self.drawText(Vector2(0, 0), "fps: " + str(self.fps), (233, 23, 23), self.font16)

    def drawText(self, pos, text, color, font):  # draw text

        text = font.render(text, True, color)
        self.screen.blit(text, (pos.x, pos.y))

    def distance(self, x1, y1, x2, y2):
        return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) * 1.0)

    def collide(self, a, b):  # aabb 2 box collide check
        rect = a.getRect()
        r = b.getRect()
        if r.x < rect.x + rect.w and r.x + r.w > rect.x and r.y < rect.y + rect.h and r.h + r.y > rect.y:
            return True
        return False

    def rotate(self, surface, angle, pivot, offset):
        rotated_image = pygame.transform.rotozoom(surface, -angle, 1)
        rotated_offset = offset.rotate(angle)
        rect = rotated_image.get_rect(center=pivot + rotated_offset)
        return rotated_image, rect

    def saveScore(self,score):
        f = open("scores.txt", "a")
        f.write(str(score) + "\n")
        print("save")
        f.close()

    def loadScores(self):
        scores = []
        with open('scores.txt') as f:
            lines = f.readlines()
            for line in lines:
                scores.append(int(line))
            f.close()

        scores.sort(reverse=True)
        return scores


utils = Utils()  # util is global object
