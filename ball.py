from headers import *
from colorama import Fore, Back, Style 
import numpy as np

class ball:

	def __init__(self):
		self.__pos_x=77
		self.__pos_y=40
		self.__vel_x=0
		self.__vel_y=0
		self.__lives=10
		self.__flag=0
		self.__score=0
		self.__bricks=0
		self.__body = np.zeros((1, 1), dtype='<U20')

		self.__empty = np.zeros((1, 1), dtype='<U20')
		self.__empty[:] = ' '
	def decrease_lives(self):
		self.__lives-=1

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
	def create(self,grid):

		self.__body[0]= ['o']
	def subtract(self,x):
		self.__bricks-=1
	def scorechange(self,a):
		self.__score+=a
	def get_score(self):
		return self.__score
	def kill(self,grid,ax,by):
		if self.__flag==1:
			self.__flag=0
			self.__lives=self.__lives-1
		self.erase_ball(grid)
		self.__vel_x=0
		self.__vel_y=0
		self.__pos_x=ax
		self.__pos_y=by
		self.create(grid)
	def update(self,grid,ax,by):
		if self.__pos_x > length-6:
			self.__vel_x = (-1)*self.__vel_x
		elif self.__pos_x < 8:
			self.__vel_x = (-1)*self.__vel_x
		if self.__pos_y < 5:
			self.__vel_y = (-1)*self.__vel_y
		if self.__pos_y==40 and self.__flag==0:
			self.kill(grid,ax,by)
		if self.__pos_y==40 and self.__flag==1 and ax-7<=self.__pos_x and ax+8>=self.__pos_x:
			self.__vel_y=-1*self.__vel_y
			if self.__pos_x > ax:
				self.__vel_x = self.__vel_x +self.__pos_x -ax
			if self.__pos_x <= ax:
				self.__vel_x = self.__vel_x -(ax-self.__pos_x)
			return 1
		if self.__pos_y >= 42:
			self.kill(grid,ax,by)
		return 0
	def start(self):
		self.__vel_x=1
		self.__vel_y=-2
		self.__flag=1
	def invertxvel(self):
		self.__vel_x=(-1)*self.__vel_x
	def invertyvel(self):
		self.__vel_y=(-1)*self.__vel_y


	def place_ball(self, grid):
        
		x = self.__pos_x
		y = self.__pos_y
		grid[y:y+1,x:x+1] = self.__body

	def erase_ball(self, grid):
		'''Erases mando off the board, reduces lives
		'''
		x = self.__pos_x
		y = self.__pos_y
		grid[y:y+1,x:x+1] = self.__empty
	def fireball(self,grid):
		self.__body[0]=[Fore.RED+'o']
		self.place_ball(grid)
	def set_values(self, x,y):
		'''sets appropriate values of mando and returns 1 if in path of obstacle 
		'''
		# if any parameter is passed as -100 that means it should remain unchanged

		self.__pos_x+=x
		self.__pos_y+=y

            
		if self.__pos_x > length-4:
			self.__pos_x = length-4
		elif self.__pos_x < 3:
			self.__pos_x = 3
		if self.__pos_y > breadth-4:
			self.__pos_y=breadth-4
		elif self.__pos_y < 5:
			self.__pos_y=4







