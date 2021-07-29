## Name : keshav bansal
## Roll No. : 2019101019

---
### ASSIGNMENT3: ADDITIONS
* Levels: press "K" key to go to the next level , 4 levels implemented, 4th one is the boss level

* For falling bricks, I have taken the time limit to be 20 seconds, which means after 20 seconds into a level,the whole layout will start shifting by 1 unit everytime the ball hits the paddle.
* The shooting powerup is active for 10 seconds and bullets can be shot using 'y' key.
* powerup 2.0 implemented
* Rainbow bricks implemented
* Boss enemy can use the 'U ' key to spawn bricks as defense mechanism

* Bonus- Fireball powerup implemented 






### Rules :

* The player has 10 lives and a time of 100 seconds to comlete the game.
* Once the ball goes below the board it gets respawned on the paddle
* For one collision with the brick the score increases by one
* When a brick gets killed the score increases by 5.
* I have used bricks in 3 colors which are red, yellow and blue.
* health of the brick is the number of collisions with the ball that are required to destroy the brick.
* The brick stays in red colour if the health of the brick is within a range of 7 and 10.
* For a brick to be in yellow colour the health is within range of 3 and 7.
* Brick of blue colour has health in the range between 1 and 3.
* Magenta coloured bricks are explosive bricks which when collided by a ball gets destroyed and destroys all the  
  bricks that are adjacent to it, which can be vertically, horizontally as well as diagonally.
* Cyan coloured bricks are unbreakable and I have kept their health to be a very large number in order to make sure that they dont get destroyed.

---

### Functionalities:

* The bricks changes colours when collided by a ball a particular number of times.
* The colllisions of the ball with the bricks have been handled using line intersection formula.
*  I have handled the movement of the powerups
* Could not implement all the power ups
* I have done the bonus which is explosive bricks 
