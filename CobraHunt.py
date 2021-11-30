import pygame
import random
import os
from typing import List
 

pygame.init()

window_width: int = 800
window_height: int = 600

class Duck:
    x: int = 0
    y: int = 0
    speed: int = 1
    sprite: pygame.Surface

    def __init__(self, sprite):
        self.y = random.randint(0, window_height)
        self.sprite = sprite

    def move(self):
        self.x += self.speed
    
    def display(self, window: pygame.Surface):
        window.blit(self.sprite, (self.x, self.y))

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
            if pygame.mouse.get_pressed(3)[0]:
                print("button 0 pressed at ", end='')
            if pygame.mouse.get_pressed(3)[1]:
                print("button 1 pressed at ", end='')
            if pygame.mouse.get_pressed(3)[2]:
                print("button 2 pressed at ", end='')
            print(pygame.mouse.get_pos()[0], " ", pygame.mouse.get_pos()[1])
    window.fill((0, 0, 0, 255))
    for duck in DuckList:
        duck.move()
        duck.display(window)
    pygame.display.update()
    clock.tick(60)
