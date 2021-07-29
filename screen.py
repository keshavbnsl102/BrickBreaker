from headers import *
import numpy as np


class Screen:
    

    def __init__(self, rows, columns):
        '''Initializes size of grid
        '''
        self.__rows = rows
        self.__columns = columns
        self.__grid = np.zeros((breadth, length), dtype='<U20')
        self.__grid[:] = ' '
                
    
    def screen_display(self):
        for i in range(self.__rows):
                for j in range(0, length):
                    print("\033[1m" + self.__grid[i][j], end='')
                print()
    
    def give_grid(self):
        return self.__grid