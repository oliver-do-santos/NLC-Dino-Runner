import random
import pygame

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.components.bird import Bird

class ObstacleManager:

    def __init__(self):    
        self.obstacles = []
        self.soud = pygame.mixer.Sound("dino_runner/components/sound/choque.wav")
    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacle_type_list = [Bird(), Cactus()]
            #small_catus  = Cactus(SMALL_CACTUS)
            #self.obstacles.append(small_catus)
            self.obstacles.append(random.choice(self.obstacle_type_list))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed,self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    # pygame.time.delay(500)
                    # game.playing = False
                    # game.deat_count +=1
                    # #music on
                    # self.soud.play()#sonido
                    # self.soud.set_volume(0.1)
                    #break
                    if not game.player.has_lives:
                        game.player_heart_manager.reduce_heart_count() #vidas descontando

                        self.soud.play()#sonido
                        self.soud.set_volume(0.1)

                        if game.player_heart_manager.heart_count > 0:
                            game.player.has_lives = True
                            self.obstacles.pop()
                            start_transition_time = pygame.time.get_ticks()
                            game.player.lives_transition_time = start_transition_time + 1000

                        else:
                            # pygame.time.delay(500)
                            game.playing = False 
                            game.deat_count += 1# contador
                            game.player_heart_manager.heart_count = 6
                            break 
                # else:
                #     self.obstacles.remove(obstacle)
                #     break
            
    def draw(self ,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):        
        self.obstacles = []