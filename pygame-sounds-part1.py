# pygame-sounds-part1
# Henry Roeser
# 4/16/25

import pygame
import random
import sys

# color constants (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

# text font
TEXT_FONT = 'Comic Sans'

# file with the logo
FAVICON_FILE = 'favicon-starter-cropped.png'

# file with sound effects
BEEP_SOUND_EFFECT = 'beep.ogg'
LASER_SOUND_EFFECT = 'laser5.ogg'
ZAP_SOUND_EFFECT = 'zap13.ogg'

# game window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# window title (caption)
# update the window title as needed
TITLE = 'Test Pygame Sound Menu'

# frame rate (frames per second)
FPS = 60

# initialize and load sound effects
pygame.mixer.init()
beep_sound = pygame.mixer.Sound(BEEP_SOUND_EFFECT)
laser_sound = pygame.mixer.Sound(LASER_SOUND_EFFECT)
zap_sound = pygame.mixer.Sound(ZAP_SOUND_EFFECT)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(TITLE)

    clock = pygame.time.Clock()
    running = True 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
    
        pygame.display.flip() # update display
        clock.tick(FPS) # control fps
    
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()