import pygame


class AssetsManager:
    def __init__(self):
        self.assets = {
            'button': pygame.image.load("assets/btn.png").convert_alpha(),
            'clickButton': pygame.image.load("assets/clickBtn.png").convert_alpha(),
        }

    def get(self, key):
        return self.assets[key]


assetsManager = AssetsManager()
