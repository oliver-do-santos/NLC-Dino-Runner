import random
import pygame

from dino_runner.components.power_ups.shield import Shield

class PowerUpManager:
    def __init__(self):
        self.power_ups =  []
        self.when_appers = 0
        self.soud = pygame.mixer.Sound("dino_runner/components/sound/poder.wav")
    def generate_power_ups(self,points):
        if len(self.power_ups) == 0:
            if self.when_appers == points:
                self.when_appers = random.randint(self.when_appers*200,self.when_appers*300)
                self.power_ups.append(Shield())

    def update(self,points,gamme_speed,player):
        self.generate_power_ups(points)
        for power_up in self.power_ups:
            power_up.update(gamme_speed,self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.shield = True
                player.show_text = True
                player.type = power_up.type
                time_ramdon = random.randint(5,8)
                player.shield_time_up = power_up.start_time + (time_ramdon * 1000)
                self.power_ups.remove(power_up)
                #music on
                self.soud.play()#sonido
                self.soud.set_volume(0.1)
    def draw(self,screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appers = random.randint(50,100)
