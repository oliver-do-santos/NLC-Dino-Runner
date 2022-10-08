import random
from dino_runner.components.dinosaur import RUN_IMG 

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self):
        self.type = 0
        self.fly = 0
        super().__init__(BIRD, self.type)
        self.rect.y = random.randint(100, 310)


    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        self.obs_to_draw = BIRD[0] if self.fly < 10 else BIRD[1]
        self.fly += 1
        if self.fly >= 20:
            self.fly = 0
        
        if self.rect.x < -self.rect.width:
            obstacles.pop()
    
    # def update(self):
    #     self.image = BIRD[self.type][self.step_index // 5]
    #     self.dino_rect = self.image.get_rect()
    #     self.dino_rect.x = self.X_POS
    #     self.dino_rect.y = self.Y_POS        
    #     self.step_index += 1