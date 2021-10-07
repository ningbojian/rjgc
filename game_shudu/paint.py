import time
import pygame
import datetime


class Paint(object):
    # 初始化
    def __init__(self):
        self.martix = []  # 九宫格的数字
        self.timing = ""

    # 绘制选择窗口
    def PaintSelected(self, selected_form, move_x, move_y):
        """ 游戏背景 """
        # fill(color): 填充某一种颜色
        selected_form.fill((220, 220, 220))

        """ 字体设置 """
        # 初始化字体
        pygame.font.init()

        # part_1: easy
        # pygame.draw.rect(self.selected_form, (128, 128, 128), (0, 0, 260, 100))
        selected_font = pygame.font.SysFont('simsunnsimsun', 30, True)
        easy_text = selected_font.render('简 单', True, (0, 0, 0))
        selected_form.blit(easy_text, (90, 30))

        # part_2: medium
        # pygame.draw.rect(self.selected_form, (128, 128, 128), (0, 100, 260, 100))
        medium_text = selected_font.render('中 等', True, (0, 0, 0))
        selected_form.blit(medium_text, (90, 130))

        # part_3: hard
        # pygame.draw.rect(self.selected_form, (128, 128, 128), (0, 200, 260, 100))
        hard_text = selected_font.render('困 难', True, (0, 0, 0))
        selected_form.blit(hard_text, (90, 230))

        """ 鼠标移动事件 """
        if 0 < move_x < 260 and 0 < move_y < 100:
            pygame.draw.rect(selected_form, (128, 128, 128), (0, 0, 260, 100))
            easy_text = selected_font.render('简 单', True, (255, 255, 255))
            selected_form.blit(easy_text, (90, 30))
        elif 0 < move_x < 260 and 100 < move_y < 200:
            pygame.draw.rect(selected_form, (128, 128, 128), (0, 100, 260, 100))
            medium_text = selected_font.render('中 等', True, (255, 255, 255))
            selected_form.blit(medium_text, (90, 130))
        elif 0 < move_x < 260 and 200 < move_y < 300:
            pygame.draw.rect(selected_form, (128, 128, 128), (0, 200, 260, 100))
            hard_text = selected_font.render('困 难', True, (255, 255, 255))
            selected_form.blit(hard_text, (90, 230))

    # 绘制主窗口
    def PaintForm(self, form, start_time, block_size, block_gap,
                  move_x, move_y, press_x, press_y, martix, empty, is_same, issuccess, start):
        """ 游戏背景 """
        # fill(color): 填充某一种颜色
        form.fill((220, 220, 220))

        """ 主窗口————上 """
        # 初始化字体
        pygame.font.init()
        # 添加标题
        # f = pygame.font.get_fonts()  #: 获取字体样式
        # pygame.font.Font.render(): 在一个新 Surface 对象上绘制文本
        title_font = pygame.font.SysFont('幼圆', 50, True)
        title_text = title_font.render('数 独', True, (0, 0, 0))
        form.blit(title_text, (120, 10))

        # 添加时间: 计时: 0:00:00
        pygame.draw.rect(form, (128, 128, 128), (380, 0, 130, 70))
        time_font = pygame.font.SysFont('幼圆', 28, True)
        time_text = time_font.render('计 时', True, (0, 0, 0))
        form.blit(time_text, (405, 5))

        tmp = round(time.time() - int(start_time), 0)
        self.time = str(datetime.timedelta(seconds=tmp))
        digtial_time = time_font.render(str(self.time), True, (255, 250, 250))
        form.blit(digtial_time, (390, 35))

        # time.sleep(1)

        # 添加游戏说明
        tips_font = pygame.font.SysFont('simsunnsimsun', 20)
        tips_text = tips_font.render('利用逻辑和推理，在其他的空格上填入1-9的数字。', True, (0, 0, 0))
        form.blit(tips_text, (25, 70))

        tips_text = tips_font.render('使1-9每个数字在每一行、每一列和每一宫中都只出现一次。', True, (0, 0, 0))
        form.blit(tips_text, (25, 90))

        tips_text = tips_font.render('按esc键重新开始', True, (0, 0, 0))
        form.blit(tips_text, (25, 110))

        """ 主窗口————中 """
        pygame.draw.rect(form, (0, 0, 0), (5, 140, 550, 550))  # 黑色背景
        pygame.draw.rect(form, (65, 105, 225), (5, 140, 185, 185))  # 蓝色背景, 左上1格
        pygame.draw.rect(form, (65, 105, 225), (370, 140, 185, 185))  # 蓝色背景, 右上3格
        pygame.draw.rect(form, (65, 105, 225), (188, 322, 185, 185))  # 蓝色背景, 中间5格
        pygame.draw.rect(form, (65, 105, 225), (5, 505, 185, 185))  # 蓝色背景, 左下7格
        pygame.draw.rect(form, (65, 105, 225), (370, 505, 185, 185))  # 蓝色背景, 右下9格

        for i in range(9):
            for j in range(9):
                # (x, y) 方块的初始位置
                x = j * block_size + (j + 1) * block_gap
                y = i * block_size + (i + 1) * block_gap

                """ 鼠标移动事件 """
                # 鼠标移动到相应方块, 方块颜色变化
                if x + 5 < move_x < x + 5 + block_size and y + 140 < move_y < y + 140 + block_size:
                    pygame.draw.rect(form, (220, 220, 220), (x + 5, y + 140, block_size, block_size))
                else:
                    pygame.draw.rect(form, (255, 255, 255), (x + 5, y + 140, block_size, block_size))

                """ 鼠标按键事件 """
                # 鼠标按键相应的方块, 该方块所在的行和列颜色均发生变化
                # 列
                if x + 5 < press_x < x + 5 + block_size and 140 < press_y < 690:
                    pygame.draw.rect(form, (220, 220, 220), (x + 5, y + 140, block_size, block_size))
                # 行
                if y + 140 < press_y < y + 140 + block_size and 5 < press_x < 555:
                    pygame.draw.rect(form, (220, 220, 220), (x + 5, y + 140, block_size, block_size))

                # 绘制数字
                num_font = pygame.font.SysFont('幼圆', 45, True)  # 数字字体类型及大小
                if martix[i][j] != 0:
                    if [i, j] not in empty and [i, j] not in is_same:
                        num_text = num_font.render(str(martix[i][j]), True, (0, 0, 0))
                    elif [i, j] not in empty and [i, j] in is_same:
                        num_text = num_font.render(str(martix[i][j]), True, (255, 0, 0))
                    else:
                        num_text = num_font.render(str(martix[i][j]), True, (65, 105, 225))
                    # if martix[i][j] == 0:
                    #     num_text = num_font.render(str(martix[i][j]), True, (255, 255, 255))
                    # else:
                    #     num_text = num_font.render(str(martix[i][j]), True, (0, 0, 0))
                    form.blit(num_text, (x + 22, y + 150))

        """ 如果游戏成功 """
        if issuccess:
            success_font = pygame.font.SysFont("simsunnsimsun", 60, True)
            str_text = success_font.render('Successful!', True, (178, 34, 34))
            form.blit(str_text, (85, 360))

        """ 游戏未开始 """
        if not start:
            pygame.draw.rect(form, (192, 192, 192), (100, 250, 360, 300))
            font = pygame.font.SysFont("幼圆", 40, True)
            str_text = font.render('空格开始', True, (0, 0, 0))
            form.blit(str_text, (190, 360))