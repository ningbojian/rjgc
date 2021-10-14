import os
import sys
import time
import pygame
import numpy as np

from paint import Paint
from Generate import Generate


class Game_Sudoku(object):
    # 初始化函数
    def __init__(self, screen_width, screen_height, selected_width, selected_height,
                 block_gap, block_size, level):
        """ 窗口 """
        self.screen_width = screen_width  # 窗口宽度
        self.screen_height = screen_height  # 窗口高度
        self.block_gap = block_gap  # 方块间隙 10
        self.block_size = block_size  # 方块大小 86
        self.form = ''  # 游戏主窗口

        self.martix = []  # 九宫格题目

        self.x, self.y = 0, 0  # 表格起始位置
        self.row, self.col = 0, 0  # 表格的相对位置

        """ 其他 """
        self.tmp = 0  # 时间差
        self.time = ""  # 计时0:00:00
        self.start_time = ""  # 开始时间
        self.nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # 数独游戏中的数字
        self.empty = []  # 数独中的空格位置
        self.is_same = []  # 当同行或同列或同方块出现相同数字, 则数独中与之相同的数字的位置
        self.issuccess = False  # 游戏是否成功
        self.start = False  # 游戏是否开始

        """ 字体 """
        self.title_font = ''  # 窗口标题字体类型及大小: Sudoku
        self.time_font = ''  # 时间字体类型及大小
        self.tips_font = ''  # 说明字体类型及大小
        self.font = ''  # 数字字体

        """ 选择窗口 """
        self.selected_form = ""  # 选择难易程度的窗口
        self.selected_width = selected_width  # 选择窗口的宽度
        self.selected_height = selected_height  # 选择窗口的高度

        self.selected_font = ""  # easy/medium/hard 字体类型及大小

        self.move_x, self.move_y = 0, 0  # 鼠标移动的位置
        self.press_x, self.press_y = 0, 0  # 鼠标按键的位置

        self.level = level  # 游戏难易程度
        self.counts = [30, 40, 50]  # 挖洞个数

    # 窗口的设置
    def Form(self):
        """
        :return:
        """
        pygame.init()  # 初始化所有导入的 pygame 模块
        pygame.display.set_caption("Game_Sudoku")  # 窗口标题
        os.environ['SDL_VIDEO_CENTERED'] = '1'  # 窗口居中显示
        self.form = pygame.display.set_mode([self.screen_width, self.screen_height], 0, 0)  # 窗口大小
        os.environ['SDL_VIDEO_CENTERED'] = '1'  # 窗口居中显示

        self.start_time = time.time()

        """ 游戏初始化 """
        self.init()

        while True:
            self.Action()  # 用户行为: 键盘输入/鼠标
            pygame.display.update()  # 使绘制的显示到窗口上

    # 选择窗口的设置
    def SelectedForm(self):
        """
        :return:
        """
        pygame.init()  # 初始化所有导入的 pygame 模块
        pygame.display.set_caption("Game_Sudoku")  # 窗口标题
        os.environ['SDL_VIDEO_CENTERED'] = '1'  # 窗口居中显示
        self.selected_form = pygame.display.set_mode([self.selected_width, self.selected_height], 0, 0)  # 窗口大小

        while True:
            self.SelectedAction()  # 用户行为: 键盘输入/鼠标
            pygame.display.update()  # 使绘制的显示到窗口上

    # 用户行为(主窗口): 键盘输入/鼠标
    def Action(self):
        for event in pygame.event.get():  # pygame.event.get(): 获取所有消息并将其从队列中删除
            if event.type == pygame.QUIT:  # pygame.QUIT: 窗口右上角的红 ×
                # sys.exit()  # sys.exit()函数是通过抛出异常的方式来终止进程的
                self.SelectedForm()
            elif event.type == pygame.MOUSEMOTION:  # 鼠标移动事件
                pos = pygame.mouse.get_pos()
                self.move_x, self.move_y = pos[0], pos[1]
            elif event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标按键事件
                pos = pygame.mouse.get_pos()
                self.press_x, self.press_y = pos[0], pos[1]
                self.row, self.col = (self.press_y - 140 - 1) // 61, (self.press_x - 5 - 1) // 61
            elif event.type == pygame.KEYDOWN:  # 键盘按键事件
                """
                pygame.KEYDOWN 按下键盘时
                pygame.KEYUP 释放键盘时
                """
                """ 
                K_ESCAPE: ESC
                """
                if event.key == pygame.K_SPACE:
                    self.start = True
                    self.start_time = time.time()
                elif event.key == pygame.K_ESCAPE:
                    """ 游戏初始化 """
                    self.init()
                elif chr(event.key) in self.nums and 0 <= self.row <= 8 and 0 <= self.col <= 8 \
                        and [self.row, self.col] in self.empty:
                    self.IsRight(chr(event.key))
                    self.martix[self.row][self.col] = chr(event.key)
                elif event.key == pygame.K_BACKSPACE:
                    if [self.row, self.col] in self.empty:
                        self.martix[self.row][self.col] = 0

        paint = Paint()
        paint.PaintForm(self.form, self.start_time, self.block_size, self.block_gap,
                        self.move_x, self.move_y, self.press_x, self.press_y, self.martix,
                        self.empty, self.is_same, self.issuccess, self.start)  # 表格绘制

        # 判断游戏是否成功
        self.IsSuccess()

    # 用户行为(选择难度窗口): 键盘输入/鼠标
    def SelectedAction(self):
        for event in pygame.event.get():  # pygame.event.get(): 获取所有消息并将其从队列中删除
            if event.type == pygame.QUIT:  # pygame.QUIT: 窗口右上角的红 ×
                sys.exit()  # sys.exit()函数是通过抛出异常的方式来终止进程的
            elif event.type == pygame.MOUSEMOTION:  # 鼠标移动事件
                pos = pygame.mouse.get_pos()
                self.move_x, self.move_y = pos[0], pos[1]
            elif event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标按键事件
                pos = pygame.mouse.get_pos()
                self.press_x, self.press_y = pos[0], pos[1]
                if 0 < self.press_x < 260 and 0 < self.press_y < 100:
                    self.level = 0
                elif 0 < self.press_x < 260 and 100 < self.press_y < 200:
                    self.level = 1
                elif 0 < self.press_x < 260 and 200 < self.press_y < 300:
                    self.level = 2
            elif event.type == pygame.MOUSEBUTTONUP:  # 鼠标释放事件
                self.Form()
        paint = Paint()
        paint.PaintSelected(self.selected_form, self.move_x, self.move_y)  # 表格绘制

    # 游戏初始化
    def init(self):
        self.empty = []
        # 数独题目、答案
        g = Generate(self.counts[self.level])
        self.martix = g.build_martix()

        # 获取数独中的空格位置
        for i in range(9):
            for j in range(9):
                if self.martix[i][j] == 0:
                    self.empty.append([i, j])

    # 判断填入数字是否符合游戏要求
    def IsRight(self, num):
        """
        :param num: 输入的数字
        :return: 该行、列、大表格是否存在和num相同的数字
        """
        """
        self.martix[self.row, :]: 行
        self.martix[:, self.col]: 列
        self.martix[self.row // 3 * 3: self.row // 3 * 3 + 3, self.col // 3 * 3: self.col // 3 * 3 + 3]: 所处表格
        """
        rowset = self.martix[self.row, :]  # 行
        colset = self.martix[:, self.col]  # 列
        blockset = self.martix[self.row // 3 * 3: self.row // 3 * 3 + 3,
                   self.col // 3 * 3: self.col // 3 * 3 + 3].reshape(9)  # 方格

        num = int(num)
        self.is_same = []
        if num in rowset or num in colset or num in blockset:
            pos = np.where(self.martix == num)
            pos_x, pos_y = pos[0], pos[1]
            for i in range(len(pos_x)):
                self.is_same.append([pos_x[i], pos_y[i]])

    # 判断游戏是否成功
    def IsSuccess(self):
        if self.martix.min() > 0 and not self.is_same:
            self.empty = []
            self.issuccess = True
            self.end = time.time()
        else:
            self.issuccess = False