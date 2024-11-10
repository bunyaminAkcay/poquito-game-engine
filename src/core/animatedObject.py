from .positionalObject import PositionalObject
import pygame

class AnimatedObject(PositionalObject):

    def __init__(self, x, y, width, height, layer : int, animationList, backgroundColor = (0,0,0,0), visibility = True):
        super().__init__(x, y, width, height, layer, backgroundColor, visibility)
        
        self.__animationList = animationList
        self.currentAnimationIndex = 0
        
        self._surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self._surface.fill(backgroundColor)
        if animationList != []:
            self.__scaledImage = pygame.transform.scale(self.__animationList[self.currentAnimationIndex].getCurrentImage(), (width, height))
            self._surface.blit(self.__scaledImage, (0,0))

    def _updateScale(self, zoom):
        self._surface.fill(self._backgroundColor)
        if self.__animationList != []:
            self.__scaledImage = pygame.transform.scale(self.__animationList[self.currentAnimationIndex].getCurrentImage(), (int(self.width * zoom), int(self.height * zoom)))
            self._surface.blit(self.__scaledImage, (0, 0))
            if self.flipX == True or self.flipY == True:
                self._surface = pygame.transform.flip(self._surface, self.flipX, self.flipY)
        self._surface = pygame.transform.scale(self._surface, (int(self.width * zoom), int(self.height * zoom)) )
    
    def update(self):
        
        if self.__animationList != [] and self.__animationList[self.currentAnimationIndex].clock.checkTickable() == True:
            scaledImageSize = self.__scaledImage.get_size()
            self._surface.fill(self._backgroundColor)
            self.__scaledImage = pygame.transform.scale(self.__animationList[self.currentAnimationIndex].getCurrentImage(), (scaledImageSize))
            self._surface.blit(self.__scaledImage, (0, 0))
            self._surface = pygame.transform.scale(self._surface, (scaledImageSize) )
            if self.flipX == True or self.flipY == True:
                self._surface = pygame.transform.flip(self._surface, self.flipX, self.flipY)
        
    
    def setAnimations(self, animationList):
        self.__animationList = animationList
        self.__scaledImage = pygame.transform.scale(self.__animationList[self.currentAnimationIndex].getCurrentImage(), (self.width, self.height))
        self._surface.blit(self.__scaledImage, (0,0))