import random
import curses
import time
screen=curses.initscr()
curses.curs_set(0)
score = 0
xtime=100

screen_height,screen_width=screen.getmaxyx() #unpackiing
newWindow=curses.newwin(screen_height,screen_width,0,0)

newWindow.keypad(True)
#newWindow.timeout(100)

snake_x= screen_width//4
snake_y=screen_height//2


snakeBody=[
  [snake_y,snake_x],
  [snake_y,snake_x-1],
  [snake_y,snake_x-2]
]

food=[screen_height//2,screen_width//2]
newWindow.addch(food[0],food[1],curses.ACS_PI)

key=curses.KEY_RIGHT

while True:
  newWindow.addstr(1,screen_width//2,f"Score {score}") 
  newWindow.timeout(max(50,60-score*5))
  
  nweKey=newWindow.getch()
  key= key if nweKey == -1 else nweKey 
  if snakeBody[0][0] in [0,screen_height-1] or snakeBody[0][1] in [0,screen_width-1] or snakeBody[0] in snakeBody[1:]:
     curses.endwin()
     endMessageScreen=curses.newwin(screen_height,screen_width,0,0)
     cor=[screen_height//2,screen_width//2]
     endMessageScreen.addstr(cor[0],cor[1],"Game Over")
     endMessageScreen.refresh()  #لازم `refresh()` عشان الـ `curses` يعرض التغييرات من الذاكرة المؤقتة (buffer) على الشاشة فعليًا. 😊
     time.sleep(2) 
     curses.endwin()
     quit()


  new_Hed=[snakeBody[0][0],snakeBody[0][1]]
  if key==curses.KEY_DOWN:
    new_Hed[0]+=1
  if key==curses.KEY_UP:
    new_Hed[0]-=1  
  if key==curses.KEY_RIGHT:
    new_Hed[1]+=1  
  if key==curses.KEY_LEFT:
    new_Hed[1]-=1  
  snakeBody.insert(0,new_Hed)

  if snakeBody[0]==food:
    score+=1
    food=None

    while food is None:
      nwe_food=[random.randint(1,screen_height-1),random.randint(1,screen_width-1)]
      food =nwe_food if nwe_food not in snakeBody else None

    newWindow.addch(food[0],food[1],curses.ACS_PI)

  else:
   tail=snakeBody.pop()
   newWindow.addch(tail[0],tail[1],' ')

   newWindow.addch(snakeBody[0][0],snakeBody[0][1],curses.ACS_CKBOARD)


