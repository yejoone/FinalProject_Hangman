
import sys

import pygame
from pygame import Vector2

from screens.MainMenu import MainMenu
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


class MainGame(Game):
    def __init__(self,score= 0,difficult=0):
        sounds.stopMusic()

        self.gameObjects = []
        self.hangMan = HangMan()
        self.wordGenerator = WordGenerator()
        self.alphabetBtns = AlphabetBtns()

        self.buttons = []
        self.buttons.append(Button(0, Vector2(650, 10), "Menu", Vector2(1.8, 1.2),utils.font16))

        self.score = score
        self.correct = False
        self.hangMan.wrongCount = difficult
        self.difficult = difficult


    def update(self):

        if self.wordGenerator.isCorrect() and not self.correct:
            self.correct = True
            self.score += 1
            self.buttons.append(Button(1, Vector2(650, 550), "Next", Vector2(1.8, 1.2), utils.font16))
            self.alphabetBtns.buttons = []
            sounds.play("correct")

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

        utils.drawText(Vector2(50, 100), "Scores: " + str(self.score), (233, 23, 233), utils.font32)

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
                    utils.currentScreen = MainGame(score=self.score,difficult=self.difficult)
                    break

        for button in self.alphabetBtns.buttons:
            button.onMouseDown()
            if button.clicked:
                self.alphabetBtns.buttons.remove(button)
                self.wordGenerator.selected.append(button.text)

                if ['A', 'U', 'I', 'E', 'O'].__contains__(button.text):
                    continue

                if not self.wordGenerator.currentWord.__contains__(button.text):
                    self.hangMan.wrongCount += 1
                    sounds.play("incorrect")

                if self.hangMan.wrongCount >= 11:
                    utils.currentScreen = GameOver(self.score,self.wordGenerator.currentWord)
                elif self.hangMan.wrongCount == 10:
                    sounds.playMusic()

    def onMouseUp(self, event):
        for button in self.buttons:
            button.onMouseUp()

        for button in self.alphabetBtns.buttons:
            button.onMouseUp()

    def onMouseWheel(self, event):
        pass

