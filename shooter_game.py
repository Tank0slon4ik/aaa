from pygame import *
from random import randint

mixer.init()

mixer.music.load('space.ogg')
mixer.music.play()

window = display.set_mode((700, 500))
display.set_caption("Не шутер")

background = transform.scale(image.load('galaxy.jpg'),(700, 500))

FPS = 60
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, xsize, ysize, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (xsize, ysize))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, player_image, x, y, xsize, ysize, speed):
        super().__init__(player_image, x, y, xsize, ysize, speed)
    def update(self):
        global key_click
        key_click = key.get_pressed()
        if key_click[K_d] and self.rect.x < 650:
            self.rect.x += self.speed
        if key_click[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
    def fire(self):
        bullet = bullets("bullet.png", 325, 450, 4, 20, 10)
        Bullets.add(bullet)

class enemy(GameSprite):
    def __init__(self, player_image, x, y, xsize, ysize, speed):
        super().__init__(player_image, x, y, xsize, ysize, speed)
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = randint(-60, -32)
            self.rect.x = randint(0, 650)
            self.speed = randint(1,3)

class bullets(GameSprite):
    def __init__(self, player_image, x, y, xsize, ysize, speed):
        super().__init__(player_image, x, y, xsize, ysize, speed)
    def update(self):
        self.rect.y -= self.speed


enemies = sprite.Group()
Bullets = sprite.Group()

player = Player('rocket.png', 325, 450, 50, 50, 4)
enemy1 = enemy('ufo.png', randint(0, 650), 0, 50, 32, randint(1, 3))
enemies.add(enemy1)
enemy2 = enemy('ufo.png', randint(0, 650), 0, 50, 32, randint(1, 3))
enemies.add(enemy2)
enemy3 = enemy('ufo.png', randint(0, 650), 0, 50, 32, randint(1, 3))
enemies.add(enemy3)
enemy4 = enemy('ufo.png', randint(0, 650), 0, 50, 32, randint(1, 3))
enemies.add(enemy4)
enemy5 = enemy('ufo.png', randint(0, 650), 0, 50, 32, randint(1, 3))
enemies.add(enemy5)
enemy6 = enemy('ufo.png', randint(0, 650), 0, 50, 32, randint(1, 3))
enemies.add(enemy6)

game = True
while game:
    window.blit(background, (0, 0))
    player.update()
    player.reset()
    enemy1.update()
    enemy1.reset()
    enemy2.update()
    enemy2.reset()
    enemy3.update()
    enemy3.reset()
    enemy4.update()
    enemy4.reset()
    enemy5.update()
    enemy5.reset()
    enemy6.update()
    enemy6.reset()
    enemies.update()
    if key_click[K_SPACE]:
        player.fire()
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()