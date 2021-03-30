#!/usr/bin/env python3

def draw_triangle(height):
    for i in range(height):
        line = " "*(height-i)+"/"+" "*(2*i)+"\\"
        if i == height-1:
            line = " "*(height-i) + "/"+"_"*(2*i)+"\\"
        print(line)

draw_triangle(5)
