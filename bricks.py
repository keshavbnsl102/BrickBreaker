from headers import *
from colorama import Fore, Back, Style, init 
import random
import numpy as np
from powerups import *
init(autoreset=True)


class bricks:
	def __init__(self,a):
		self._pos_x=0
		self._pos_y=0
		self._health=0
		self._flag=0
		self._id=0
		self._index=0
		self._kill=0
		self._hitstatus=0
		self._body = np.zeros((5, 5), dtype='<U20')

		self._empty = np.zeros((5, 5), dtype='<U20')
		self._empty[:] = ' '

	def change_y(self,a):
		self._pos_y+=a
	def give_status(self):
		return self._kill
	def getid(self):
		return self._id
	def assign(self):
		self._health=random.randint(2,20)
	def givehitstat(self):
		return self._hitstatus
	def get_pos_x(self):
		return self._pos_x
	def get_pos_y(self):
		return self._pos_y
	def reducehealth(self):
		self._health-=1
	def kill(self):
		self._kill=1

	def collision(self,aax,bby,aax2,bby2,ball,grid,bricks,fire):
		if aax2<self._pos_x+5 and aax2>=self._pos_x and bby2<self._pos_y+5 and bby2>=self._pos_y:
			self._health=self._health-1
			self._hitstatus=1
			m=random.randint(0,1)
			
			ball.scorechange(1)
			objectify=self
			f=1
			if self._health==0:
				self.delete_brick(grid)
				ball.scorechange(5)
				ball.subtract(1)
				self._kill=1
				if m==0:
					powerup_exp=expand(10,self._pos_x,self._pos_y,ball.get_vel_x(),ball.get_vel_y())
					powerup_exp._render=1
					powers.append(powerup_exp)
				elif m==1:
					powerup_exp=shooting(10,self._pos_x,self._pos_y,ball.get_vel_x(),ball.get_vel_y())
					powerup_exp._render=1
					powers.append(powerup_exp)

			if aax2<=aax and bby2>=bby:
				if (self._pos_x+4-aax-(self._pos_y-bby)*((aax2-aax)/(bby2-bby)))<0:
					ball.invertxvel()
					# ball._pos_x+=ball._vel_x
					# ball._pos_y+=ball._vel_y
				else:
					ball.invertyvel()
					# ball._pos_x+=ball._vel_x
					# ball._pos_y+=ball._vel_y
			elif aax2>=aax and bby2>=bby:
				if (self._pos_x-aax-(self._pos_y-bby)*((aax2-aax)/(bby2-bby)))<0:
					ball.invertyvel()
					# ball._pos_x+=ball._vel_x
					# ball._pos_y+=ball._vel_y
				else:
					ball.invertxvel()
					# ball._pos_x+=ball._vel_x
					# ball._pos_y+=ball._vel_y
			elif aax2<=aax and bby2<=bby:
				if (self._pos_x+4-aax-(self._pos_y+4-bby)*((aax2-aax)/(bby2-bby)))<0:
					ball.invertxvel()
					# ball._pos_x+=ball._vel_x
					# ball._pos_y+=ball._vel_y
				else:
					ball.invertyvel()
					# ball._pos_x+=ball._vel_x
					# ball._pos_y+=ball._vel_y
			elif aax2>=aax and bby2<=bby:
				if (self._pos_x-aax-(self._pos_y+4-bby)*((aax2-aax)/(bby2-bby)))<0:
					ball.invertyvel()
					# ball._pos_x+=ball._vel_x
					# ball._pos_y+=ball._vel_y
				else:
					ball.invertxvel()
					# ball._pos_x+=ball._vel_x
					# ball._pos_y+=ball._vel_y
			if self._id==3 or fire:
				m=self._index
				brickis=[]
				brickis.append(self)
				while len(brickis)!=0:
					f=brickis[0]
					m=f._index
					x=f._pos_x
					y=f._pos_y
					brickis.pop(0)
					for bro in bricks:
						if bro._pos_x==x-5 and bro._pos_y==y:
							brick1=bro
							brick1.delete_brick(grid)
							brick1._kill=1
							ball.scorechange(5)
							if brick1._id!=3:
								brick1._health=0
							if brick1._id==3 and brick1._health>0:
								brick1._health=0
								brickis.append(brick1)
						if bro._pos_x==x+5 and bro._pos_y==y:
							brick2=bro
							brick2.delete_brick(grid)
							brick2._kill=1
							ball.scorechange(5)
							if brick2._id!=3:
								brick2._health=0
							if brick2._id==3 and brick2._health>0:
								brick2._health=0
								brickis.append(brick2)
						if bro._pos_x==x and bro._pos_y==y+5:
							brick3=bro
							brick3.delete_brick(grid)
							brick3._kill=1
							ball.scorechange(5)
							if brick3._id!=3:
								brick3._health=0
							if brick3._id==3 and brick3._health>0:
								brick3._health=0
								brickis.append(brick3)
						if bro._pos_x==x and bro._pos_y==y-5:
							brick4=bro
							brick4.delete_brick(grid)
							brick4._kill=1
							ball.scorechange(5)
							if brick4._id!=3:
								brick4._health=0
							if brick4._id==3 and brick4._health>0:
								brick4._health=0
								brickis.append(brick4)
						if bro._pos_x==x+5 and bro._pos_y==y-5:
							brick5=bro
							brick5.delete_brick(grid)
							brick5._kill=1
							ball.scorechange(5)
							if brick5._id!=3:
								brick5._health=0
							if brick5._id==3 and brick5._health>0:
								brick5._health=0
								brickis.append(brick5)
						if bro._pos_x==x+5 and bro._pos_y==y+5:
							brick6=bro
							brick6.delete_brick(grid)
							brick6._kill=1
							ball.scorechange(5)
							if brick6._id!=3:
								brick6._health=0
							if brick6._id==3 and brick6._health>0:
								brick6._health=0
								brickis.append(brick6)
						if bro._pos_x==x-5 and bro._pos_y==y+5:
							brick7=bro
							brick7.delete_brick(grid)
							brick7._kill=1
							ball.scorechange(5)
							if brick7._id!=3:
								brick7._health=0
							if brick7._id==3 and brick7._health>0:
								brick7._health=0
								brickis.append(brick7)
						if bro._pos_x==x-5 and bro._pos_y==y-5:
							brick8=bro
							brick8.delete_brick(grid)
							brick8._kill=1
							ball.scorechange(5)
							if brick8._id!=3:
								brick8._health=0
							if brick8._id==3 and brick8._health>0:
								brick8._health=0
								brickis.append(brick8)
			return 1	


		else:
			return 0
	def formation(self):
		if self._health<=10 and self._health>7:
			self._body[0]=[Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+'|']
			self._body[1]=[Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+'|']
			self._body[2]=[Back.RED+' ',Back.RED+' ',Back.RED+'o',Back.RED+' ',Back.RED+'|']
			self._body[3]=[Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+'|']
			self._body[4]=[Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+'|']
		elif self._health<=7 and self._health>3:
			self._body[0]=[Back.YELLOW+' ',Back.YELLOW+' ',Back.YELLOW+' ',Back.YELLOW+' ',Back.YELLOW+'|']
			self._body[1]=[Back.YELLOW+' ',Back.YELLOW+' ',Back.YELLOW+' ',Back.YELLOW+' ',Back.YELLOW+'|']
			self._body[2]=[Back.YELLOW+' ',Back.YELLOW+' ',Back.YELLOW+'o',Back.YELLOW+' ',Back.YELLOW+'|']
			self._body[3]=[Back.YELLOW+' ',Back.YELLOW+' ',Back.YELLOW+' ',Back.YELLOW+' ',Back.YELLOW+'|']
			self._body[4]=[Back.YELLOW+' ',Back.YELLOW+' ',Back.YELLOW+' ',Back.YELLOW+' ',Back.YELLOW+'|']
		elif self._health<=3 and self._health>1:
			self._body[0]=[Back.BLUE+Style.BRIGHT+' ',Back.BLUE+Style.BRIGHT+' ',Back.BLUE+Style.BRIGHT+' ',Back.BLUE+Style.BRIGHT+' ',Back.BLUE+Style.BRIGHT+'|']
			self._body[1]=[Back.BLUE+Style.BRIGHT+' ',Back.BLUE+Style.BRIGHT+' ',Back.BLUE+Style.BRIGHT+' ',Back.BLUE+Style.BRIGHT+' ',Back.BLUE+Style.BRIGHT+'|']
			self._body[2]=[Back.BLUE+Style.BRIGHT+' ',Back.BLUE+Style.BRIGHT+' ',Back.BLUE+Style.BRIGHT+'o',Back.BLUE+Style.BRIGHT+' ',Back.BLUE+Style.BRIGHT+'|']
			self._body[3]=[Back.BLUE+Style.BRIGHT+' ',Back.BLUE+Style.BRIGHT+' ',Back.BLUE+Style.BRIGHT+' ',Back.BLUE+Style.BRIGHT+' ',Back.BLUE+Style.BRIGHT+'|']
			self._body[4]=[Back.BLUE+Style.BRIGHT+' ',Back.BLUE+Style.BRIGHT+' ',Back.BLUE+Style.BRIGHT+' ',Back.BLUE+Style.BRIGHT+' ',Back.BLUE+Style.BRIGHT+'|']







