import sys
import os
base_path = os.path.dirname(__file__)
src_path = os.path.join(base_path, "..", "src")
sys.path.append(src_path)

import pygame

from core.game import Game
from core.scene import Scene
from core.UIText import UIText

from character import Character, CharacterCollider
from terrain import Terrain
from mainCamera import MainCamera

def main():

    cam = MainCamera(0, 0)

    scene = Scene("Scene1", cam)
    scene.addGameObject(cam)
    
    
    character = Character(0, -250, 32 * 2, 32 * 2, 0, [])
    scene.addGameObject(character)
    
    cam.referenceObject = character

    terrainSprite = pygame.image.load(os.path.join(base_path, "assets", "Terrain", "terrain.png"))
    
    terrain1 = Terrain(-160, 150, 160*2, 48*2, 0, terrainSprite)
    scene.addGameObject(terrain1)

    terrain2 = Terrain(-160, -150, 160*2, 48*2, 0, terrainSprite)
    scene.addGameObject(terrain2)

    terrain3 = Terrain( 300, 0, 160*2, 48*2, 0, terrainSprite)
    scene.addGameObject(terrain3)

    characterCollider = CharacterCollider(["Terrain"], character)
    scene.addGameObject(characterCollider)

    poquitoText1 = UIText("Poquito", 50, 50, 96, -10, (0,0,0))
    poquitoText2 = UIText("Poquito", 45, 45, 100, -12, (255,255,255))
    scene.addGameObject(poquitoText1)
    scene.addGameObject(poquitoText2)

    game = Game((1280, 720), "Scene1", 60, 100, pygame.NOFRAME , (216,189,155))
    game.run()


main()