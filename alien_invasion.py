import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """游戏资源和行为管理类"""

    def __init__(self):
        """初始化游戏兵创建资源"""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption(self.settings.caption)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        self.clock = pygame.time.Clock()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 侦听键盘和鼠标事件
            self._check_events()
            self.ship.update()
            self.bullets.update()

            self._remove_unuse_bullet()

            # 每次循环时都重绘屏幕
            self._update_screen()
            self.clock.tick(60)

    def _remove_unuse_bullet(self):
        """删除失效子弹"""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                continue
            if event.type == pygame.KEYDOWN:
                self._chenck_keydown_event(event)
                continue
            if event.type == pygame.KEYUP:
                self._chenck_keyup_event(event)
                continue

    def _fire_bullet(self):
        """创建子弹并加入bullets编组"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """更新屏幕上的图像, 并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def _chenck_keydown_event(self, event):
        """keydown事件操作"""
        if event.key == pygame.K_RIGHT:
            # 开启向右移动标记
            self.ship.moving_right = True
            return
        if event.key == pygame.K_LEFT:
            # 开启向左移动标记
            self.ship.moving_left = True
            return
        if event.key == pygame.K_UP:
            # 开启向上移动标记
            self.ship.moving_up = True
            return
        if event.key == pygame.K_DOWN:
            # 开启向下移动标记
            self.ship.moving_down = True
            return
        if event.key == pygame.K_q:
            sys.exit()
            return
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
            return

    def _chenck_keyup_event(self, event):
        """keyup事件操作"""
        if event.key == pygame.K_RIGHT:
            # 关闭向右移动标记
            self.ship.moving_right = False
            return
        if event.key == pygame.K_LEFT:
            # 关闭向左移动标记
            self.ship.moving_left = False
            return
        if event.key == pygame.K_UP:
            # 关闭向右移动标记
            self.ship.moving_up = False
            return
        if event.key == pygame.K_DOWN:
            # 关闭向左移动标记
            self.ship.moving_down = False
            return


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
