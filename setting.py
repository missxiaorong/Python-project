
class Setting():
    # 存储该项目所有设置的类

    def __init__(self):
        # 初始化游戏的设置
        # 屏幕设置
        self.screen_width = 1100
        self.screen_height = 620
        self.bg_color = (65,65,65)
        #飞船的设置
        self.ship_speed_factor = 1.5   # 移动1.5px
        self.ship_limit = 4

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3  # 些设置创建宽3像素、高15像素的深灰色子弹
        self.bullet_height = 15
        self.bullet_color = 178,34,34
        self.bullet_allowed = 3 # 将未消失的子弹数限制为3颗

        #外星人设置
        self.alien_speed_factor = 3 # 外星人移动速度设置
        self.fleet_drop_speed = 10   # 外星人群向下移动的速度
        # fleet_direction为1表示右移，-1表示为左移
        self.fleet_direction = 1



