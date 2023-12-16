import pygame
import random
import pygame as pg
   #                       Падаючі Зірки
pygame.init()

picture_level1 = pg.image.load('images/background.png')
picture_diamond1 = pg.image.load('images/8.png')
picture_diamond2 = pg.image.load('images/9.png')
picture_diamond3 = pg.image.load('images/11.png')
window = pygame.display.set_mode((600, 700))
run = True
wizard_direction = 'STOP'
count_before_diamand = 0

lost = 0
catch = 0

def draw_level1(window, picture):
    window.blit(picture, (0, 0))


class wizard:
    main_picture = pg.image.load('images/1_IDLE_000.png')
    lives_number = 5
    width = 138
    height = 150
    x = 10
    y = 500
    speed = 1

    def move_left(self):
        if self.x - self.speed >= 0:
            self.x -= self.speed
        else:
            self.x = 0

    def move_right(self):
        if self.x + self.speed <= 600 - self.width:
            self.x += self.speed
        else:
            self.x = 600 - self.width

    def stand(self, window):
        window.blit(self.main_picture, (self.x, self.y))

    def wizard_position(self):
        return (self.x, self.y)

    def wizard_size(self):
        return (self.width, self.height)


class super_wizard(wizard):
    width = 150
    height = 175
    main_picture = pygame.image.load("images/1_IDLE_000_i.png")
    left_picture = pygame.image.load("images/3_Run_000_il.png")
    right_picture = pygame.image.load("images/3_RUN_000_i.png")
    jump_picture = pygame.image.load("images/4_JUMP_003.png")

    def jump(self,window):
        window.blit(self.jump_pictuire, (self.x,self.y-70))
class diamond():
    x = 0
    y = 0
    speed = 0
    picture = 0

    def __init__(self, picture):
        self.x = random.randint(0, 560)
        self.speed = random.randint(1, 1)
        self.picture = picture

    def show(self, window):
        window.blit(self.picture, (self.x, self.y))

    def fall(self):
        self.y += self.speed

    def diamond_position(self):
        return (self.x, self.y)


class diamonds():
    diam_pict = [pg.image.load('images/8.png'), pg.image.load('images/9.png'), pg.image.load('images/11.png')]
    diam_list = []

    def __init__(self):
        pass

    def add(self):
        self.diam_list.append(diamond(self.diam_pict[random.randint(0, 2)]))

    def draw(self, window):
        for element in self.diam_list:
            element.show(window)

    def fall(self):
        for element in self.diam_list:
            element.fall()

    def delete(self, x, y, width,height):
        count = 0
        for element in self.diam_list:
            position = element.diamond_position()
            d_x = position [0]
            d_y = position [1]+47
            if d_x > x and d_x < x + width and d_y > y and d_y < y + height:
                del self.diam_list[count]
                count += 1
                print(count)

wizard1 = super_wizard()
wizard2 = wizard()
diamonds_in_game = diamonds()
diamonds_in_game.add()

while run:
    if count_before_diamand == 200:
        diamonds_in_game.add()
        count_before_diamand = 0
    draw_level1(window, picture_level1)
    diamonds_in_game.draw(window)
    wizard2.stand(window)
    wizard1.stand(window)

    # Перший

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            wizard_direction = 'LEFT'
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            wizard_direction = 'RIGHT'
    if wizard_direction == 'LEFT':
        wizard1.move_left()
    elif wizard_direction == 'RIGHT':
        wizard1.move_right()
    else:
        wizard1.stand(window)

    # Другий

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            wizard_direction = 'LEFT'
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            wizard_direction = 'RIGHT'
    if wizard_direction == 'LEFT':
        wizard2.move_left()
    elif wizard_direction == 'RIGHT':
        wizard2.move_right()
    else:
        wizard2.stand(window)



    pg.display.update()
    count_before_diamand += 1
    wizard_position = wizard1.wizard_position()
    wizard_size = wizard1.wizard_size()
    result = diamonds_in_game.delete(wizard_position[0], wizard_position[1], wizard_size[0], wizard_size[1])

    catch += 0
    lost += 1

    diamonds_in_game.fall()
pygame.quit()
