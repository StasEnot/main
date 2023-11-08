from typing import Tuple

import pygame

image_path = '/data/data/org.test.YouWorld/files/app/'

clock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((600,315))
pygame.display.set_caption("Моя перша гра")

icon = pygame.image.load('../../foto/pika.png')
pygame.display.set_icon(icon)

screen.fill((70,44,133))

back = pygame.image.load('../../foto/backk.png').convert()

walk_left= [
pygame.image.load('../../player/left/play1_l.png').convert_alpha(),
pygame.image.load('../../player/left/play2_l.png').convert_alpha(),
pygame.image.load('../../player/left/play3_l.png').convert_alpha(),
pygame.image.load('../../player/left/play4_l.png'),
    ]

walk_right = [
pygame.image.load('../../player/right/play1_r.png').convert_alpha(),
pygame.image.load('../../player/right/play2_r.png').convert_alpha(),
pygame.image.load('../../player/right/play3_r.png').convert_alpha(),
pygame.image.load('../../player/right/play4_r.png').convert_alpha(),
    ]



zombi = pygame.image.load('../../foto/zombi.png').convert_alpha()
zombi_game = []

player_anim = 0
bg_a = 0

player_speed = 15
player_x = 150
player_y = 250

is_jump = False
jump = 8

bg_sound = pygame.mixer.Sound('../../music/Hornet.mp3')
bg_sound.play()

zombi_time = pygame.USEREVENT = 1
pygame.time.set_timer(zombi_time, 2500)

font = pygame.font.Font('../../fonts/roboto.ttf', 40)
font_text = pygame.font.Font('../../fonts/roboto.ttf', 15)
text = font.render('Ви програли', True, 'Red')

again = font.render('Зіграти знову', True, 'Red')
again_rect = again.get_rect(topleft=(180,200))


gameplay = True

ball = font_text.render('Ваші очки:' , True, 'White')
rewards_text = font_text.render('%s % (rewards)', True, 'White' )
rewards = 0

bullet = pygame.image.load('../../foto/bullet.png')
bullets: int = []
bullets_a: int = 5
bullets_text = font_text.render('bullets_a', True, 'White' )
bullets_text_text = font_text.render("Патрони:", True, 'White')

arrows = pygame.image.load('../foto/arrow1.png')
arrows_rect =  walk_left[0].get_rect(topleft=(540,260))
arrows_1 = pygame.image.load("../foto/arrow2.png")
arrows_rect_1 = walk_left[0].get_rect(topleft=(450, 260))
arrows_2 = pygame.image.load("../foto/arrow3.png")
arrows_rect_3 = walk_left[0].get_rect(topleft=(10, 260))
gun = pygame.image.load("../foto/gun.png")
gun_rect = walk_left[0].get_rect(topleft=(90, 260))

running = True
while running:

    screen.blit(back, (bg_a,0))
    screen.blit(back, (bg_a + 600,0))
    screen.blit(ball, (0,0))
    screen.blit(rewards_text, (80,0))
    screen.blit(bullets_text_text, (00,20))
    screen.blit(bullets_text, (64,20))
    screen.blit(arrows, (540,260))
    screen.blit(arrows_1, (450, 260))
    screen.blit(arrows_2, (10, 260))
    screen.blit(gun, (90, 260))

    if gameplay == True:
        player_rect = walk_left[0].get_rect(topleft=(player_x,player_y))
 
        if zombi_game:
           for (i,el) in enumerate(zombi_game) :
               screen.blit(zombi, el)
               el.x -= 10

               if el.x < -10:
                   zombi_game.pop(i)
                   rewards += 1

               if player_rect.colliderect(el):
                    print('Ви Програли %s' % (rewards))
                    gameplay = False
                 
    
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        if keys[pygame.K_LEFT] or arrows_rect_1.collidepoint(mouse) and pygame.mouse.get_pressed()[0] and player_x > 70:
            screen.blit(walk_left[player_anim],(player_x,player_y))
        else:
            screen.blit(walk_right[player_anim],(player_x,player_y))

        mouse = pygame.mouse.get_pos()
        if keys[pygame.K_LEFT] and player_x > 70 or arrows_rect_1.collidepoint(mouse) and pygame.mouse.get_pressed()[0] and player_x > 70:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x > 0 or arrows_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] and player_x > 0:
            player_x += player_speed
  
        if not is_jump:
            if keys[pygame.K_UP] or arrows_rect_3.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                is_jump = True
        else:
            if jump >= -8:
                if jump > 0:
                    player_y -= (jump ** 2) / 2
                else:
                    player_y += (jump ** 2) / 2
                jump -= 1
            else:
                is_jump = False
                jump = 8
     
        if player_anim == 3:
            player_anim = 0
        else: 
            player_anim +=1   
 
        bg_a -= 2
        if bg_a == -600:
            bg_a = 0


        
        if bullets:
            for (i,el) in enumerate(bullets):
                screen.blit(bullet,(el.x,el.y))
                el.x += 4

                if el.x > 605:
                    bullets.pop(i)

                if zombi_game:
                    for(index, zombi_el) in enumerate(zombi_game):
                        if el.colliderect(zombi_el):
                            zombi_game.pop(index)
                            bullets.pop(i)

                
  
    else:
        screen.fill((208,120,100))
        screen.blit(text,(185,100))
        screen.blit(again, again_rect)

        mouse = pygame.mouse.get_pos()
        if again_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 150
            zombi_game.clear()
            bullets_a = 5
            bullets.clear()


            


    pygame.display.update()
    
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            pygame.quit()
            running = False
       if event.type == zombi_time:
            zombi_game.append(zombi.get_rect(topleft=(590,250)))

       if gameplay and event.type == pygame.KEYUP and event.key  == pygame.K_SPACE and bullets_a > 0 or gun_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            bullets.append(bullet.get_rect(topleft=(player_x + 30, player_y + 10)))
            bullets_a -= 1    
     

    clock.tick(15)

    
    

  

