from __future__ import annotations


import sys
import pygame
from pygame import Vector2

from utils.util import utils

from utils.Button import Button
from utils.sounds import sounds

from HangMan.AlphabetBtns import AlphabetBtns
from HangMan.GameObject import GameObject
from HangMan.HangMan import HangMan
from HangMan.WordGenerator import WordGenerator
from screens.Game import Game
from screens.GameOver import GameOver
from utils.assets_manager import assetsManager

class HighScores(Game):
    def __init__(self,word = "WORD"):
        self.gameObjects = []

        self.buttons = []
        self.buttons.append(Button(0, Vector2(650, 10), "Menu", Vector2(1.8, 1.2),utils.font16))
        self.scores = utils.loadScores()
        self.scores = self.scores[0:10]

    def update(self):
        pass

    def drawGrid(self):
        blockSize = 40
        for x in range(0, utils.width, blockSize):
            for y in range(0, utils.height, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(utils.screen, (200,200,200), rect, 1)

    def draw(self):
        utils.screen.fill((233, 233, 233), (0, 0, utils.width, utils.height))

        self.drawGrid()

        for button in self.buttons:
            button.draw()

        utils.drawText(Vector2(140, 40), "Top 10 high scores: ", (23, 23, 233), utils.font32)

        y = 100
        x = 250
        i = 1
        for score in self.scores:
            pygame.draw.rect(utils.screen,(23,23,23),(x - 200,y - 10,450,50),2)
            pygame.draw.rect(utils.screen, (23, 23, 23), (x - 200, y - 10, 100, 50), 2)

            utils.drawText(Vector2(x - 150, y), str(i) , (23, 23, 23), utils.font24)
            utils.drawText(Vector2(x, y), str(score), (23, 123, 23), utils.font24)
            y += 48
            i += 1

    def onKeyDown(self, key):
        pass

    def onKeyUp(self, key):
        pass

    def onMouseDown(self, event):
        for button in self.buttons:
            button.onMouseDown()
            if button.clicked:
                if button.id == 0:
                    from screens.MainGame import MainMenu
                    utils.currentScreen = MainMenu()
                    break
                if button.id == 3:
                    exit(1)

    def onMouseUp(self, event):
        for button in self.buttons:
            button.onMouseUp()

    def onMouseWheel(self, event):
        pass