class redbricks(bricks):
	def __init__(self,a,b):
		super().__init__(2)
		self._pos_x=a
		self._pos_y=b
		self._health=10
		self._id=1
		self._body[0]=[Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+'|']
		self._body[1]=[Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+'|']
		self._body[2]=[Back.RED+' ',Back.RED+' ',Back.RED+'o',Back.RED+' ',Back.RED+'|']
		self._body[3]=[Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+'|']
		self._body[4]=[Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+'|']
	def printfunc(self,grid):
		grid[self._pos_y:self._pos_y+5,self._pos_x:self._pos_x+5]=self._body


	def delete_brick(self,grid):
		grid[self._pos_y:self._pos_y+5,self._pos_x:self._pos_x+5]=self._empty



class yellowbricks(bricks):
	def __init__(self,a,b):
		super().__init__(2)
		self._pos_x=a
		self._pos_y=b
		self._health=7
		self._id=2
		self._body[0]=[Back.YELLOW+' ',Back.YELLOW+' ',Back.YELLOW+' ',Back.YELLOW+' ',Back.YELLOW+'|']
		self._body[1]=[Back.YELLOW+' ',Back.YELLOW+' ',Back.YELLOW+' ',Back.YELLOW+' ',Back.YELLOW+'|']
		self._body[2]=[Back.YELLOW+' ',Back.YELLOW+' ',Back.YELLOW+'o',Back.YELLOW+' ',Back.YELLOW+'|']
		self._body[3]=[Back.YELLOW+' ',Back.YELLOW+' ',Back.YELLOW+' ',Back.YELLOW+' ',Back.YELLOW+'|']
		self._body[4]=[Back.YELLOW+' ',Back.YELLOW+' ',Back.YELLOW+' ',Back.YELLOW+' ',Back.YELLOW+'|']

	def printfunc(self,grid):
		grid[self._pos_y:self._pos_y+5,self._pos_x:self._pos_x+5]=self._body

	def delete_brick(self,grid):
		grid[self._pos_y:self._pos_y+5,self._pos_x:self._pos_x+5]=self._empty


