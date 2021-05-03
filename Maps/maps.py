import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge


class Map:

    def __init__(self, map_string):
        self.map_string = map_string

        self._goals = []
        self._me = None
        self._width = 0
        self._height = 0
        self._map_array = []

    def is_goal(self, x: int, y: int):
        return (x, y) in self._goals

    def is_valid_cell(self, x: int, y: int):
        return 0 <= x < self._width and 0 <= y < self._height and self._map_array[y][x] != '0'

    def get_successors(self, x: int, y: int):
        successors = []

        if x + 1 < self._width and 0 <= y < self._height and self.is_valid_cell(x + 1, y):
            successors.append((x + 1, y))

        if x + 1 < self._width and y + 1 < self._height and self.is_valid_cell(x + 1, y + 1):
            successors.append((x + 1, y + 1))

        if 0 <= x < self._width and y + 1 < self._height and self.is_valid_cell(x, y + 1):
            successors.append((x, y + 1))

        if x - 1 >= 0 and y + 1 < self._height and self.is_valid_cell(x - 1, y + 1):
            successors.append((x - 1, y + 1))

        if x - 1 >= 0 and 0 <= y < self._height and self.is_valid_cell(x - 1, y):
            successors.append((x - 1, y))

        if x - 1 >= 0 and y - 1 >= 0 and self.is_valid_cell(x - 1, y - 1):
            successors.append((x - 1, y - 1))

        if 0 <= x < self._width and y - 1 >= 0 and self.is_valid_cell(x, y - 1):
            successors.append((x, y - 1))

        if x + 1 < self._width and y - 1 >= 0 and self.is_valid_cell(x + 1, y - 1):
            successors.append((x + 1, y - 1))

        if not successors:
            raise Exception('Wrong coordinate!')

        return successors

    def get_matrix(self):
        mat = []
        for i, arr in enumerate(self._map_array):
            mat.append([])
            for j in arr:
                if j == '0':
                    mat[i].append(0)

                elif j == '1':
                    mat[i].append(20)
                else:
                    mat[i].append(ord(j) + 25)
        return mat

    def draw(self, **kwargs):
        mat = np.array(self.get_matrix())
        algorithm = None
        heuristics = None
        x, y = np.meshgrid(np.arange(mat.shape[1]), np.arange(mat.shape[0]))
        m = np.c_[x[mat.astype(bool)], y[mat.astype(bool)]]
        plt.matshow(mat)

        def rect(pos):
            r = plt.Rectangle(pos - 0.51, 1, 1, facecolor="none", edgecolor="g", linewidth=0.5)
            plt.gca().add_patch(r)

        def goal_item(pos):
            r = plt.Circle(pos, 0.4, facecolor="#20fa8d")
            plt.gca().add_patch(r)

        def foot_item(pos, index):
            r = plt.Circle(pos, 0.35, facecolor="#fa2082")
            plt.gca().add_patch(r)
            if pos != self._me:
                plt.text(r.get_center()[0] - 0.1, r.get_center()[1], str(index),
                         fontsize=55 / np.min([self._width, self._height]))

        def me_item(pos):
            r = Wedge(pos, .3, 0, 320, facecolor="#fa9420")
            plt.gca().add_patch(r)

        for pos in m:
            rect(pos)

        for pos in self._goals:
            goal_item(pos)

        try:
            algorithm = kwargs['algorithm']

            for index, pos in enumerate(algorithm(self)):
                foot_item(pos, index)
        except:
            pass

        try:
            algorithm = kwargs['algorithm']
            heuristics = kwargs['heuristics']

            for index, pos in enumerate(algorithm(self, heuristics)):
                foot_item(pos, index)
        except:
            pass

        me_item(self._me)

        plt.axis('off')
        plt.show()

    @property
    def goals(self):
        return self._goals

    @goals.setter
    def goals(self, goals):
        self._goals = goals

    @property
    def me(self):
        return self._me

    @me.setter
    def me(self, value):
        self._me = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def map_array(self):
        return self._map_array

    @map_array.setter
    def map_array(self, value):
        self._map_array = value

    def __str__(self):
        return self.map_string


class Parser:

    def __init__(self):
        self.maps_parent = './maps/'
        self.maps = [
            'mini.txt',
            'map1.txt',
            'map2.txt',
            'map3.txt',
            'map4.txt',
            'map5.txt',
            'wall.txt',
            'river.txt'
        ]
        self.count = len(self.maps)

    def parse(self, file) -> Map:
        map_string = ''
        map_array = []
        goals = []
        me = None
        width = 0
        height = 0
        for i, line in enumerate(file):
            if width == 0:
                width = len(line) - 1

            height += 1
            map_string += line
            map_array.append([])
            for j, c in enumerate(line):
                if c == '1':
                    goals.append((j, i))
                elif c == '*':
                    me = (j, i)
                if c != '\n':
                    map_array[i].append(c)

        _map = Map(map_string)
        _map.goals = goals
        _map.width = width
        _map.height = height
        _map.me = me
        _map.map_array = map_array
        return _map

    def get_map(self, number: int) -> Map:
        try:
            with open(self.maps_parent + self.maps[number], 'r') as file:
                return self.parse(file)
        except:
            raise Exception('wrong map number!')

    def get_all_maps(self) -> list:
        maps = []
        for i in range(len(self.maps)):
            maps.append(self.get_map(i))
        return maps
