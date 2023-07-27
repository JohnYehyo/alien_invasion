class Settings:
    """设置类"""

    def __init__(self):
        """初始化属性"""
        # 窗口标题
        self.caption = "外星人入侵"
        # 屏幕宽度
        self.screen_width = 1440
        # 屏幕高度
        self.screen_height = 900
        # 背景颜色
        self.bg_color = (230, 230, 230)

        # 飞船贴图
        self.ship_image = "images/ship.bmp"
        # 飞船速度
        self.ship_speed = 1.5

        # 子弹颜色
        self.bullet_color = (0, 0, 0)
        # 子弹宽度
        self.bullet_width = 5
        # 子弹高度
        self.bullet_height = 5
        # 子弹速度
        self.bullet_speed = 3
        # 子弹限制
        self.bullet_allowed = 3




