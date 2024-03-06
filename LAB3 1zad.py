import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Dziewięciokąt")

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)

# Funkcja rysująca dziewięciokąt
def draw_nonagon():
    win.fill((0, 0, 0))
    radius = 150
    center_x = center_y = 300
    angle = 360 / 9
    points = []
    for i in range(9):
        x = center_x + radius * math.cos(math.radians(angle * i))
        y = center_y + radius * math.sin(math.radians(angle * i))
        points.append((x, y))
    pygame.draw.polygon(win, JASNY_NIEBIESKI, points, 5)
    pygame.display.flip()

# Funkcja rysująca dziewięciokąt obrócony o zadany kąt
def draw_rotated_nonagon(angle):
    win.fill((0, 0, 0))
    radius = 150
    center_x = center_y = 300
    points = []
    for i in range(9):
        rotated_x = center_x + radius * math.cos(math.radians(angle)) * math.cos(math.radians(360 / 9 * i)) - radius * math.sin(math.radians(angle)) * math.sin(math.radians(360 / 9 * i))
        rotated_y = center_y + radius * math.sin(math.radians(angle)) * math.cos(math.radians(360 / 9 * i)) + radius * math.cos(math.radians(angle)) * math.sin(math.radians(360 / 9 * i))
        points.append((rotated_x, rotated_y))
    pygame.draw.polygon(win, ZIELONY, points, 5)
    pygame.display.flip()

# Funkcja rysująca przekrzywiony dziewięciokąt
def draw_skewed_nonagon():
    win.fill((0, 0, 0))
    radius = 150
    center_x = center_y = 300
    przekrzywienie = 0.5
    points = []
    for i in range(9):
        x = center_x + radius * math.cos(math.radians(360 / 9 * i)) * przekrzywienie
        y = center_y + radius * math.sin(math.radians(360 / 9 * i)) * 0.9 * przekrzywienie
        points.append((x, y))
    pygame.draw.polygon(win, POMARANCZOWY, points, 5)
    pygame.display.flip()

# Funkcja rysująca "ściśnięty" dziewięciokąt u góry
def draw_compressed_nonagon():
    win.fill((0, 0, 0))
    radius = 150
    center_x = 300
    center_y = 130
    zwezenie = 0.8
    points = []
    for i in range(9):
        x = center_x + radius * math.cos(math.radians(360 / 9 * i))
        y = center_y + radius * math.sin(math.radians(360 / 9 * i)) * zwezenie
        points.append((x, y))
    pygame.draw.polygon(win, NIEBIESKI, points, 5)
    pygame.display.flip()

# Funkcja rysująca "kopnięty" dziewięciokąt
def draw_kicked_nonagon():
    win.fill((0, 0, 0))
    radius = 150
    center_x = center_y = 300
    angle = 360 / 9
    kopniecie = 1.2  
    points = []
    for i in range(9):
        x = center_x + radius * math.cos(math.radians(angle * i)) * kopniecie
        y = center_y + radius * math.sin(math.radians(angle * i))
        points.append((x, y))
    pygame.draw.polygon(win, FIOLETOWY, points, 5)
    pygame.display.flip()

# Funkcja rysująca dziewięciokąt "do góry nogami" i zwężony
def draw_upside_down_nonagon():
    win.fill((0, 0, 0))
    radius = 150
    center_x = center_y = 300
    angle = 360 / 9
    zwezenie = 0.5
    points = []
    for i in range(9):
        x = center_x + radius * math.cos(math.radians(angle * i)) * zwezenie
        y = center_y + radius * math.sin(math.radians(angle * i))
        points.append((x, y))
    pygame.draw.polygon(win, POMARANCZOWY, points, 5)
    pygame.display.flip()

# Funkcja rysująca rozszerzony i pod kątem dziewięciokąt
def draw_extended_skewed_nonagon():
    win.fill((0, 0, 0))
    radius = 150
    center_x = 380
    center_y = 450
    wydluzenie = 1.5
    points = []
    for i in range(9):
        x = center_x + radius * math.cos(math.radians(360 / 9 * i)) * wydluzenie
        y = center_y + radius * math.sin(math.radians(360 / 9 * i))
        points.append((x, y))
    pygame.draw.polygon(win, SZARY, points, 5)
    pygame.display.flip()

# Funkcja rysująca do góry nogami, kopnięty i poszerzony dziewięciokąt
def draw_upside_down_kicked_extended_nonagon():
    win.fill((0, 0, 0))
    radius = 150
    center_x = 350
    center_y = 400
    wydluzenie = 1.5
    zwezenie = 0.5
    points = []
    for i in range(9):
        x = center_x + radius * math.cos(math.radians(360 / 9 * i)) * wydluzenie
        y = center_y - radius * math.sin(math.radians(360 / 9 * i)) * zwezenie
        points.append((x, y))
    pygame.draw.polygon(win, POMARANCZOWY, points, 5)
    pygame.display.flip()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                draw_nonagon()
            elif event.key == pygame.K_2:
                draw_rotated_nonagon(45)
            elif event.key == pygame.K_3:
                draw_rotated_nonagon(179)
            elif event.key == pygame.K_4:
                draw_skewed_nonagon()
            elif event.key == pygame.K_5:
                draw_compressed_nonagon()
            elif event.key == pygame.K_6:
                draw_kicked_nonagon()
            elif event.key == pygame.K_7:
                draw_upside_down_nonagon()
            elif event.key == pygame.K_8:
                draw_extended_skewed_nonagon()
            elif event.key == pygame.K_9:
                draw_upside_down_kicked_extended_nonagon()

pygame.quit()
