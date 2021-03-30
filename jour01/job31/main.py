#!/usr/bin/env python3
import random

notes = [random.randint(0,100) for i in range(35)]
notesModif = [0]*35

counter = 0
for note in notes:
    notesModif[counter] = calcNote(note)
    counter += 1

def calcNote(note):
    diff = note%5
    if diff>=3 :
       return note+1 if diff==4 else note+2
    else :
        return note
