import pygame
class Dice:
    def __init__(self, number_of_dice):
        self._number_of_dice = number_of_dice
        self._big_font = pygame.font.SysFont("comicsansms", 36)
        self._small_font = pygame.font.SysFont("comicsansms", 25)
    
    def roll_dice(self):
        