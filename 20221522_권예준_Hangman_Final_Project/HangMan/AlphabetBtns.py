from pygame import Vector2

from utils.Button import Button
from utils.util import utils


class AlphabetBtns:
    def __init__(self):



        self.buttons = []
        x = 270
        y = 440
        
        font = utils.font48

        self.buttons.append(Button(0, Vector2(40 + x + 40 * 0, y - 40), "A", Vector2(0.5, 1.2), font))
        self.buttons.append(Button(0, Vector2(40 + x + 40 * 1, y - 40), "E", Vector2(0.5, 1.2), font))
        self.buttons.append(Button(0, Vector2(40 + x + 40 * 2, y - 40), "I", Vector2(0.5, 1.2), font))
        self.buttons.append(Button(0, Vector2(40 + x + 40 * 3, y - 40), "O", Vector2(0.5, 1.2), font))
        self.buttons.append(Button(0, Vector2(40 + x + 40 * 4, y - 40), "U", Vector2(0.5, 1.2), font))

        self.buttons.append(Button(0, Vector2(x + 40 * 0, y), "B", Vector2(0.5, 1.2), font))
        self.buttons.append(Button(0, Vector2(x + 40 * 1, y), "C", Vector2(0.5, 1.2), font))
        self.buttons.append(Button(0, Vector2(x + 40 * 2, y), "J", Vector2(0.5, 1.2), font))
        self.buttons.append(Button(0, Vector2(x + 40 * 3, y), "K", Vector2(0.5, 1.2), font))
        self.buttons.append(Button(0, Vector2(x + 40 * 4, y), "Q", Vector2(0.5, 1.2), font))
        self.buttons.append(Button(0, Vector2(x + 40 * 5, y), "R", Vector2(0.5, 1.2), font))
        self.buttons.append(Button(0, Vector2(x + 40 * 6, y), "X", Vector2(0.5, 1.2), font))

        self.buttons.append(Button(0, Vector2(x + 40 * 0, y + 40), "D", Vector2(0.5, 1.2), font))
        self.buttons.append(Button(0, Vector2(x + 40 * 1, y + 40), "F", Vector2(0.5, 1.2), font))
        self.buttons.append(Button(0, Vector2(x + 40 * 2, y + 40), "L", Vector2(0.5, 1.2), font))
        self.buttons.append(Button(0, Vector2(x + 40 * 3, y + 40), "M", Vector2(0.5, 1.2), font))
        self.buttons.append(Button(0, Vector2(x + 40 * 4, y + 40), "S", Vector2(0.5, 1.2), font))
        self.buttons.append(Button(0, Vector2(x + 40 * 5, y + 40), "T", Vector2(0.5, 1.2), font))
        self.buttons.append(Button(0, Vector2(x + 40 * 6, y + 40), "Y", Vector2(0.5, 1.2), font))

        self.buttons.append(Button(0, Vector2(x + 40 * 0, y + 40 * 2), "G", Vector2(0.5, 1.2), font))
        self.buttons.append(Button(0, Vector2(x + 40 * 1, y + 40 * 2), "H", Vector2(0.5, 1.2), font))
        self.buttons.append(Button(0, Vector2(x + 40 * 2, y + 40 * 2), "N", Vector2(0.5, 1.2), font))
        self.buttons.append(Button(0, Vector2(x + 40 * 3, y + 40 * 2), "P", Vector2(0.5, 1.2), font))
        self.buttons.append(Button(0, Vector2(x + 40 * 4, y + 40 * 2), "V", Vector2(0.5, 1.2), font))
        self.buttons.append(Button(0, Vector2(x + 40 * 5, y + 40 * 2), "W", Vector2(0.5, 1.2), font))
        self.buttons.append(Button(0, Vector2(x + 40 * 6, y + 40 * 2), "Z", Vector2(0.5, 1.2), font))


    def draw(self):
        for button in self.buttons:
            button.draw()
