import pygame 

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS

class ObstacleManager:
    
    def __init__(self):    
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            small_catus  = Cactus(SMALL_CACTUS)
            self.obstacles.append(small_catus)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed,self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                game.deat_count +=1
                break
            
    def draw(self ,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles():        
        self.obstacles = []