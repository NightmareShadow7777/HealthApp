# Разработай свою игру в этом файле!
from pygame import*
class GameSprite(sprite.Sprite):
    def __init__(self, picture, w, h, x, y):
        super().__init__()
        self.image=transform.scale(image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= 5
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x += 5
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= 5
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += 5

class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.side = 'right'
        if self.rect.x >= 615:
            self.side = 'left'
        if self.side == 'left':
            self.rect.x -= 5
        else:
            self.rect.x += 5

class Enemy1(GameSprite):
    def update(self):
        if self.rect.y <= 300:
            self.side = 'right'
        if self.rect.y >= 420:
            self.side = 'left'
        if self.side == 'left':
            self.rect.y -= 5
        else:
            self.rect.y += 5

win_width = 700
win_height = 500
wall_1m = GameSprite('wall.png', 80, 180, 200, 250)

hero = Player('hero.png', 60, 60, 0, 0)
enemy = Enemy('enemy.png', 80, 80, 620, 280)
enemy1 = Enemy1('enemy1.png', 80, 80, 520, 280)
treasure = GameSprite('treasure.png', 80, 80, 615, 400)

w1 = GameSprite('wall.png', 450, 60, 100, 20)
w2 = GameSprite('wall.png', 350, 60, 100, 480)
w3 = GameSprite('wall.png', 10, 380, 100, 20)

window = display.set_mode((700, 500))
display.set_caption('Моя первая игра')
background = transform.scale(image.load('background.png'), (700, 500))
run = True
finish = False 
clock = time.Clock()
FPS = 60
font.init()
font = font.SysFont('Arial', 40)
win = font.render('YOU WIN', True, (255, 255, 15))
lose = font.render('YOU LOSE', True, (180, 0, 0))

while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        window.blit(background, (0, 0))
        hero.reset()
        hero.update()
        enemy.reset()
        enemy.update()
        treasure.reset()
        enemy1.reset()
        enemy1.update()
        w1.reset()
        w2.reset()
        w3.reset()
        if sprite.collide_rect(hero, enemy) or sprite.collide_rect(hero, w1) or sprite.collide_rect(hero, w2) or sprite.collide_rect(hero, w3) or sprite.collide_rect(hero, enemy1):
            finish = True
            window.blit(lose, (250, 250))
        if sprite.collide_rect(hero, treasure):
            finish = True
            window.blit(win, (250, 250))
    display.update()
