from headers import *
from colorama import Fore, Back, Style 
import numpy as np

class ufo:

	def __init__(self):
		

		self.__pos_x=10
		self.__pos_y=3
		self.__vel_x=0
		self.__vel_y=0
		self.__health=10
		self.__flag=0
		self.__score=0
		self.__bricks=0
		arr=np.zeros((14,64),dtype='<U20')
		arr[:]=' '
		z=0
		with open("ufo.txt") as ufo:
			for a in ufo:
				x = 0
				for b in a:
					if b == '\n':
						break
					else:
						arr[z][x] = b+Fore.RESET
					x += 1
				z += 1
		self.__body = arr

		self.__empty = np.zeros((14,64), dtype='<U20')
		self.__empty[:] = ' '

	def health(self):
		return self.__health
	def get_pos_x(self):
		return self.__pos_x
	def get_pos_y(self):
		return self.__pos_y

	def update(self,grid,a):
		self.clean(grid)
		self.__pos_x=a-30
		if(self.__pos_x<=3):
			self.__pos_x=3
		if(self.__pos_x>=80):
			self.__pos_x=80
	def ball_collision(self,a,b,ball):
		if a>=self.__pos_x+3 and a<=self.__pos_x+6 and b<self.__pos_y+14 and ball.get_vel_x()>0:
			ball.invertxvel()
			self.__health=self.__health-1
		elif a>=self.__pos_x+56 and a<=self.__pos_x+60 and b<self.__pos_y+14 and ball.get_vel_x()<0:
			ball.invertxvel()
			self.__health=self.__health-1
		elif a>=self.__pos_x-2 and a<=self.__pos_x+60 and b>self.__pos_y+13 and b<=self.__pos_y+15 and ball.get_vel_y()<0:
			ball.invertyvel()
			self.__health=self.__health-1

	def clean(self,grid):
		grid[self.__pos_y:self.__pos_y+14,self.__pos_x:self.__pos_x+64]=self.__empty	

	def printfunc(self,grid):
		grid[self.__pos_y:self.__pos_y+14,self.__pos_x:self.__pos_x+64]=self.__body


class bomb:

	def __init__(self,ufo):
		self.__pos_x=ufo.get_pos_x()+25
		self.__pos_y=ufo.get_pos_y()+10
		self.__vel_x=0
		self.__vel_y=0
		self.__kill=0
		arr=np.zeros((5,14),dtype='<U20')
		arr[:]=' '
		z=0
		with open("bomb.txt") as bomb:
			for a in bomb:
				x = 0
				for b in a:
					if b == '\n':
						break
					else:
						arr[z][x] = b+Fore.RESET
					x += 1
				z += 1

		
		self.__body = arr


		self.__empty = np.zeros((5,14), dtype='<U20')
		self.__empty[:] = ' '

	def update(self,grid,a):
		self.clean(grid)
		self.__pos_x=a-30
		if(self.__pos_x<=3):
			self.__pos_x=3
		if(self.__pos_x>=80):
			self.__pos_x=80

	def change_y(self,a,grid):
		self.__pos_y+=a
		if(self.__pos_y>=40):
			self.clean(grid)
			self.__kill=1

	def get_kill_stat(self):
		return self.__kill
	def paddle_collision(self,a,b,ball):
		if self.__pos_x<=a+7 and self.__pos_x>=a-7 and self.__pos_y>=38:
			ball.decrease_lives()
			self.__kill=1
	def clean(self,grid):
		grid[self.__pos_y:self.__pos_y+5,self.__pos_x:self.__pos_x+14]=self.__empty	

	def printfunc(self,grid):
		grid[self.__pos_y:self.__pos_y+5,self.__pos_x:self.__pos_x+14]=self.__body







