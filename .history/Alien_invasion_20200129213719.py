import pygame
from settings import Settings
from ship import Ship
import game_functions as gf 

def run_game():
    #初始化游戏并创建一个游戏对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship = Ship(screen)

    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        gf.check_events()

        #每次循环时都重绘屏幕并让
        gf.update_screen(ai_settings,screen,ship)

        #让最近绘制的屏幕可见
        pygame.display.flip()

run_game