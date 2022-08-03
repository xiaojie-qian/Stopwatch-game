# template for "Stopwatch: The Game"
import simplegui
# define global variables
t = 0 
tried = 0
count = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global d
    pass
    d = (t%600)%10
    c = ((t%600)//10)%10 
    b = (t%600)//100 
    a = t//600
    return str(a)+":"+str(b)+str(c)+"."+str(d)
   
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global t 
    t += 1
    timer.start()
    format(t)

    
def stop_handler():
    timer.stop()
    global count, tried
    if d == 0:
        count += 1
        tried += 1
    else:
        tried += 1
    format(t)

    
def reset_handler(): 
    global t,count,tried
    timer.stop()
    t = 0
    format(t)
    count = 0
    tried = 0
    
# define event handler for timer with 0.1 sec interval
timer = simplegui.create_timer(100, start_handler)

# define draw handler
def draw(canvas):
    canvas.draw_text(format(t), [60, 130], 30, "yellow")
    canvas.draw_text(str(count) + "/" + str(tried), [160, 20], 20, "White")
    
# create frame
f = simplegui.create_frame("Stopwatch", 200, 250)

# register event handlers
f.add_label("Press 'start' to start the watch.")
f.add_label("Press 'stop' when you think you get whole second.")                       
f.add_button("start", start_handler,100)
f.add_button("stop", stop_handler,100)
f.add_button("reset", reset_handler,100)
f.set_draw_handler(draw)

# start frame
f.start()


# Please remember to review the grading rubric