class explosive(bricks):
	def __init__(self,a,b):
		super().__init__(2)
		self._pos_x=a
		self._pos_y=b
		self._health=1
		self._id=3
		self._body[0]=[Back.MAGENTA+' ',Back.MAGENTA+' ',Back.MAGENTA+' ',Back.MAGENTA+' ',Back.MAGENTA+'|']
		self._body[1]=[Back.MAGENTA+' ',Back.MAGENTA+' ',Back.MAGENTA+' ',Back.MAGENTA+' ',Back.MAGENTA+'|']
		self._body[2]=[Back.MAGENTA+' ',Back.MAGENTA+' ',Back.MAGENTA+'o',Back.MAGENTA+' ',Back.MAGENTA+'|']
		self._body[3]=[Back.MAGENTA+' ',Back.MAGENTA+' ',Back.MAGENTA+' ',Back.MAGENTA+' ',Back.MAGENTA+'|']
		self._body[4]=[Back.MAGENTA+' ',Back.MAGENTA+' ',Back.MAGENTA+' ',Back.MAGENTA+' ',Back.MAGENTA+'|']

	def printfunc(self,grid):
		grid[self._pos_y:self._pos_y+5,self._pos_x:self._pos_x+5]=self._body

	def delete_brick(self,grid):
		grid[self._pos_y:self._pos_y+5,self._pos_x:self._pos_x+5]=self._empty

