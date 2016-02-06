import argparse
import yaml

PLAYER_FILE="player.yml"
from Thing import *
from Room import *
from Item import *
import Player

def status(args):
    print("I have some status")

def move(args):
    print("Moved to a place")

def act(args):
    print("Act in a way")

def look(args):
    with open('rooms.yml', 'r') as f:
        doc = yaml.load(f)
    room = doc[player.data['room']]
    if len(args)==0:
        txt = room["desc"]
    else:
        thingToLookAt=args.pop(0)
        if thingToLookAt in room["rooms"]:
            txt=room["rooms"][thingToLookAt]["desc"]
        else:
            txt=None
            for itemdict in room["items"]:
                if thingToLookAt in itemdict:
                    txt=itemdict[thingToLookAt][0]["desc"]
            if txt == None:
                txt="?????"
    print(txt)

parser = argparse.ArgumentParser(description='Play the Game')

# show status by default
parser.set_defaults(func=status)

subparsers = parser.add_subparsers()

moveparse = subparsers.add_parser('move', help='move somewhere')
moveparse.add_argument('args', metavar='ARG', type=int, nargs='*',
                       help='everything else')
moveparse.set_defaults(func=move)

actparse = subparsers.add_parser('act', help='act')
actparse.add_argument('args', metavar='ARG', type=int, nargs='*',
                      help='everything else')
actparse.set_defaults(func=act)

lookparse = subparsers.add_parser('look', help='look')
lookparse.add_argument('args', metavar='ARG', nargs='*',
                      help='everything else')
lookparse.set_defaults(func=look)


if __name__ == "__main__":
    player=Player.load(PLAYER_FILE)
    args = parser.parse_args()
    # func is set by set_defaults
    args.func(args.args) #args args args args args args args argsargs args args argsargs args args argsargs args args argsargs args args argsargs args args args
    player.save(PLAYER_FILE)
