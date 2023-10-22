import pygame

pygame.init()
screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Моя перша гра")

icon = pygame.image.load('foto/pika.png')
pygame.display.set_icon(icon)

screen.fill((70,44,133))

cvad = pygame.Surface((150,50))
cvad.fill('red')

running = True
while running:

    screen.blit(cvad,(425,225))

    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                screen.fill((114,157,224))
                cvad.fill('Blue')
                
   
