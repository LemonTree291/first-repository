import pygame

pygame.init()

display = pygame.display.set_mode((600, 600))
pygame.display.set_caption("My game")
icon = pygame.image.load("python.png")
pygame.display.set_icon(icon)
pygame.draw.rect(display, "white", pygame.Rect(0, 0, 600, 600))
color = "red"

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            #break
        pass


    pygame.draw.line(display, color, (0, 300), (300, 300), 15)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if color == "red":
            color = "green"
        else:
            color = "red"







    pygame.display.update()