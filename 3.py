import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((600,315))
pygame.display.set_caption("Моя перша гра")

icon = pygame.image.load('foto/pika.png')
pygame.display.set_icon(icon)

screen.fill((70,44,133))

back = pygame.image.load('foto/backk.jpg')

walk_left= [
pygame.image.load('player/left/play1_l.png'),
pygame.image.load('player/left/play2_l.png'),
pygame.image.load('player/left/play3_l.png'),
pygame.image.load('player/left/play4_l.png'),
    ]

walk_right = [
pygame.image.load('player/right/play1_r.png'),
pygame.image.load('player/right/play2_r.png'),
pygame.image.load('player/right/play3_r.png'),
pygame.image.load('player/right/play4_r.png'),
    ]

player_anim = 0
bg_a = 0


running = True
while running:

    
    screen.blit(back,(bg_a,0))
    screen.blit(back,(bg_a + 600,0))
    
    screen.blit(walk_right[player_anim],(300,250))

    if player_anim == 3:
       player_anim = 0
    else:
       player_anim +=1
       
    bg_a -= 0.1
    if bg_a == -600:
        bg_a = 0 

    pygame.display.update()
    
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            
       clock.tick(15)      
