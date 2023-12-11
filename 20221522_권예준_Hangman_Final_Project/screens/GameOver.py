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
from utils.assets_manager import assetsManager

class GameOver(Game):
    def __init__(self,score,word = "WORD"):
        sounds.playMusic()
        self.gameObjects = []
        self.hangMan = HangMan(80,480,11)
        self.wordGenerator = WordGenerator((800/2) - (len(word) * 40 / 2),80,True)
        self.wordGenerator.currentWord = word

        self.buttons = []
        self.buttons.append(Button(0, Vector2(500, 240), "Restart", Vector2(3, 2)))
        self.buttons.append(Button(1, Vector2(500, 340), "Menu", Vector2(3, 2)))
        self.buttons.append(Button(2, Vector2(500, 440), "Quit", Vector2(3, 2)))

        self.score = score
        utils.saveScore(score)

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
        self.hangMan.draw()
        self.wordGenerator.draw()

        for button in self.buttons:
            button.draw()

        utils.drawText(Vector2(450, 150), "Scores: " + str(self.score), (233, 23, 233), utils.font24)
        utils.drawText(Vector2(250, 150), "Game Over!", (233, 23, 23), utils.font24)



    def onKeyDown(self, key):
        pass

    def onKeyUp(self, key):
        pass

    def onMouseDown(self, event):
        for button in self.buttons:
            button.onMouseDown()
            if button.clicked:
                if button.id == 0:
                    from screens.SelectDifficult import SelectDifficult
                    utils.currentScreen = SelectDifficult()
                    break
                if button.id == 1:
                    from screens.MainMenu import MainMenu
                    utils.currentScreen = MainMenu()
                    break
                if button.id == 2:
                    exit(1)

    def onMouseUp(self, event):
        for button in self.buttons:
            button.onMouseUp()

    def onMouseWheel(self, event):
        pass

