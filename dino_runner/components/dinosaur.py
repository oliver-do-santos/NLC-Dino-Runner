
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
        self.soud = pygame.mixer.Sound("dino_runner/components/sound/SaltoEfect.wav")
        
        self.has_lives = False#vidas
        self.lives_transition_time = 0

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
            self.soud.play()#sonido
            self.soud.set_volume(0.1)
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
            #print(self.dino_rect.y)
            self.jump_vel -= 0.8
            #print(self.jump_vel) 

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
        
    def check_invicibility(self,screen):
        if self.shield == True:
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks())/100,2)
            
            #print(time_to_show)
            if time_to_show >= 0 and self.show_text:
                print(time_to_show)    
            else:
                self.shield = False
                self.type = DEFAULT_TYPE
    
    def check_lives(self):#metodos preguntando si tiene vidas
        if self.has_lives:
            transition_time = round((self.lives_transition_time - pygame.time.get_ticks()) / 1000)
            if transition_time < 0:
                self.has_lives = False