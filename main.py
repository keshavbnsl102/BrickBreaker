import os
import random
import signal
import time
import tty
from input import *
from colorama import Fore, Back, Style 
from headers import *
from background import *
from screen import *
from paddle import *
from ball import *
from bricks import *
from input2 import *
from powerups import *
from ufo import *
from bullets import *

time_var = time.time()
start_game = time.time()
refreshcount = 0
screen=Screen(breadth,length)
grid=screen.give_grid()
obj_scenery = background()
obj_scenery.create_ground(grid)
obj_scenery.create_sky(grid)
obj_paddle=paddle()
obj_ball=ball()
bricks=[]
level=1
old_level=1
bricks=addbrick(grid,level,obj_ball)
os.system("clear")
gameover=0
flag=0
level_start=time.time()
ufo=ufo()
bombs=[]
bomb_time_var=time.time()
ufo_fetch=0
gravity=1
shooting_power=0
fireball_power=0
bullets=[]
fireball_start=time.time()
shooting_start=time.time()
while True:
    
    if time.time() - time_var >= 0.15:
        time_var = time.time()
     

        

        updatebrick(grid,bricks)
        obj_paddle.erase_paddle(grid)
        obj_paddle.create(grid)
        obj_ball.erase_ball(grid)
        obj_ball.create(grid)
        print("\033[%d;%dH" % (40, 150))
        char=user_input()
        if char == "q":
            break
        elif char == "d":
            obj_paddle.set_values(4)
        elif char == "a":
            obj_paddle.set_values(-4)
        elif char==" ":
            obj_ball.start()
        elif char=="k" or old_level==level-1:
            if char=="k":
                level+=1
                level_start=time.time()
            for brick in bricks:
                brick.delete_brick(grid)
            bricks=addbrick(grid,level,obj_ball)
            old_level=level
        ax=obj_paddle.get_pos_x()
        by=obj_paddle.get_pos_y()
        a=obj_ball.get_vel_x()
        b=obj_ball.get_vel_y()
        aax=obj_ball.get_pos_x()
        bby=obj_ball.get_pos_y()
        obj_paddle.set_values(0)
        obj_paddle.place_paddle(grid)
        obj_ball.set_values(a,b)
        aax2=obj_ball.get_pos_x()
        bby2=obj_ball.get_pos_y()
        if level==4:
            ufo.ball_collision(aax2,bby2,obj_ball)
        for brick in bricks:
            if brick._health!=0:
                brick.collision(aax,bby,aax2,bby2,obj_ball,grid,bricks,fireball_power)
        if(obj_ball.get_bricks==0):
            level+=1
            level_start=time.time()

        c=obj_ball.update(grid,ax,by)
        if(c==1 and time.time()-level_start>20):
            flag+=1
            for brick in bricks:
                if brick.give_status()==0:
                    brick.delete_brick(grid)
                    brick.change_y(1)
                    brick.printfunc(grid)
            if(flag==14):
                gameover=1

        

                
        for brick in bricks:
            if brick.getid()==6 and brick.givehitstat()==0:
                brick.assign()
                brick.formation()
                brick.printfunc(grid)
        if level==4:
            ufo.update(grid,ax)
            ufo.printfunc(grid)
            char2=user_input()
            if char2=="u" and ufo_fetch<2:
                bricks=layer(grid)
                ufo_fetch+=1
            if time.time()-bomb_time_var>=1:
                bomb_time_var=time.time()
                bombs.append(bomb(ufo))
            for bomb_obj in bombs:
                bomb_obj.clean(grid)
                if bomb_obj.get_kill_stat()==0:
                    bomb_obj.change_y(3,grid)
                    bomb_obj.paddle_collision(ax,by,obj_ball)
                    if bomb_obj.get_kill_stat()==0:
                        bomb_obj.printfunc(grid)
        obj_paddle.place_paddle(grid)
        if shooting_power==1:
            obj_paddle.place_paddle2(grid)
            y=user_input()
            if y=="y":
                bullets.append(bulleti(obj_paddle.get_pos_x()-7,obj_paddle.get_pos_y()-2))
                bullets.append(bulleti(obj_paddle.get_pos_x()+7,obj_paddle.get_pos_y()-2))
            for bullet in bullets:
                if bullet.status()==0:
                    bullet.clean(grid)
                    bullet.change_y()
                    if bullet.get_pos_y()<=4:
                        bullet.kill()
                    bullet.create_bullet()
                    bullet.place_bullet(grid)
                    for brick in bricks:
                        a=brick.collision(bullet.get_pos_x()-1,bullet.get_pos_y()-1,bullet.get_pos_x(),bullet.get_pos_y(),obj_ball,grid,bricks,fireball_power)
                        if a==1:
                            bullet.kill()
                            bullet.clean(grid)
        for brick in bricks:
            if brick.give_status()==1:
                brick.delete_brick(grid)
            else:
                brick.printfunc(grid)
        for brick in bricks:
            if brick.give_status()==0:
                brick.printfunc(grid)
        obj_ball.place_ball(grid)

        for powe in powers:        
            if powe._render==1 :
                powe.clean(grid)
                powe.changey(powe.get_vel_y())
                powe.changex(powe.get_vel_x())
                if powe.get_pos_y()<=42:
                    powe.printi(grid,obj_paddle)
                powe.change_vel_y(gravity,grid)
            if powe._activated==1 and powe._id==2:
                shooting_power=1
                shooting_start=time.time()
                powe.update()
            if powe._activated==1 and powe._id==1:
                fireball_power=1
                fireball_start=time.time()
                powe.update()

        if time.time()-fireball_start>=10:
            fireball_power=0
        if time.time()-shooting_start>=10:
            shooting_power=0
        if fireball_power==1:
            obj_ball.fireball(grid)


        

        print("\033[%d;%dH" % (0, 0))
        # print(Fore.WHITE)
        # os.system("clear")
        if level==4:
            print("UFO health:",end="\t")
            for i in range(ufo.health()):
                print(Back.CYAN + "|",end=" ")
            for i in range(10-ufo.health()):
                print(" ",end=" ")
            print(" \t\t",end=" ")
        print(Back.CYAN + "Time:",end=" ")
        print(  1000 -(round(time.time()) - round(start_game)),end=" ")
        print("\t\t",end=" ")
        print(Back.CYAN+"Lives:",obj_ball.get_lives(),end=" ")
        print("\t\t",end=" ")
        print(Back.CYAN+"Score:",obj_ball.get_score(),end=" ")
        print("\t\t",end=" ")
        print()
        if shooting_power==1:
            print("Shooting power time left:",max(0,10-time.time()+shooting_start),end=" ")
        if fireball_power==1:
            print("fireball_power time left:",max(0,10-time.time()+fireball_start),end=" ")
        if fireball_power==0 and shooting_power==0 :
            for i in range(50):
                print(" ",end=" ")
        
        print()
        print(Style.RESET_ALL)
        screen.screen_display()
        if round(time.time()) - round(start_game)>1000:
            print("TIMES UP",end="\n")
            break
        if obj_ball.get_lives()<=0 or level>=5 or gameover==1:
            print("GAME OVER",end="\n")
            break
        if (ufo.health()==0):
            ufo.clean(grid)
            print("Player wins")
            
            break

        





