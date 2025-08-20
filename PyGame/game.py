import pygame as pg

class Game:
    def __init__(self):
        self.ground = 300
        self.player = Dinossaur(50,100)

    def jump(self):
        self.player.jump()

    def update(self):
        self.player.update()
        if(self.player.y + self.player.h + self.player.speed_y >= self.ground):
            self.player.jumping = False
            self.player.y = self.ground - self.player.h
    
    def render(self, window):
        pg.draw.rect(window, (60,60,60), pg.Rect(0,self.ground,700,200))
        self.player.render(window)

class Dinossaur:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 50
        self.h = 90

        self.speed_y = 4
        self.gravity = 1
        self.jumping = True

        self.sprite_0 = pg.image.load('dino.png')
        self.sprite_1 = pg.image.load('dino2.png')

        self.frame = 0
        
    def jump(self):
        if(self.jumping == False):
            self.jumping = True
            self.speed_y = -15
  

    def update(self):
        if(self.jumping == True):
            self.y += self.speed_y
            self.speed_y += self.gravity
        else:        
            self.frame = (self.frame+1)%2  

    def render(self, window):
        #pg.draw.rect(window, (60,60,60), pg.Rect(self.x,self.y,self.w,self.h))
        window.blit(self.sprite, (self.x, self.y))
        if(self.frame == 0):
            window.blit(self.sprite_0, (self.x, self.y))
        if(self.frame == 1):
            window.blit(self.sprite_1, (self.x, self.y))

            