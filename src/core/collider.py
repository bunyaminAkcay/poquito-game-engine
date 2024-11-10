import pygame

from .gameObject import GameObject
from .game import Game

from enum import Enum

class CollisionSide(Enum):
    LEFT = 1
    RIGHT = 2
    TOP = 3
    BOTTOM = 4

class Collider(GameObject):

    def __init__(self, collidableTagList : list, referenceObject, offsetRect = (0, 0, 0, 0)):
        super().__init__()
        self.collidedObject = None
        self.collidedSides = []
        self.__collidableTagList = collidableTagList
        self.referenceObject = referenceObject
        self.__offsetRect = offsetRect
        self.collidedLeftLen = 0
        self.collidedRightLen = 0
        self.collidedTopLen = 0
        self.collidedBottomtLen = 0

    def onCollide(self):
        pass

    def fixedUpdate(self):
        referenceRect = self.referenceObject.getRect()
        referenceRectWithOffset = pygame.Rect(  referenceRect.x + self.__offsetRect[0],
                                                referenceRect.y + self.__offsetRect[1],
                                                referenceRect.width + self.__offsetRect[2],
                                                referenceRect.height + self.__offsetRect[3])
        for gameObject in Game.getScene().gameObjects:
            if (gameObject.getTag() in self.__collidableTagList) and referenceRectWithOffset.colliderect(gameObject.getRect()):
                self.collidedObject = gameObject
                self.__detectCollisionSides(referenceRectWithOffset, gameObject.getRect())
                self.onCollide()
                break
    

    def __detectCollisionSides(self, referenceRect, targetRect):
        self.collidedSides = []  # Reset collided sides
        if referenceRect.right > targetRect.left and referenceRect.left < targetRect.left:
            self.collidedSides.append(CollisionSide.RIGHT)
            self.collidedRightLen = referenceRect.right - targetRect.left
        else:
            self.collidedRightLen = 0

        if referenceRect.left < targetRect.right and referenceRect.right > targetRect.right:
            self.collidedSides.append(CollisionSide.LEFT)
            self.collidedLeftLen = targetRect.right - referenceRect.left
        else:
            self.collidedLeftLen = 0

        if referenceRect.bottom > targetRect.top and referenceRect.top < targetRect.top:
            self.collidedSides.append(CollisionSide.TOP)
            self.collidedTopLen = referenceRect.bottom - targetRect.top
        else:
            self.collidedTopLen = 0
        
        
        if referenceRect.top < targetRect.bottom and referenceRect.bottom > targetRect.bottom:
            self.collidedSides.append(CollisionSide.BOTTOM)
            self.collidedBottomLen = targetRect.bottom - referenceRect.top
        else:
            self.collidedBottomLen = 0