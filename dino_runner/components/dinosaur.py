
import pygame

from dino_runner.utils.constants import  DUCKING, JUMPING_SHIELD, RUNNING, JUMPING, DEFAULT_TYPE, RUNNING_SHIELD, SHIELD_TYPE,DUCKING_SHIELD
from pygame.sprite import Sprite

DUCK_IMG = {DEFAULT_TYPE: DUCKING ,SHIELD_TYPE:DUCKING_SHIELD}
JUMP_IMG = {DEFAULT_TYPE: JUMPING ,SHIELD_TYPE:JUMPING_SHIELD}
RUN_IMG =  {DEFAULT_TYPE: RUNNING ,SHIELD_TYPE:RUNNING_SHIELD}

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.duck_img =  DUCKING
        self.jump_vel = self.JUMP_VEL
        self.setup_state ()

    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.show_text = False
        self.shield_time_up = 0

    def execute_dino(self):        #movido
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck: 
            self.duck()

    def update(self,user_input):                
        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False 
            self.dino_jump = False
        elif not self.dino_jump:
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck = False
        
        if self.step_index >= 10:
            self.step_index = 0

    def jump(self):
        self.image = JUMP_IMG[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            print(self.dino_rect.y)
            self.jump_vel -= 0.8
            print(self.jump_vel) 

        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL 

    def duck(self): #saltar
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.dino_rect.y = self.Y_POS + 40
        self.step_index +=1

    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS        
        self.step_index += 1
        
    def draw(self,screen: pygame.Surface):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        
    def check_invicibility(self):
        pass