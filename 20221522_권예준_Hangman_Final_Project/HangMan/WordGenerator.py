import random

import pygame
from pygame import Vector2

from utils.util import utils


class WordGenerator():

    def __init__(self,x = 0,y = 0,show = False):
        self.show = show
        self.words = []
        with open('assets/wordlist.txt') as f:
            lines = f.readlines()
            for line in lines:
                word = line.replace("\n", "")
                self.words.append(word)

        self.currentWord = "HELLO"
        self.selected = []

        self.newRandomWord()

        if show:
            self.x = x
            self.y = y

    def newRandomWord(self):
        randIndex = random.randrange(0,len(self.words))
        self.currentWord = self.words[randIndex]
        self.currentWord = self.currentWord.upper()

    def isCorrect(self):
        count = 0
        for character in self.currentWord:
            if self.show or self.selected.__contains__(character):
                count += 1
        return count == len(self.currentWord)

    def draw(self):

        x = (800/2) - (len(self.currentWord) * 40 / 2)
        y = 320
        if self.show:
            x = self.x
            y = self.y

        i = 10
        for character in self.currentWord:
            if self.show or self.selected.__contains__(character):
                utils.drawText(Vector2(x + i,y),character,(23,23,233),utils.font32)
            pygame.draw.line(utils.screen, (23,23,233), (x + i - 8, y + 40), (x + i + 28, y + 40), width=2)
            i += 45
