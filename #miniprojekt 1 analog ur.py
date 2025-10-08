#miniprojekt 1 analog ur
import pygame
import math
import datetime

pygame.init()
width, height = 600, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Analogt ur")

font = pygame.font.Font(None, 36)

center = (width // 2, height // 2)
radius = 250

#definere uret og henter tid
def draw_clock(surface, center, radius):
    now = datetime.datetime.now()
    hour = now.hour % 12
    minute = now.minute
    second = now.second

#tegner uret
    surface.fill((255, 255, 255))
    pygame.draw.circle(surface, (0, 0, 0), center, radius, 3) 
    for i in range(12):
        angle = 2 * math.pi * i / 12 - math.pi / 2
        x1 = int(center[0] + math.cos(angle) * (radius - 16))
        y1 = int(center[1] + math.sin(angle) * (radius - 16))
        x2 = int(center[0] + math.cos(angle) * (radius - 2))
        y2 = int(center[1] + math.sin(angle) * (radius - 2))
        pygame.draw.line(surface, (0, 0, 0), (x1, y1), (x2, y2), 3)
        
        # Tegn tal ved hver time-markering
        hour_number = 12 if i == 0 else i  
        text = font.render(str(hour_number), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_x = int(center[0] + math.cos(angle) * (radius - 30))
        text_y = int(center[1] + math.sin(angle) * (radius - 30))
        text_rect.center = (text_x, text_y)
        surface.blit(text, text_rect)

    # Tegn minutmarkeringer
    for i in range(60):
        if i % 5 != 0:  
            angle = 2 * math.pi * i / 60 - math.pi / 2
            x1 = int(center[0] + math.cos(angle) * (radius - 8))
            y1 = int(center[1] + math.sin(angle) * (radius - 8))
            x2 = int(center[0] + math.cos(angle) * (radius - 2))
            y2 = int(center[1] + math.sin(angle) * (radius - 2))
            pygame.draw.line(surface, (0, 0, 0), (x1, y1), (x2, y2), 2)

    # Timeviser
    hour_angle = 2 * math.pi * (hour + minute / 60) / 12 - math.pi / 2
    hour_x = int(center[0] + math.cos(hour_angle) * (radius * 0.6))
    hour_y = int(center[1] + math.sin(hour_angle) * (radius * 0.6))
    pygame.draw.line(surface, (0, 0, 0), center, (hour_x, hour_y), 7)

    # Minutviser
    min_angle = 2 * math.pi * minute / 60 - math.pi / 2
    min_x = int(center[0] + math.cos(min_angle) * (radius * 0.8))
    min_y = int(center[1] + math.sin(min_angle) * (radius * 0.8))
    pygame.draw.line(surface, (0, 0, 0), center, (min_x, min_y), 5)

    # Sekundviser
    sec_angle = 2 * math.pi * second / 60 - math.pi / 2
    sec_x = int(center[0] + math.cos(sec_angle) * (radius * 0.9))
    sec_y = int(center[1] + math.sin(sec_angle) * (radius * 0.9))
    pygame.draw.line(surface, (255, 0, 0), center, (sec_x, sec_y), 2)
    
run = True
clock = pygame.time.Clock()
while run:
    draw_clock(win, center, radius)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
clock = pygame.time.Clock()
while run:
    draw_clock(win, center, radius)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(1)  
pygame.quit()
