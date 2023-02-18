import sys
import pygame


SCR_WIDTH = 576
SCR_HIGHT = 1024


def draw_floor():
    screen.blit(floor_surf, (floor_x_pos, 900))
    screen.blit(floor_surf, (floor_x_pos + SCR_WIDTH, 900))


pygame.init()
screen = pygame.display.set_mode((SCR_WIDTH, SCR_HIGHT))
clock = pygame.time.Clock()

bg_surf = pygame.image.load('assets/background-day.png').convert()
bg_surf = pygame.transform.scale2x(bg_surf)

floor_surf = pygame.image.load('assets/base.png').convert()
floor_surf = pygame.transform.scale2x(floor_surf)
floor_x_pos = 0

while True:  # game loop
    for event in pygame.event.get():  # event loop
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surf, (0, 0))

    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -(SCR_WIDTH):
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)
