from headers import *
from colorama import Fore, Back, Style 
import numpy as np

class paddle:

	def __init__(self):
		self.__pos_x=74
		self.__pos_y=40
		self.__vel_x=0
		self.__vel_y=0
		self.__body = np.zeros((3, 15), dtype='<U20')

		self.__empty = np.zeros((4, 15), dtype='<U20')
		self.__empty[:] = ' '
		self.__x=np.array(['-'])
		self.__body2=np.zeros((4,15),dtype='<U20')

	def create(self,grid):

		self.__body[0]= np.tile(self.__x,15)
		self.__body[1]=np.tile(self.__x,15)
		self.__body[2]= np.tile(self.__x,15)

	def place_paddle(self, grid):
        
		x = self.__pos_x
		y = self.__pos_y
		grid[y-1:y+2, x-7:x+8] = self.__body
	def place_paddle2(self,grid):
		x = self.__pos_x
		y = self.__pos_y
		self.__body2[0]=[Fore.RED+'|',Fore.RED+'|',Fore.RED+'|',' ',' ',' ',' ',' ',' ',' ',' ',' ',Fore.RED+'|',Fore.RED+'|',Fore.RED+'|']
		self.__body2[1]= np.tile(self.__x,15)
		self.__body2[2]=np.tile(self.__x,15)
		self.__body2[3]= np.tile(self.__x,15)
		grid[y-1:y+3, x-7:x+8] = self.__body2


	def get_pos_x(self):
		return self.__pos_x
	def get_pos_y(self):
		return self.__pos_y

	def erase_paddle(self, grid):
		'''Erases mando off the board, reduces lives
		'''
		x = self.__pos_x
		y = self.__pos_y
		grid[y-1:y+3, x-7:x+8] = self.__empty

	def set_values(self, x):
		'''sets appropriate values of mando and returns 1 if in path of obstacle 
		'''
		# if any parameter is passed as -100 that means it should remain unchanged

		if x != -100:
			self.__pos_x += x

            
			if self.__pos_x > length-8:
				self.__pos_x = length-8
			elif self.__pos_x <= 7:
				self.__pos_x = 7






