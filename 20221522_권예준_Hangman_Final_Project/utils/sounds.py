import pygame
from pygame import mixer

class Sounds:
    def __init__(self):
        mixer.init()
        self.ss = {
            'click': mixer.Sound("assets/clickBtn.wav"),
            'correct': mixer.Sound("assets/correct.wav"),
            'incorrect': mixer.Sound("assets/incorrect.wav"),
        }

    def playMusic(self):
        mixer.music.load("assets/music.mp3")
        mixer.music.play(-1)

    def stopMusic(self):
        mixer.music.stop()

    def play(self, key):
        pygame.mixer.Sound.play(self.ss[key])


sounds = Sounds()
