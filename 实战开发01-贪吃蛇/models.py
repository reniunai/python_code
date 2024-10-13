import pygame
import random
from contants import *

# 移动方向字典
DIRECTION_DICT = {
    pygame.K_UP: (0, -BLOCK_SIZE),    # 上
    pygame.K_RIGHT: ( BLOCK_SIZE, 0),    # 右
    pygame.K_DOWN: (0,  BLOCK_SIZE),    # 下
    pygame.K_LEFT: (-BLOCK_SIZE, 0),    # 左
}

# 蛇头方向字典
HEAD_DICT = {
    pygame.K_DOWN:   0,
    pygame.K_RIGHT: 90,
    pygame.K_UP:   180,
    pygame.K_LEFT: 270,
}
class Snake:
    
    def __init__(self, x, y):
        self.direction = pygame.K_RIGHT  # 0上，1右，2下，3左
        self.is_cross_enable = True
        # 得分
        self.score = 0
        # 蛇身列表
        self.snake_body = [
            pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
        ]
        # 蛇头图片
        head_image = pygame.image.load("res/head-red.png")
        # 对图片大小的缩放
        self.snake_head_image = pygame.transform.scale(head_image, 
            (BLOCK_SIZE, BLOCK_SIZE))

        for _ in range(3):       
            self.grow()
            
        self.score = 0
    
    def draw(self, screen):
        # 绘制蛇身体
        for node in self.snake_body[1:]:
            pygame.draw.rect(screen, COLOR_WHITE, node, border_radius=3)

        # 绘制蛇头
        head: pygame.Rect = self.snake_body[0]
        # 对原始头图进行旋转：
        # Down  -> 0
        # Right -> 90
        # Up    -> 180
        # Left  -> 270
        head_image = pygame.transform.rotate(self.snake_head_image, HEAD_DICT[self.direction])
        screen.blit(head_image, (head.x, head.y))

    def is_direction_enable(self, input_key):
        
        if input_key not in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN):
            return False
        
        # 不能原地掉头 (不能左右)
        LR = (pygame.K_LEFT, pygame.K_RIGHT)
        if self.direction in LR and input_key in LR:
            return False
        # 不能原地掉头 (不能上下)
        UD = (pygame.K_UP, pygame.K_DOWN)
        if self.direction in UD and input_key in UD:
            return False
        
        return True

    def update_direction(self, input_key):
        """更新运动方向
        禁止水平或垂直方向直接变换
        
        :param new_dir: 新的方向
        """
        # 符合条件，更新方向
        self.direction = input_key

    def move(self):
        """ 
        移动之前要根据输入的方向，修改移动的方向 direction
        每一帧绘制之前都会调用move移动
        让蛇向前移动一格
        """
        # 把蛇头复制一份
        new_node = self.snake_body[0].copy()
        # 往前进的方向移动一格 (direction 0上，1右，2下，3左)
        new_move = DIRECTION_DICT[self.direction]
        new_node.x += new_move[0]
        new_node.y += new_move[1]
        
        if self.is_cross_enable:
            # 如果超出范围，瞬移
            if new_node.x >= SCREEN_WIDTH:
                new_node.x -= SCREEN_WIDTH
            elif new_node.x < 0:
                new_node.x += SCREEN_WIDTH
            
            if new_node.y >= SCREEN_HEIGHT:
                new_node.y -= SCREEN_HEIGHT
            elif new_node.y < 0:
                new_node.y += SCREEN_HEIGHT
            
        # 把新的蛇头放到最前边
        self.snake_body.insert(0, new_node)
        # 把蛇尾移除
        self.snake_body.pop() # 索引不穿参，默认移除最后一个
    
    def grow(self):
        # 蛇尾复制一份
        new_node = self.snake_body[-1].copy()
        
        # 添加新的节点到尾部
        self.snake_body.append(new_node)
        
        # 得1分
        self.score += 1
    
class Food:
    
    def __init__(self, node) -> None:
        # self.node = pygame.Rect(16 * BLOCK_SIZE, 8 * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        self.node = node
        
    def draw(self, screen):
        pygame.draw.rect(screen, COLOR_BLUE, self.node, border_radius=3)

    # 注解
    @staticmethod
    def gen_food_position(snake: Snake) -> pygame.Rect:
        """根据屏幕宽高、蛇身信息生成新的食物的x、y坐标

        :param snake: 蛇对象
        :return: 坐标的x、y元组 (32, 24)
        """
        while True:
            # W: 640 // 20 = 32
            x = random.randint(0, SCREEN_WIDTH // BLOCK_SIZE - 1) # 0, 1, 2 ... 31
            # H: 480 // 20 = 24
            y = random.randint(0, SCREEN_HEIGHT // BLOCK_SIZE - 1) # 0, 1, 2 ... 23
            # 如果在蛇身上，重新生成
            new_food_node = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            if new_food_node not in snake.snake_body:
                # 新的食物不在蛇身&蛇头
                return new_food_node
            