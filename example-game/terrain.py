import sys
import os
base_path = os.path.dirname(__file__)
src_path = os.path.join(base_path, "..", "src")
sys.path.append(src_path)

from core.spriteObject import SpriteObject
import pygame


class Terrain(SpriteObject):
    
    def init(self):
        self.setTag("Terrain")
