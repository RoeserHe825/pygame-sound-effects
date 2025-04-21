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
TEXT_FONT = 'DejaVuSans.ttf'

# file with the logo
FAVICON_FILE = 'favicon-starter-cropped.png'

# file with sound effects
BEEP_SOUND_EFFECT = 'beep.ogg'
LASER_SOUND_EFFECT = 'laser5.ogg'
ZAP_SOUND_EFFECT = 'zap13.ogg'
DOOM_SOUND_EFFECT = 'doom-death-sound-effect.ogg'

# background music
BACKGROUND_SOUND = 'atomic-cat.ogg'

# game window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# window title (caption)
TITLE = 'Test Pygame Sound Menu'

# frame rate (frames per second)
FPS = 60

# draw text function
def draw_text(screen, text, font, text_color, y):
    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface, (WINDOW_WIDTH // 2 - text_surface.get_width() // 2, y))

def main():
    pygame.init()
    
    # initialize and load sound effects
    pygame.mixer.init()
    beep_sound = pygame.mixer.Sound(BEEP_SOUND_EFFECT)
    laser_sound = pygame.mixer.Sound(LASER_SOUND_EFFECT)
    zap_sound = pygame.mixer.Sound(ZAP_SOUND_EFFECT)
    doom_sound = pygame.mixer.Sound(DOOM_SOUND_EFFECT)
    pygame.mixer.music.load(BACKGROUND_SOUND) 
    
    # set up the screen
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(TITLE)
    
    # load favicon
    favicon = pygame.image.load(FAVICON_FILE)
    pygame.display.set_icon(favicon)
    
    
    clock = pygame.time.Clock()
    
    # set up font
    text_font = pygame.font.SysFont(TEXT_FONT, 30) 
  
    
    text_color = WHITE
    
    # instructions for the menu
    instructions = [
        "Press 'a' to play BEEP Sound Effect", 
        "Press 's' to play LASER Sound Effect", 
        "Press 'd' to play ZAP Sound Effect",
        "Press 'w' to play Background Music", 
        "Press 'q' to pause Background Music", 
        "Press 'e' to play DOOM Sound Effect",
        "Press 'r' to randomize the Text Color"
    ]
    
    base_y = 30  # starting y-value for the first command on the menu
    line_height = 40  # number of pixels between each command on the menu
    
    running = True
    while running:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # handle key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            beep_sound.play()
        if keys[pygame.K_s]:
            laser_sound.play() 
        if keys[pygame.K_d]:
            zap_sound.play()  
        if keys[pygame.K_e]:
            doom_sound.play() 
        if keys[pygame.K_r]:
            # Randomize text color
            text_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if keys[pygame.K_w]:
            pygame.mixer.music.play(-1) # never stops because of -1 
        if keys[pygame.K_q]:
            pygame.mixer.music.pause() # pauses the background music
        
        screen.fill(BLACK)
        
        # draw instructions
        for i in range(len(instructions)):
            instruction = instructions[i]
            draw_text(screen, instruction, text_font, text_color, base_y + i * line_height)
        
        # update display
        pygame.display.flip()
        
        # control frame rate
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