class bluebricks(bricks):
	def __init__(self,a,b):
		super().__init__(2)
		self._pos_x=a
		self._pos_y=b
		self._health=3
		self._id=4
		self._body[0]=[Back.GREEN+' ',Back.GREEN+' ',Back.GREEN+' ',Back.GREEN+' ',Back.GREEN+'|']
		self._body[1]=[Back.GREEN+' ',Back.GREEN+' ',Back.GREEN+' ',Back.GREEN+' ',Back.GREEN+'|']
		self._body[2]=[Back.GREEN+' ',Back.GREEN+' ',Back.GREEN+'o',Back.GREEN+' ',Back.GREEN+'|']
		self._body[3]=[Back.GREEN+' ',Back.GREEN+' ',Back.GREEN+' ',Back.GREEN+' ',Back.GREEN+'|']
		self._body[4]=[Back.GREEN+' ',Back.GREEN+' ',Back.GREEN+' ',Back.GREEN+' ',Back.GREEN+'|']

	def printfunc(self,grid):
		grid[self._pos_y:self._pos_y+5,self._pos_x:self._pos_x+5]=self._body


	def delete_brick(self,grid):
		grid[self._pos_y:self._pos_y+5,self._pos_x:self._pos_x+5]=self._empty

class unbreakable(bricks):
	def __init__(self,a,b):
		super().__init__(2)
		self._pos_x=a
		self._pos_y=b
		self._health=10000
		self._id=5
		self._body[0]=[Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+'|']
		self._body[1]=[Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+'|']
		self._body[2]=[Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+'o',Back.CYAN+' ',Back.CYAN+'|']
		self._body[3]=[Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+'|']
		self._body[4]=[Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+'|']

	def printfunc(self,grid):
		grid[self._pos_y:self._pos_y+5,self._pos_x:self._pos_x+5]=self._body


	def delete_brick(self,grid):
		grid[self._pos_y:self._pos_y+5,self._pos_x:self._pos_x+5]=self._empty

class rainbow(bricks):
	def __init__(self,a,b):
		super().__init__(2)
		self._pos_x=a
		self._pos_y=b
		self._health=5
		self._id=6
		self._hitstatus=0
		self._body[0]=[Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+'|']
		self._body[1]=[Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+'|']
		self._body[2]=[Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+'o',Back.CYAN+' ',Back.CYAN+'|']
		self._body[3]=[Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+'|']
		self._body[4]=[Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+'|']

	def printfunc(self,grid):
		grid[self._pos_y:self._pos_y+5,self._pos_x:self._pos_x+5]=self._body


	def delete_brick(self,grid):
		grid[self._pos_y:self._pos_y+5,self._pos_x:self._pos_x+5]=self._empty



