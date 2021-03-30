#!/usr/bin/env python3

def draw_rectangle(width, height):
    extline = "|"
    for i in range(width-2):
        extline += "-"
    extline += "|"
    print(extline)

    for i in range(height-2):
        borderline="|"+" "*(width-2)+"|"
        print(borderline)
    print(extline)

draw_rectangle(14,4)
