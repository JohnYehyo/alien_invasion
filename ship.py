import pygame
from settings import Settings


class Ship:
    """飞船管理类"""

    def __init__(self, ai_game):
        """初始化飞船及其初始位置"""
        self.screen = ai_game.screen
        # self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.settings = Settings()
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load(self.settings.ship_image)
        self.rect = self.image.get_rect()

        # 每艘新飞船都放置在屏幕中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 属性存储浮点数
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # 更新飞船的矩形对象
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
