import pygame
import random
import os
from typing import List
 

pygame.init()

window_width: int = 800
window_height: int = 600

class Duck:
    x: int = -1000
    y: int = -1000
    width : int = 0
    height : int = 0
    speed: int = 0
    sprite: pygame.Surface

    def __init__(self, sprite):
        self.sprite = sprite
        self.width = sprite.get_width()
        self.height = sprite.get_height()
        self.x = -self.width
        self.y = random.randint(0, window_height - self.height)
        self.speed = 10

    def move(self) -> None:
        self.x += self.speed

    def display(self, window) -> None:
        window.blit(self.sprite, (self.x, self.y))

    def contains(self, mouse_x: int, mouse_y: int) -> bool:
        if self.x <= mouse_x and mouse_x <= self.x + self.width and self.y <= mouse_y and mouse_y <= self.y + self.height:
            return True
        return False

loop: bool = True

window = pygame.display.set_mode((window_width, window_height))

duckSprite = pygame.image.load(os.path.join("assets", "duck.png"))
background = pygame.image.load(os.path.join("assets", "background.png"))

font = pygame.freetype.Font(os.path.join("assets", "font.ttf"), 24)
text : pygame.Surface
clock = pygame.time.Clock()

score = 0
DuckList: List[Duck] = []

while loop == True:
    clock.tick(40)
    if len(DuckList) == 0:
        DuckList.append(Duck(duckSprite))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for duck in DuckList:
                if duck.contains(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    score += 100
                    DuckList.remove(duck)
    window.blit(background, (0, 0))
    text, rect = font.render(f"Score: {score}", (250, 253, 15))
    window.blit(text, (620, 520))
    for duck in DuckList:
        duck.move()
        duck.display(window)
        if duck.x >= 800:
            score -= 100
            DuckList.remove(duck)
    pygame.display.update()

pygame.quit()
exit(0)