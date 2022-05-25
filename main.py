import pygame, sys
import invader

pygame.init()

WIDTH, HEIGHT = 1000, 700

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

invaders_list = []

def init(invaders_list):
    for type in range(5):
        for index in range(10):
            invaders_list.append(invader.Invader(0, type, 0, 0))

init(invaders_list)

print(invaders_list)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
