import pgzrun
import pgzero.actor as actor
import pgzero.builtins as builtins
import pgzero.clock as clock
import pgzero.constants as constants
import pgzero.data as data
import pgzero.game as game
import pgzero.keyboard as keyboard
import pgzero.loaders as loaders
import pgzero.music as music
import pgzero.ptext as ptext
import pgzero.rect as rect
import pgzero.runner as runner
import pgzero.screen as screen
import pgzero.soundfmt as soundfmt
import pgzero.spellcheck as spellcheck
import pgzero.tone as tone

Nb_cases = 8
Grosseur_case = 50

WIDTH = Nb_cases * Grosseur_case
HEIGHT = Nb_cases * Grosseur_case

Map = ["11    22",
       "rr    gg",
       "        ",
       "        ",
       "        ",
       "        ",
       "bb    yy",
       "33    44"
       ]


def draw_background():
    for x in range(Nb_cases):
        for y in range(Nb_cases):
            screen.Screen.blit('case', x * Grosseur_case, y * Grosseur_case)
def draw_scenery():
    for y in range(Nb_cases):
        for x in range(Nb_cases):
            if Map[y][x] == 'r':
                screen.Screen.blit("redCase", x * Grosseur_case, y * Grosseur_case)
            elif Map[y][x] == '1':
                screen.Screen.blit("redCase", x * Grosseur_case, y * Grosseur_case)
            elif Map[y][x] == 'g':
                screen.Screen.blit('green_case', x * Grosseur_case, y * Grosseur_case)
            elif Map[y][x] == '2':
                screen.Screen.blit('green_case', x * Grosseur_case, y * Grosseur_case)
            elif Map[y][x] == 'b':
                screen.Screen.blit('blue_case', x * Grosseur_case, y * Grosseur_case)
            elif Map[y][x] == '3':
                screen.Screen.blit('blue_case', x * Grosseur_case, y * Grosseur_case)
            elif Map[y][x] == 'y':
                screen.Screen.blit('yellow_case', x * Grosseur_case, y * Grosseur_case)
            elif Map[y][x] == '4':
                screen.Screen.blit('yellow_case', x * Grosseur_case, y * Grosseur_case)

def setup_game():
    global redplayer
    redplayer[0] = actor.Actor('red', (0, 0))
    for y in range(Nb_cases):
        for x in range(Nb_cases):
            if Map[y][x] == '1':
                redplayer.draw(x * Grosseur_case, y * Grosseur_case)
            
def draw():
    draw_scenery()
    draw_background()

pgzrun.go()
