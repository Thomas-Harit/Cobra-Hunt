import pygame
import random
from typing import List

pygame.init()

window_width: int = 800
window_height: int = 600

class Duck:
    x: int = 0
    y: int = 0
    speed: int = 0

    def __init__(self):
        self.y = random.randint(0, window_height)

    def move(self):
        self.x += self.speed

loop: bool = True

window = pygame.display.set_mode((window_width, window_height))

score = 0
DuckList: List[Duck] = []
while loop == True:
    print("JE LOOP")
    loop = False