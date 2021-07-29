from headers import *
import numpy as np

from colorama import Fore, Back, Style 
RESET=Style.RESET_ALL
GREY = Fore.LIGHTGREEN_EX
CYAN = Fore.LIGHTCYAN_EX+Back.CYAN  
RED = Fore.BLUE
BLUE = Fore.BLUE
GCOLOR = Fore.LIGHTGREEN_EX+Back.GREEN
WHITE=Fore.WHITE
ICE=Fore.CYAN
RCOLOR=Fore.LIGHTRED_EX+Back.RED
class background:

    def __init__(self):
        self.__skyblockwidth = 2
        self.__groundblockwidth = 2
        self.__groundblock = np.array([[RCOLOR + '-'+RESET, RCOLOR + '-'+RESET], [
                                      RCOLOR+'x'+RESET, RCOLOR+'x'+RESET], [RCOLOR+'x'+RESET, RCOLOR+'x'+RESET]])
        self.__skyblock = np.array([[Back.YELLOW+' '+RESET, Back.WHITE+' '+RESET], [
                                   Back.WHITE+' '+RESET, Back.MAGENTA+' '+RESET], [Back.MAGENTA+' '+RESET, Back.MAGENTA+' '+RESET]])

    def create_ground(self, grid):
        grid[breadth-X:breadth,
             0:length] = np.tile(self.__groundblock, (int)(length/2))

    def create_sky(self, grid):
        grid[0:X,
             0:length] = np.tile(self.__skyblock, (int)(length/2))
