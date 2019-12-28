import os

import pygame
import py_midicsv
import sys
import random

csv_string = py_midicsv.midi_to_csv("midifile.mid")




new_csvstring = []

newtimestamp = 10000
modifynext = 0 

for x in csv_string:
    csvpart = x.split(",")
    if (csvpart[2] == " Note_on_c" and modifynext == 0 and int(csvpart[1]) > newtimestamp):
        modifynext = 2
    
    if (modifynext > 0 and csvpart[2] == " Note_on_c"):
        modifynext -= 1 
        if (modifynext == 0):
            newtimestamp += 10000 + random.randint(-2000,2000)
    else:
        new_csvstring.append(x)

with open("midifile_modified.mid", "wb") as ofile:
    midi_writer = py_midicsv.FileWriter(ofile)
    midi_writer.write(py_midicsv.csv_to_midi(new_csvstring))

def play(file):
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.8)

    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    clock = pygame.time.Clock()

    x = input()

play("midifile_modified.mid")