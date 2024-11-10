import sys
import os
base_path = os.path.dirname(__file__)
src_path = os.path.join(base_path, "..", "src")
sys.path.append(src_path)

import pygame
from core.camera import Camera


class MainCamera(Camera):

    def setReferenceObject(self, referenceObject):
        self.referenceObject = referenceObject

    def update(self):
        self.centerX = self.referenceObject.x
        self.centerY = self.referenceObject.y

        keys = pygame.key.get_pressed()

        if keys[pygame.K_KP_PLUS]:
            self.zoom(1.01)
        elif keys[pygame.K_KP_MINUS]:
            self.zoom(0.99)