def addbrick(grid,level,ball): 
	bricks=[]
	if level==1:
		x=26 
		y=8
		k=0
		for i in range(4):
			for j in range(21):
				a=random.randint(0,5)
				if a==0:
					brick=redbricks(x,y)
					brick.printfunc(grid)
					brick._index=k
					bricks.append(brick)
				elif a==1:
					brick=yellowbricks(x,y)
					brick.printfunc(grid)
					brick._index=k
					bricks.append(brick)
				elif a==2:
					brick=bluebricks(x,y)
					brick.printfunc(grid)
					brick._index=k
					bricks.append(brick)
				elif a==3:
					brick=unbreakable(x,y)
					brick.printfunc(grid)
					brick._index=k
					bricks.append(brick)
				elif a==4:
					brick=explosive(x,y)
					brick.printfunc(grid)
					brick._index=k
					bricks.append(brick)
				elif a==5:
					brick=rainbow(x,y)
					brick.printfunc(grid)
					brick._index=k
					bricks.append(brick)

				x+=5
				k+=1
			x=26	
			y+=5

	elif level==2:
		x=26
		y=23
		z=21
		m=26
		k=0
		for i in range(4):
			for j in range(z):
				a=random.randint(0,5)
				if a==0:
					brick=redbricks(x,y)
					brick.printfunc(grid)
					brick._index=k
					bricks.append(brick)
				elif a==1:
					brick=yellowbricks(x,y)
					brick.printfunc(grid)
					brick._index=k
					bricks.append(brick)
				elif a==2:
					brick=bluebricks(x,y)
					brick.printfunc(grid)
					brick._index=k
					bricks.append(brick)
				elif a==3:
					brick=unbreakable(x,y)
					brick.printfunc(grid)
					brick._index=k
					bricks.append(brick)
				elif a==4:
					brick=explosive(x,y)
					brick.printfunc(grid)
					brick._index=k
					bricks.append(brick)
				elif a==5:
					brick=rainbow(x,y)
					brick.printfunc(grid)
					brick._index=k
					bricks.append(brick)
				x+=5
				k+=1
			x=m+5
			m+=5
			y-=5
			z-=2

	elif level==3:
		x=26
		y=23
		z=21
		m=26
		k=0
		for i in range(4):

			if i==0 or i==1:
				for j in range(z):
					a=random.randint(0,5)
					if a==0:
						brick=redbricks(x,y)
						brick.printfunc(grid)
						brick._index=k
						bricks.append(brick)
					elif a==1:
						brick=yellowbricks(x,y)
						brick.printfunc(grid)
						brick._index=k
						bricks.append(brick)
					elif a==2:
						brick=bluebricks(x,y)
						brick.printfunc(grid)
						brick._index=k
						bricks.append(brick)
					elif a==3:
						brick=unbreakable(x,y)
						brick.printfunc(grid)
						brick._index=k
						bricks.append(brick)
					elif a==4:
						brick=explosive(x,y)
						brick.printfunc(grid)
						brick._index=k
						bricks.append(brick)
					elif a==5:
						brick=rainbow(x,y)
						brick.printfunc(grid)
						brick._index=k
						bricks.append(brick)
					x+=5
					k+=1

			else:
				x=26
				for j in range(int(z/3)):
					a=random.randint(0,5)
					if a==0:
						brick=redbricks(x,y)
						brick.printfunc(grid)
						brick._index=k
						bricks.append(brick)
					elif a==1:
						brick=yellowbricks(x,y)
						brick.printfunc(grid)
						brick._index=k
						bricks.append(brick)
					elif a==2:
						brick=bluebricks(x,y)
						brick.printfunc(grid)
						brick._index=k
						bricks.append(brick)
					elif a==3:
						brick=unbreakable(x,y)
						brick.printfunc(grid)
						brick._index=k
						bricks.append(brick)
					elif a==4:
						brick=explosive(x,y)
						brick.printfunc(grid)
						brick._index=k
						bricks.append(brick)
					elif a==5:
						brick=rainbow(x,y)
						brick.printfunc(grid)
						brick._index=k
						bricks.append(brick)
					x+=5
					k+=1
				x=96
				for j in range(int(z/3)):
					a=random.randint(0,5)
					if a==0:
						brick=redbricks(x,y)
						brick.printfunc(grid)
						brick._index=k
						bricks.append(brick)
					elif a==1:
						brick=yellowbricks(x,y)
						brick.printfunc(grid)
						brick._index=k
						bricks.append(brick)
					elif a==2:
						brick=bluebricks(x,y)
						brick.printfunc(grid)
						brick._index=k
						bricks.append(brick)
					elif a==3:
						brick=unbreakable(x,y)
						brick.printfunc(grid)
						brick._index=k
						bricks.append(brick)
					elif a==4:
						brick=explosive(x,y)
						brick.printfunc(grid)
						brick._index=k
						bricks.append(brick)
					elif a==5:
						brick=rainbow(x,y)
						brick.printfunc(grid)
						brick._index=k
						bricks.append(brick)
					x+=5
					k+=1


			x=26
			y-=5

	return bricks

def layer(grid):
	bricks=[]
	x=6
	y=20
	k=0
	for i in range(1):
		for j in range(28):
			a=random.randint(0,5)
			if a==0:
				brick=redbricks(x,y)
				brick.printfunc(grid)
				brick._index=k
				bricks.append(brick)
			elif a==1:
				brick=yellowbricks(x,y)
				brick.printfunc(grid)
				brick._index=k
				bricks.append(brick)
			elif a==2 or a==3:
				brick=bluebricks(x,y)
				brick.printfunc(grid)
				brick._index=k
				bricks.append(brick)
			elif a==4:
				brick=explosive(x,y)
				brick.printfunc(grid)
				brick._index=k
				bricks.append(brick)
			elif a==5:
				brick=rainbow(x,y)
				brick.printfunc(grid)
				brick._index=k
				bricks.append(brick)

			x+=5
			k+=1
		x=6	
		y+=5
	return bricks
		


def updatebrick(grid,bricks):
	for brick in bricks:
		if brick._health!=0:
			brick.formation()
			brick.printfunc(grid)






