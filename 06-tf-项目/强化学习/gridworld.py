#
#创建一个格子世界
#来自：https://blog.csdn.net/qq_36686996/article/details/79595915

import numpy as np
from gym.envs.toy_text import discrete
#设置方向
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
class GridWorldEnv(discrete.DiscreteEnv):
    def __init__(self , shape = [4,4]):
        self.shape = shape
        self.nS = np.prod(self.shape)
        self.nA = 4
        Max_y = shape[0]
        Max_x = shape[1]
        p = {}
        grid = np.arange(self.nS).reshape(shape)
        it = np.nditer(grid , flags = ['multi_index'])
        while not it.finished:
            s = it.iterindex
            y , x = it.multi_index
            p[s] = {a : [] for a in range(self.nA)}
            is_done = lambda s :s == 0 or s == (self.nS - 1)
            reward = 0.0 if is_done(s) else -1.0

            if is_done(s):
                p[s][UP] = [(1.0 , s , reward , True)]
                p[s][RIGHT] = [(1.0 , s , reward , True)]
                p[s][DOWN] = [(1.0 , s , reward , True)]
                p[s][LEFT] = [(1.0 , s , reward , True)]
            else:
                np_UP = s if y == 0 else s - Max_x
                np_RIGHT = s if x == (Max_x - 1) else s + 1
                np_DOWN = s if y == (Max_y - 1) else s + Max_x
                np_LEFT = s if x == 0 else s - 1
                p[s][UP] = [(1.0 , np_UP , reward , is_done(np_UP))]
                p[s][RIGHT] = [(1.0 , np_RIGHT , reward , is_done(np_RIGHT))]
                p[s][DOWN] = [(1.0 , np_DOWN , reward , is_done(np_DOWN))]
                p[s][LEFT] = [(1.0 , np_LEFT , reward , is_done(np_LEFT))]
                pass
            it.iternext()
        pass
        self.p = p
    pass