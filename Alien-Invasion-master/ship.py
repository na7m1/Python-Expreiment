import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """Initialize the ship, and set its starting position."""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载船舶图像，并获取其矩形。
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 在屏幕底部中心启动每艘新船。
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 存储船舶中心的十进制值。
        self.center = float(self.rect.centerx)

        # 运动标志。
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx

    def update(self):
        """Update the ship's position, based on movement flags."""
        # 更新船舶的中心值，而不是矩形。
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 从 self.center 更新矩形对象。
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
