import sys
import os
sys.path.append(os.path.abspath("../src"))

from core.spriteObject import SpriteObject
import pygame


class Terrain(SpriteObject):
    
    def init(self):
        self.setTag("Terrain")
