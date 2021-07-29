import os
import random
import signal
import time
import tty
from headers import *
import numpy as np
from colorama import Fore, Back, Style 

class powerups():

	def __init__(self,uptime):
		self._activated=0
		self._uptime=uptime
		self._upstart=0
		self._render=0
		self._body = np.zeros((5, 5), dtype='<U20')
		self._empty = np.zeros((5, 5), dtype='<U20')
		self._empty[:] = ' '



	def initiate(self):
		if self._activated==0:
			self._activated=1
			self._upstart=time.time()







class expand(powerups):

	def __init__(self,uptime,a,b,c,d):
		super().__init__(uptime)
		self._body[0]=[Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+'|']
		self._body[1]=[Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+'|']
		self._body[2]=[Back.RED+' ',Back.RED+'F',Back.RED+'I',Back.RED+'R',Back.RED+'E']
		self._body[3]=[Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+'|']
		self._body[4]=[Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+'|']
		self._pos_x=a
		self._pos_y=b
		self.__vel_x=c
		self.__vel_y=d
		self._id=1


	def update(self):
		if self._activated==1:
			if time.time()-self._upstart>self._uptime:
				self._activated=0
	def changex(self,a):
		self._pos_x+=a
	def changey(self,b):
		self._pos_y+=b
	def change_vel_x(self,c):
		self.__vel_x+=c
	def change_vel_y(self,d,grid):
		self.__vel_y+=d
		if self._pos_y>=40:
			self.clean(grid)
			self._render=0
		if self._pos_x > length-14:
			self._pos_x = length-14
		elif self._pos_x < 3:
			self._pos_x = 3
		if self._pos_y < 5:
			self._pos_y=4
		if self._pos_x > length-14:
			self.__vel_x = (-1)*self.__vel_x
		elif self._pos_x < 6:
			self.__vel_x = (-1)*self.__vel_x
		if self._pos_y < 5:
			self.__vel_y = (-1)*self.__vel_y
	def get_vel_x(self):
		return self.__vel_x
	def get_vel_y(self):
		return self.__vel_y
	def get_pos_y(self):
		return self._pos_y
	def setx(self,a):
		self._pos_x=a
	def sety(self,b):
		self._pos_y=b
	def printi(self,grid,paddle):
		print(self._pos_y)
		print(self._pos_x)
		grid[self._pos_y:self._pos_y+5,self._pos_x:self._pos_x+5]=self._body
		if self._pos_y>=40:
			self.clean(grid)
			self._render=0
		if self._pos_y>=38 and self._pos_x>=paddle.get_pos_x()-12 and self._pos_x<=paddle.get_pos_x()+9:
			self.initiate()
	def clean(self,grid):
		grid[self._pos_y:self._pos_y+5,self._pos_x:self._pos_x+5]=self._empty



class shrink(powerups):

	def update(self):
		if self._activated==1:
			if time.time()-self._upstart>self._uptime:
				self._activated=0

class thruball(powerups):

	def update(self):
		if self._activated==1:
			if time.time()-self._upstart>self._uptime:
				self._activated=0



class fastball(powerups):

	def update(self):
		if self._activated==1:
			if time.time()-self._upstart>self._uptime:
				self._activated=0

class shooting(powerups):
	def __init__(self,uptime,a,b,c,d):
		super().__init__(uptime)
		self._body[0]=[Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+' ',Back.RED+' ',Back.RED+'|']
		self._body[1]=[Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+' ',Back.RED+' ',Back.RED+'|']
		self._body[2]=[Back.CYAN+'S',Back.CYAN+'H',Back.CYAN+'O',Back.RED+'O',Back.RED+'T']
		self._body[3]=[Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+' ',Back.RED+' ',Back.RED+'|']
		self._body[4]=[Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+' ',Back.RED+' ',Back.RED+'|']
		self._pos_x=a
		self._pos_y=b
		self.__vel_x=c
		self.__vel_y=d
		self._id=2


	def update(self):
		if self._activated==1:
			if time.time()-self._upstart>self._uptime:
				self._activated=0
	def changex(self,a):
		self._pos_x+=a
	def changey(self,b):
		self._pos_y+=b
	def change_vel_x(self,c):
		self.__vel_x+=c
	def change_vel_y(self,d,grid):
		self.__vel_y+=d
		if self._pos_y>=40:
			self.clean(grid)
			self._render=0
		if self._pos_x > length-14:
			self._pos_x = length-14
		elif self._pos_x < 3:
			self._pos_x = 3
		if self._pos_y < 5:
			self._pos_y=4
		if self._pos_x > length-14:
			self.__vel_x = (-1)*self.__vel_x
		elif self._pos_x < 6:
			self.__vel_x = (-1)*self.__vel_x
		if self._pos_y < 5:
			self.__vel_y = (-1)*self.__vel_y
	def get_vel_x(self):
		return self.__vel_x
	def get_vel_y(self):
		return self.__vel_y
	def get_pos_y(self):
		return self._pos_y
	def setx(self,a):
		self._pos_x=a
	def sety(self,b):
		self._pos_y=b
	def printi(self,grid,paddle):
		print(self._pos_y)
		print(self._pos_x)
		grid[self._pos_y:self._pos_y+5,self._pos_x:self._pos_x+5]=self._body
		if self._pos_y>=40:
			self.clean(grid)
			self._render=0
		if self._pos_y>=38 and self._pos_x>=paddle.get_pos_x()-12 and self._pos_x<=paddle.get_pos_x()+9:
			self.initiate()
	def clean(self,grid):
		grid[self._pos_y:self._pos_y+5,self._pos_x:self._pos_x+5]=self._empty





