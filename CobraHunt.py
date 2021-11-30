import pygame
import random
import os
from typing import List
 

pygame.init()

window_width: int = 800
window_height: int = 600

class Duck:
    x: int
    y: int
    width : int
    height : int
    speed: int = 1
    sprite: pygame.Surface

    def __init__(self, sprite):
        self.sprite = sprite
        self.width = sprite.get_width()
        self.height = sprite.get_height()
        self.x = -self.width
        self.y = random.randint(0, window_height - self.height)

    def move(self) -> None:
        self.x += self.speed
    
    def display(self, window: pygame.Surface) -> None:
        window.blit(self.sprite, (self.x, self.y))

    def contains(self, x: int, y: int) -> bool:
        if self.x <= x and x <= self.x + self.width and self.y <= y and y <= self.y + self.height:
            return True
        return False

loop: bool = True

window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
duckSprite = pygame.image.load(os.path.join("assets", "duck.png"))
clock = pygame.time.Clock()

score = 0
DuckList: List[Duck] = []

while loop == True:
    if len(DuckList) == 0:
        DuckList.append(Duck(duckSprite))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for duck in DuckList:
                if duck.contains(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    DuckList.remove(duck)
    window.fill((0, 0, 0, 255))
    for duck in DuckList:
        duck.move()
        duck.display(window)
        if duck.x >= 800:
            DuckList.remove(duck)
    pygame.display.update()
    clock.tick(60)
