import random
import numpy as np


class Generate(object):
    # 初始化九宫格
    def __init__(self, n):
        # int8，int16，int32，int64 可替换为等价的字符串 'i1'，'i2'，'i4'，以及其他
        self.martix = np.zeros((9, 9), dtype='i1')
        self.Nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        self.n = n  # 挖洞数目

        # 挖洞时保存挖好的数独
        self.uniqueMartix = []

    # 构建数独
    def build_martix(self):
        # self.LasVegas(11)  # 数独的生成
        while not self.LasVegas(11):
            pass
        self.Generate(self.n)
        return self.martix

    # 拉斯维加斯算法生成数独
    def LasVegas(self, counts):
        """
        :param counts: 生成的数字个数
        :return:
        """
        while counts:
            # [x, y] 为表格位置, 即表格位置是随机生成
            row = random.randint(0, 8)
            col = random.randint(0, 8)

            # 九宫格中的空格
            if self.martix[row, col] == 0:
                # 随机取数
                value = random.sample(self.Get_possible(row, col), 1)[0]
                self.martix[row, col] = value
                counts -= 1

        # 采用深度优先方法继续解数独
        if self.Solve():
            return True
        else:
            return False

    # 求解数独
    def Solve(self):
        for row in range(9):
            for col in range(9):
                if self.martix[row, col] == 0:
                    possible = self.Get_possible(row, col)  # 所有的可能的数字
                    for value in possible:
                        self.martix[row, col] = value
                        if self.Solve():
                            return True
                        self.martix[row, col] = 0
                        self.row, self.col = row, col
                    return False
        return True

    # 数字[1, 9]随机排列
    def Get_possible(self, row, col):
        """
        :param row: 横坐标
        :param col: 纵坐标
        :return: 返回可能的数字集合
        """
        # [x, y] 为大表格位置, 即九个小格子为一个大表格
        x, y = row // 3, col // 3
        """
        self.martix[row, :]: [row, col]表格所在行
        self.martix[:, col]: [row, col]表格所在列
        """
        rowSet = set(self.martix[row, :])  # [row, col] 所在行的数字集合
        colSet = set(self.martix[:, col])  # [row, col] 所在列的数字集合
        blockSet = set(self.martix[x * 3: x * 3 + 3, y * 3: y * 3 + 3].reshape(9))  # [row, col] 所在大表格的数字集合

        return self.Nums - rowSet - colSet - blockSet

    # 根据数独盘生成数独题目
    def Generate(self, n):
        # level 表示要挖掉的数字个数，通常挖掉 50 - 60 个左右，
        # 最多挖去63-64个可以得到有唯一解的宫格，但是需要计算的时间会长很多
        self.uniqueMartix = self.martix.copy()

        counts = 0
        while counts < n:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            # 该格子已经挖过了
            if self.uniqueMartix[row, col] == 0:
                continue

            # 挖掉该格子后能生成唯一的九宫格。如果有就继续挖，如果没有唯一解就不挖这个格子
            if self.IsUnique(row, col):
                # 保存挖洞后的状态
                self.uniqueMartix[row, col] = 0

                # 挖完洞后继续挖，直到挖出指定数量的格子
                self.martix = self.uniqueMartix.copy()

                counts += 1

    # 挖洞后判断是否该九宫格只有唯一的答案
    def IsUnique(self, row, col):
        for value in range(1, 10):
            if self.martix[row][col] != value:
                # 假设挖掉这个数字
                self.martix[row][col] = 0
                if value in self.Get_possible(row, col):
                    # 更换一个数字之后检查是否还有另一解
                    self.martix[row][col] = value
                    if self.Solve():
                        return False

                # 上面进行深度优先过程已经改变了 self.martix的值，恢复更换这个数字之前的状态
                self.martix = self.uniqueMartix.copy()

        # 已尝试所有其他数字发现无解,即只有唯一解
        return True