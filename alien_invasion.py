
import sys    # 玩家退出时，使用模块sys退出游戏
import  pygame
from  setting import Setting
from  ship import Ship
from alien import  Alien
import game_functions as gf
from  pygame.sprite import  Group
from game_stats import  GameStats


def run_game():
    # 初始化Pygame、设置和屏幕对象
    pygame.init()   # 初始化背景设置
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) # 创建显示窗口，并指定了游戏窗口的尺寸px，注意使用了两个括号
    pygame.display.set_caption("Alien Invasion")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人编组
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #创建一个外星人
    # alien = Alien(ai_settings, screen)
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标
        gf.check_events(ai_settings,screen,ship,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens,bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
