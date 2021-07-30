# Pygame template

import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')

WIDTH = 400
HEIGHT = 480
FPS = 1

def timerCall(secs):
    second = secs[0]
    result = "00:00:00"
    if second > 0:

        hour = second // 3600
        minute = (second % 3600) // 60
        sec = (second % 60)

        secDis = ('0' + str(sec))
        secDis = secDis[-2] + secDis[-1]

        minDis = ('0' + str(minute))
        minDis = minDis[-2] + minDis[-1]

        hourDis = ('0' + str(hour))
        hourDis = hourDis[-2] + hourDis[-1]

        result = hourDis + ':' + minDis + ':' + secDis

        secs[0] -= 1

    return result

# define several useful colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init() # sound or music
screen  = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fred's Stopwatch")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y, color):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

background = pygame.image.load(path.join(img_dir, "bg.png")).convert()
background_rect = background.get_rect()

pygame.mixer.music.load(path.join(snd_dir, 'No_Hope.mp3'))
pygame.mixer.music.set_volume(0.5)

realQuit = True
while realQuit:
    second = [eval(input("Please enter seconds: "))]
    # Game Loop
    running = True
    while running:
        # Keep the loop running at the right speed
        clock.tick(FPS)
        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

        # Update
        disTIME = timerCall(second)

        if second[0] < -12:
            running = False
        elif second[0] < 0:
            second[0] -= 1
            disTIME = "Close in " + str(second[0] + 13) + "s"
        elif second[0] == 0:
            second[0] -= 1
            pygame.mixer.music.play(loops=-1)

        # Draw / render
        screen.fill(BLACK) # Use RGB
        screen.blit(background, background_rect)
        if second[0] < 15 and second[0] >= -1:
            draw_text(screen, disTIME, 64, WIDTH / 2, HEIGHT / 4, RED)
        else:
            draw_text(screen, disTIME, 64, WIDTH / 2, HEIGHT / 4, WHITE)

        # Double buffering *after* every drawing!
        pygame.display.flip()

    pygame.mixer.music.pause()
    quiteQ = input("Is this the end?[y/n]")
    if quiteQ == 'y':
        realQuit = False

pygame.quit()
