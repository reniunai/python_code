import pygame
from contants import *
from models import Snake, Food
"""
贪吃蛇游戏

1. 准备pygame开发环境: 窗口尺寸，标题
    a. 准备背景图
    b. 准备蛇头图片

2. while True:
    a. 处理用户输入事件
    b. 处理游戏逻辑
    c. 渲染界面
    d. 控制渲染速度fps
    
游戏逻辑：
1. 根据用户输入方向修改前进方向   ok
2. 遇到食物，吃掉食物，蛇身长一节 ok
3. 碰到墙体 or 碰到自己 结束游戏  
4. 全部吃完，结束游戏

额外功能：
1. 从屏幕另一端出现
2. 分数越高，速度越快
"""
class Game:
    
    def __init__(self) -> None:
        
        # 不能少init函数
        pygame.init()
        
        # 设置窗口大小，获取Surface
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # 设置标题
        pygame.display.set_caption("贪吃蛇大战v1.0")

        # 设置图标
        icon = pygame.image.load("res/icon.png")
        pygame.display.set_icon(icon)

        # 加载背景图（缩放）
        bg_image = pygame.image.load("res/bg.png")
        self.bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))


    def start(self):
        # clock
        clock = pygame.time.Clock()
        snake = Snake(5, 3)
        food  = Food(Food.gen_food_position(snake))
        is_game_over = False

        while True:
            # a.处理事件，获取用户的输入事件------------------------------------
            event_list = pygame.event.get()
            new_dir = None
            # 解析处理所有事件 
            # event.type 保存用户输入的事件类型：鼠标、按键
            # event.key  保存按下或抬起的按键
            for event in event_list: # 一帧时间内同时出现 上and左
                if event.type == pygame.QUIT:
                    print("点击了关闭")
                    # 退出游戏
                    self.quit_game()
                elif event.type == pygame.KEYDOWN:
                    print("按键被按下：", event.key)
                    # 上、下、左、右、空格 。移动之前要根据输入的方向，修改移动的方向 direction
                    if is_game_over:
                        if event.key == pygame.K_q:
                            # 退出游戏
                            self.quit_game() 
                        elif event.key == pygame.K_SPACE:
                            # 空格 重启游戏
                            snake = Snake(5, 3)
                            food  = Food(Food.gen_food_position(snake))
                            is_game_over = False
                            # self.start()
                            # return
                    elif event.key == pygame.K_ESCAPE:
                        self.quit_game()
                    elif snake.is_direction_enable(event.key):
                        new_dir = event.key
            
            if new_dir is not None:
                snake.update_direction(new_dir)
            
            # b. 处理游戏逻辑 ----------------------------------------------
            if not is_game_over: # 游戏没有结束
                snake.move()
                
                snake_head = snake.snake_body[0]
                
                # 碰到墙壁 (超出屏幕)
                if snake_head.x < 0 or snake_head.x >= SCREEN_WIDTH \
                    or snake_head.y < 0 or snake_head.y >= SCREEN_HEIGHT:
                    is_game_over = True
            
                # 碰到自己
                if snake_head in snake.snake_body[1:]:
                    is_game_over = True
                    
                # 遇到食物，吃掉食物，蛇身长一节
                if snake_head == food.node:
                    # 吃掉食物，刷新食物
                    food = Food(Food.gen_food_position(snake))
                    # 蛇身长一节
                    snake.grow()
                    

            
            # c. 渲染界面     ----------------------------------------------
            # 背景图
            self.screen.blit(self.bg_image, (0, 0))
            # 网格线
            # pygame.draw.line(screen, COLOR_GRAY, (0, 0), (300, 100))
            # 绘制所有的横线， h = 480 // 20 = 24 [0, 20, 40....480)
            for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
                pygame.draw.line(self.screen, COLOR_GRAY, (0, y), (SCREEN_WIDTH, y))
            # 绘制所有的竖线， w = 640 // 20 = 32 [0, 20, 40....640)
            for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
                pygame.draw.line(self.screen, COLOR_GRAY, (x, 0), (x, SCREEN_HEIGHT))
            
            # 绘制蛇身 rect = (x, y, w, h)
            snake.draw(self.screen)
            
            # 绘制食物
            food.draw(self.screen)
            
            # 绘制得分和fps
            self.show_text("Score: {}".format(snake.score), 20, 10, 10)
            
            fps = clock.get_fps() # 获取真的每秒帧率fps
            self.show_text("FPS: {:.2f}".format(fps), 20, SCREEN_WIDTH - 100, 10)
            
            # 根据游戏是否结束，渲染文字
            if is_game_over:
                self.show_text("游戏结束", 50, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4)
                self.show_text(f"得分：{snake.score}", 24, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4 + 60)
                self.show_text("按【空格键】重新开始", 24, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4 + 90)
                self.show_text("按【Q】退出游戏", 24, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4 + 120)
            
            # pygame.display.flip() # 执行最终的渲染
            # pygame.display.update(x, y, w, h) # 只渲染指定矩形区域内容，效率更高
            pygame.display.update()
            # d. 控制渲染速度fps ---------------------------------------------
            clock.tick(10 + snake.score)

    def quit_game(self):
        pygame.display.quit()
        exit(0)
            
    def show_text(self, text, font_size, x, y):
        """绘制文字

        :param text: 文字内容
        :param font_size: 字号
        :param x: 坐标x
        :param y: 坐标y
        """
        font1 = pygame.font.SysFont("SimHei", font_size)
        text = font1.render(text, True, COLOR_RED)
        self.screen.blit(text, (x, y))
        
        
if __name__ == '__main__':
    snake_game = Game()
    snake_game.start()
