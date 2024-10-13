import pygame
import time
from pygame.locals import KEYDOWN

"""
文件名不可以与已有模块名相同
"""

# 初始化pygame
pygame.init()

# 创建窗体 Surface
screen: pygame.surface.Surface = pygame.display.set_mode(size=(640, 480))

# 窗口标题
pygame.display.set_caption("飞机大战v1.0")

# 窗口图标
icon_image = pygame.image.load("res/icon.png")
pygame.display.set_icon(icon_image)

COLOR = (200, 200, 0) # R(0-255) G(0-255) B(0-255)
# 准备图片
plane_image = pygame.image.load("res/hero2.png")
# 旋转
plane_image = pygame.transform.rotate(plane_image, 90)

# 时钟
clock = pygame.time.Clock()

counter = 0
# 运行无限循环 fps - Frame Per Second 帧率（每秒绘制多少帧） 0.1
while True:
    start = time.time()
    # 处理事件，获取用户的输入事件------------------------------------
    event_list = pygame.event.get()
    # 解析处理所有事件 
    # event.type 保存用户输入的事件类型：鼠标、按键
    # event.key  保存按下或抬起的按键
    for event in event_list:
        if event.type == pygame.QUIT:
            print("点击了关闭")
            # 退出游戏
            pygame.display.quit()
            exit(0)
        elif event.type == pygame.KEYDOWN:
            print("按键被按下：", event.key)
            # 上、下、左、右、空格
            if event.key == pygame.K_UP:
                print("向上")
            elif event.key == pygame.K_DOWN:
                print("向下")
            elif event.key == pygame.K_LEFT:
                print("向左")
            elif event.key == pygame.K_RIGHT:
                print("向右")
                
    # 绘制界面------------------------------------------------------
    screen.fill(COLOR)
    
    # 绘制图片
    screen.blit(plane_image, (320, 30))
    
    # 刷新界面, 内存对象中的内容才能真正刷新到界面
    pygame.display.flip()
    
    # 通过主动休眠减少刷新速度
    # time.sleep(0.1) # 休眠0.1秒
    # end = time.time()
    # duration = end - start # 当前帧的耗时. 60Hz, 144Hz, 240Hz
    # if duration != 0:
    #     print("duration: {} fps: {}".format(duration, 1 / duration))
    
    clock.tick(30) # 10帧/s - 每次运行，内部会确保跑足1/10s的时间
    
    print("fps: ", clock.get_fps())