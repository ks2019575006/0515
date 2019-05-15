import turtle as t

def write_ab(x,y):
    t.goto(x,y)
    t.stamp()
    t.write("x:%d, y:%d"%(x,y))

def screen_clear(x,y):
    t.goto(x,y)
    t.clear()

t.setup(600,600)
s=t.Screen()
t.penup()
s.onscreenclick(write,xy,1)
s.onscreenclick(screen,clear,3)
s.listen()
            
