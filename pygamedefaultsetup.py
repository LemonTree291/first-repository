import pygame

pygame.init()

display = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My game")
icon = pygame.image.load("python.png")
pygame.display.set_icon(icon)



pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            break
    pygame.display.update()


