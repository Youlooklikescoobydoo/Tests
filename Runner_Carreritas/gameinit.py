import pygame

pygame.init()

screen = pygame.display.set_mode ((500, 300))
pygame.display.set_caption("SandboxRunGame")

clock = pygame.time.Clock()

running = True

terrain = pygame.image.load("PyGraphics/Terrain.png")
terrainPos = terrain.get_rect(midbottom = (200, 180))
yipSpt = pygame.image.load("PyGraphics/lowresyippe.png")
yipColl = yipSpt.get_rect(topleft = (200, 100))


yipSpt_x =
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(terrain, terrainColl)
    screen.blit(yipSpt, yipColl)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
exit()
