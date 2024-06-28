import pygame
from mathrect import MathRect


class Game:
    def __init__(self):
        pygame.init()
        self.sdim = [800, 600]
        self.screen = pygame.display.set_mode(self.sdim)
        self.run = True
        self.fps = 15
        self.timer = pygame.time.Clock()
        self.range = 300
        self.m = []
        
        for i in range(self.range):
            self.m.append(MathRect(i, i, 2, 2, self.sdim))
        
        
    def main(self):
        while self.run:
            self.screen.fill("Gray3")
            self.timer.tick(self.fps)
            
            for i in self.m:
                i.draw(self.screen, 'Purple')
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    
            pygame.display.update()
            
        pygame.quit()
            

Game().main()       
