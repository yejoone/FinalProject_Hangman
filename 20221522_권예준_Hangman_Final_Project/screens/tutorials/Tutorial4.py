
import sys

import pygame
from pygame import Vector2

from screens.MainMenu import MainMenu
from screens.tutorials.Tutorial5 import Tutorial5
from utils.Button import Button
from utils.util import utils


import screens
from utils.sounds import sounds

from HangMan.AlphabetBtns import AlphabetBtns
from HangMan.GameObject import GameObject
from HangMan.HangMan import HangMan
from HangMan.WordGenerator import WordGenerator
from screens.Game import Game
from screens.GameOver import GameOver
from utils.assets_manager import assetsManager


class Tutorial4(Game):
    def __init__(self):


        self.gameObjects = []
        self.hangMan = HangMan()
        self.wordGenerator = WordGenerator()
        self.alphabetBtns = AlphabetBtns()
        self.wordGenerator.currentWord = "CAT"

        self.buttons = []
        self.buttons.append(Button(0, Vector2(650, 10), "Menu", Vector2(1.8, 1.2),utils.font16))
        self.buttons.append(Button(1, Vector2(650, 550), "Next", Vector2(1.8, 1.2), utils.font16))
        self.buttons.append(Button(2, Vector2(50, 550), "Previous", Vector2(1.8, 1.2), utils.font16))

        self.alphabetBtns.buttons.remove(self.alphabetBtns.buttons[6])
        self.alphabetBtns.buttons.remove(self.alphabetBtns.buttons[0])
        self.alphabetBtns.buttons.remove(self.alphabetBtns.buttons[17])
        self.wordGenerator.selected.append('C')
        self.wordGenerator.selected.append('A')
        self.wordGenerator.selected.append('T')


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
        self.alphabetBtns.draw()

        for button in self.buttons:
            button.draw()

        utils.drawText(Vector2(50, 100), "How to play?" , (23, 23, 23), utils.font16)
        utils.drawText(Vector2(50, 400), "2.If the word is correct", (23, 233, 23), utils.font16)
        utils.drawText(Vector2(60, 420), "you win and earn 1 score!", (23, 233, 23), utils.font16)


    def onKeyDown(self, key):
        pass

    def onKeyUp(self, key):
        pass

    def onMouseDown(self, event):
        for button in self.buttons:
            button.onMouseDown()
            if button.clicked:
                if button.id == 0:
                    utils.currentScreen = MainMenu()
                    break
                if button.id == 1:
                    utils.currentScreen = Tutorial5()
                    break
                if button.id == 2:
                        from screens.tutorials.Tutorial3 import Tutorial3
                        utils.currentScreen = Tutorial3()
                        break



    def onMouseUp(self, event):
        for button in self.buttons:
            button.onMouseUp()

        for button in self.alphabetBtns.buttons:
            button.onMouseUp()

    def onMouseWheel(self, event):
        pass

