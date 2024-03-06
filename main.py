import pgzrun
import random

#creating title of game window
TITLE = "Eat the Burger"

#setting width and height of game window
WIDTH = 1000
HEIGHT = 1000

#creating a variable to store a message
message = ""

#creating actors-actors are game objects
burger = Actor("burger")
burger.pos=50,50

#creating function draw
#this is automatically called by system. instructions that we want continuously repeated are written in function draw
#function draw is an endless loop which keeps repeating until code is running
def draw() :
    screen.clear()
    screen.fill(color=(128,0,0))
    screen.draw.text(message,center=[400,10],fontsize=30)
    #instruction to draw burger on screen
    burger.draw()
    
#creating a function to change burger position
def place_burger() :
    burger.x = random.randint(50,WIDTH-50)
    burger.y = random.randint(50,HEIGHT-50)

def on_mouse_down(pos) :
    if burger.collidepoint(pos):
        message = "Keep Eating!"
        place_burger()
    
    else :
        message = "try again"

place_burger()


#function must be called to start processing
pgzrun.go()