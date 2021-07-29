from headers import *
from colorama import Fore, Back, Style 
import numpy as np

class bulleti:

	def __init__(self,a,b):
		self.__pos_x=a
		self.__pos_y=b
		self.__vel_x=0
		self.__vel_y=-2
		self.__flag=0
		self.__score=0
		self.__bricks=0
		self.__kill=0
		self.__body = np.zeros((1, 1), dtype='<U20')

		self.__empty = np.zeros((1, 1), dtype='<U20')
		self.__empty[:] = ' '

	def create_bullet(self):
		self.__body[0]=[Fore.RED+'^']
	def place_bullet(self,grid):
		grid[self.__pos_y:self.__pos_y+1,self.__pos_x:self.__pos_x+1]=self.__body
	def clean(self,grid):
		grid[self.__pos_y:self.__pos_y+1,self.__pos_x:self.__pos_x+1]=self.__empty
	def change_y(self):
		self.__pos_y+=self.__vel_y
	def status(self):
		return self.__kill
	def kill(self):
		self.__kill=1


	def get_bricks(self):
		return self.__bricks

	def get_vel_x(self):
		return self.__vel_x
	def get_lives(self):
		return self.__lives
	def get_vel_y(self):
		return self.__vel_y
	def get_pos_x(self):
		return self.__pos_x
	def get_pos_y(self):
		return self.__pos_y
	def subtract(self,x):
		self.__bricks-=1
	def scorechange(self,a):
		self.__score+=a
	def get_score(self):
		return self.__score