import pygame
from pygame.locals import *

# 游戏初始化
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# 加载图像
player_image = pygame.image.load("player.png").convert_alpha()
platform_image = pygame.image.load("platform.png").convert_alpha()

# 定义常量
GRAVITY = 0.8
PLAYER_SPEED = 5
JUMP_HEIGHT = 15

# 玩家类
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.is_jumping = False

    def update(self):
        self.gravity()
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        self.check_collision()

    def gravity(self):
        if self.vel_y == 0:
            self.vel_y = 1
        else:
            self.vel_y += GRAVITY

    def jump(self):
        if not self.is_jumping:
            self.vel_y = -JUMP_HEIGHT
            self.is_jumping = True

    def check_collision(self):
        if self.rect.y >= height - self.rect.height:
            self.rect.y = height - self.rect.height
            self.vel_y = 0
            self.is_jumping = False

# 平台类
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = platform_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# 创建玩家和平台
player = Player(50, height - 100)
platforms = pygame.sprite.Group()
platforms.add(Platform(0, height - 40))
platforms.add(Platform(width - 200, height - 80))
platforms.add(Platform(200, height - 160))
platforms.add(Platform(width - 400, height - 200))
platforms.add(Platform(100, height - 320))

# 游戏循环
running = True
while running:
    # 1. 清屏
    screen.fill((0, 0, 0))

    # 2. 更新玩家和平台
    player.update()

    # 3. 绘制玩家和平台
    screen.blit(player.image, player.rect)
    platforms.draw(screen)

    # 4. 刷新屏幕
    pygame.display.flip()
    clock.tick(60)

    # 5. 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                player.jump()

    # 6. 处理键盘输入
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        player.vel_x = -PLAYER_SPEED
    elif keys[K_RIGHT]:
        player.vel_x = PLAYER_SPEED
    else:
        player.vel_x = 0

    # 7. 检测玩家和平台碰撞
    if pygame.sprite.spritecollide(player, platforms, False):
        player.rect.y -= player.vel_y
        player.vel_y = 0
        player.is_jumping = False

pygame.quit()