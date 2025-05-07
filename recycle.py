import random,pgzrun
WIDTH=600
HEIGHT=600
ITEMS=["bag","battery","bottle","crisps"]
level=1
actors=[]
animation=[]
game_state="ready" 
def draw():
    screen.blit('bground',(0,0))
    if game_state=="play":
         for i in actors:
            i.draw ()
    elif game_state=="ready":
        screen.draw.text("hit the paper bag to win\n there are 6 levels\n click to start",fontsize=30,center=(WIDTH/2,HEIGHT/2),color="white")
    elif game_state=="win":
        screen.draw.text("you win!!!!!!!!!!!!!!!!!!",fontsize=30,center=(WIDTH/2,HEIGHT/2),color="white")
    elif game_state=="game_over":
        screen.draw.text("you are out G4ME__0VER",fontsize=30,center=(WIDTH/2,HEIGHT/2),color="white")

def update():
    global actors
    if game_state=="play":
        if len(actors)==0:
            actors=making_items(level)
    
def making_items(level):
    objects=picker(level)
    actors=making_actors(objects)
    layout(actors)
    speed(actors)
    return actors
def picker(level):
    objects=["paper"]
    for i in range(level):
        objects.append(random.choice(ITEMS))
    return objects
def making_actors(objects):
    actors=[]
    for i in objects:
        actors.append(Actor(i+"img"))
    return actors
def layout(actors):
    nog=len(actors)+1 
    gap_size=WIDTH//nog
    random.shuffle(actors)
    for i,v in enumerate (actors):
        v.pos=(i+1)*gap_size,0
def speed(actors):
    global animation
    for i in actors:
        duration=10-level
        i.anchor=("center","bottom")
        a=animate(i,duration=duration,on_finished=game_over,y=HEIGHT)
        animation.append(a)

def game_over():
    global game_state
    print("g4me_0ver")
    game_state="game_over"
def on_mouse_down (pos):
    global level,animation,actors,game_state
    if game_state=="ready":
        game_state="play"
    for i in actors:
        if i.collidepoint(pos):
            if "paper" in i.image:
                if level==6:
                     game_state="win"
                else:     
                    level=level+1
                    actors=[]
                    animation=[]

pgzrun.go()
