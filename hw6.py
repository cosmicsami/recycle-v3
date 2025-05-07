import random,pgzrun

WIDTH=1100
HEIGHT=700
ITEMS=["R","OIP"]
level=1
actors=[]
animation=[]


def draw():
    screen.blit("ghz",(-20,0))


def picker(level):
    objects=["OIP"]
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
    for i,v in enumerate (actors):
        v.pos=(i+1)*gap_size,0

pgzrun.go()