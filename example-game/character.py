import sys
import os
sys.path.append(os.path.abspath("../src"))

from core.animatedObject import AnimatedObject
import pygame
from core.animation import Animation
from core.collider import Collider, CollisionSide
from core.game import Game

class Character(AnimatedObject):

    def init(self):
        self.velocityY = 0
        self.velocityX = 0
        self.gravity = 0.2
        self.speed = 1
        self.maxSpeed = 7
        self.jumpPower = 8
        self.idleSpeed = 1
        self.collidedBottom = False
        self.collidedTop = False
        self.collidedHorizantal = False
        self.setTag("Character")

        idleSpriteSheet = pygame.image.load("assets/character/Idle.png")
        idleAnimation = Animation( Animation.spriteSheetToImageList(idleSpriteSheet, 32, 32, 11), 50)
        
        runSpriteSheet = pygame.image.load("assets/character/Run.png")
        runAnimation = Animation( Animation.spriteSheetToImageList(runSpriteSheet, 32, 32, 12), 50)

        jumpSprite = pygame.image.load("assets/character/Jump.png")
        jumpAnimation = Animation( [jumpSprite], 50)

        fallSprite = pygame.image.load("assets/character/Fall.png")
        fallAnimation = Animation( [fallSprite], 50)

        self.setAnimations([idleAnimation, runAnimation, jumpAnimation, fallAnimation])
    

    def update(self):
        super().update()
        keys = pygame.key.get_pressed()

        jumped = False

        if keys[pygame.K_UP] and self.collidedBottom:
            self.velocityY -= self.jumpPower
            jumped = True
        
        if keys[pygame.K_RIGHT]:
            self.velocityX += self.speed
        elif keys[pygame.K_LEFT]:
            self.velocityX -= self.speed
        else:
            self.velocityX *= 0.9
        

        if self.collidedBottom and jumped == False:        
            self.velocityY = 0
        else:    
            self.velocityY += self.gravity
        
        if self.collidedHorizantal and self.collidedBottom == False:        
            self.velocityX = 0
        
        if self.velocityX > self.maxSpeed:
            self.velocityX = self.maxSpeed
        elif self.velocityX < - self.maxSpeed:
            self.velocityX = -self.maxSpeed

        self.x += self.velocityX
        self.y += self.velocityY

        if self.collidedBottom and self.velocityX < self.idleSpeed:
            self.currentAnimationIndex = 0
        elif self.collidedBottom and self.velocityX >= self.idleSpeed:
            self.currentAnimationIndex = 1
        elif self.velocityY < 0:
            self.currentAnimationIndex = 2
        else:
            self.currentAnimationIndex = 3

        if self.velocityX > 0:
            self.flipX = False
        elif self.velocityX < 0:
            self.flipX = True

        self.collidedBottom = False
        self.collidedTop = False
        self.collidedHorizantal = False

class CharacterCollider(Collider):
    
    def onCollide(self):
        
        if ((CollisionSide.LEFT in self.collidedSides) or (CollisionSide.RIGHT in self.collidedSides)):
            self.referenceObject.collidedHorizantal = True
        
        if (CollisionSide.TOP in self.collidedSides):
            self.referenceObject.collidedBottom = True
            self.referenceObject.velocityY = 0
            self.referenceObject.y -= self.collidedTopLen -1
        
        if (CollisionSide.BOTTOM in self.collidedSides): 
            self.referenceObject.collidedTop = True
            self.referenceObject.velocityY = 0
            self.referenceObject.y -= self.collidedTopLen -1
            

        
        