import pygame

pygame.init()

display = pygame.display.set_mode((600, 600))
pygame.display.set_caption("My game")
icon = pygame.image.load("python.png")
pygame.display.set_icon(icon)



pygame.display.update()

pygame.draw.rect(display, "white", pygame.Rect(0, 0, 600, 600))


pygame.draw.line(display, "red", (0, 0), (600, 600), 15)





while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            break

    pygame.display.update()


