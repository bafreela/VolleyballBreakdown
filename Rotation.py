#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 19:44:19 2018
Purpose: Simulate a volleyball rotation
Author: Brock Freeland
"""

import turtle


def rotate(l, n):
    '''
    Reverses the list in the court function in order to simulate
    a volleyball rotation

    Parameters:
        l: the list of colors (positions)
        n: the change of the index of colors

    Return value: rotated position in the list
    '''
    return l[n:]+ l[:n] #returns position value for color change in player function

def court(tortoise,rotations):
    '''
    Uses turtle graphics to create a volleyball court

    Parameters:
        tortoise: turtle object
        rotations: number of position rotations for players

    Return value: None
    '''
    #draws the volleyball court
    tortoise.speed(100)
    tortoise.up()
    tortoise.goto(-200,-200)
    tortoise.down()
    tortoise.width(3)
    for segment in range(4):    #draws the square boundaries of the court
        tortoise.forward(400)
        tortoise.left(90)

    tortoise.goto(-200,0)   #draws the net
    tortoise.forward(400)

    players(tortoise,rotations) #calls player function with turtle object and number of rotations


def extras(tortoise):
    """
    Creates the additional objects in the volleyball court

    Parameters:
        tortoise: turtle object

    Return Value: None
    """

    #10 foot line for each side of court
    tortoise.speed(100)
    tortoise.up()
    tortoise.goto(-200,62)
    tortoise.pencolor("red")
    tortoise.down()
    tortoise.forward(400)

    tortoise.up()
    tortoise.goto(-200,-62)
    tortoise.pencolor("red")
    tortoise.down()
    tortoise.forward(400)


    #REFs

    tortoise.up()
    tortoise.goto(230,-20)
    tortoise.fillcolor("black")
    tortoise.pencolor("black")
    tortoise.down()
    tortoise.begin_fill()
    tortoise.circle(20)
    tortoise.end_fill()

    tortoise.up()
    tortoise.goto(-230,-20)
    tortoise.fillcolor("black")
    tortoise.pencolor("black")
    tortoise.down()
    tortoise.begin_fill()
    tortoise.circle(20)
    tortoise.end_fill()

# scores table
    tortoise.up()
    tortoise.goto(275,-50)
    tortoise.left(90)
    tortoise.fillcolor("white")
    tortoise.pencolor("black")
    tortoise.down()
    tortoise.begin_fill()
    tortoise.forward(120)
    tortoise.right(90)
    tortoise.forward(50)
    tortoise.right(90)
    tortoise.forward(120)
    tortoise.right(90)
    tortoise.forward(50)
    tortoise.end_fill()


#stands


    tortoise.up()
    tortoise.goto(-275,250)
    tortoise.left(90)
    tortoise.fillcolor("white")
    tortoise.pencolor("black")
    tortoise.down()
    tortoise.begin_fill()
    tortoise.forward(500)
    tortoise.right(90)
    tortoise.forward(50)
    tortoise.right(90)
    tortoise.forward(500)
    tortoise.right(90)
    tortoise.forward(50)
    tortoise.end_fill()

def players(tortoise,rotations):
    """
    Creates circles that represent volleyball players with turtle graphics

    Parameters:
        tortoise: turtle object
        rotations: number of position rotations for the players

    Return Value: None
    """

    extras(tortoise)

    
    position = ['white', 'white', 'white', 'white', 'white', 'red'] #list of colors for players
    tortoise.width(2)
    tortoise.speed(15)

    for index in range(rotations+1): #rotates the players positions by one
        position=rotate(position, -1) #calls rotate to cycle through color position for each player



 #TEAM 1

        tortoise.up()
        tortoise.goto(110,-60)
        tortoise.fillcolor(position[2]) #sets color as index color in list (position)
        tortoise.pencolor("black")
        tortoise.down()
        tortoise.begin_fill()
        tortoise.circle(25) #represents player as circle 
        tortoise.end_fill()

#repeats steps for each of the following players
        tortoise.up()
        tortoise.goto(0,-60)
        tortoise.fillcolor(position[1])
        tortoise.pencolor("black")
        tortoise.down()
        tortoise.begin_fill()
        tortoise.circle(25)
        tortoise.end_fill()

        tortoise.up()
        tortoise.goto(-110,-60)
        tortoise.fillcolor(position[0])
        tortoise.pencolor("black")
        tortoise.down()
        tortoise.begin_fill()
        tortoise.circle(25)
        tortoise.end_fill()

        tortoise.up()
        tortoise.goto(-110,-160)
        tortoise.fillcolor(position[5])
        tortoise.pencolor("black")
        tortoise.down()
        tortoise.begin_fill()
        tortoise.circle(25)
        tortoise.end_fill()

        tortoise.up()
        tortoise.goto(0,-160)
        tortoise.fillcolor(position[4])
        tortoise.pencolor("black")
        tortoise.down()
        tortoise.begin_fill()
        tortoise.circle(25)
        tortoise.end_fill()

        tortoise.up()
        tortoise.goto(110,-160)
        tortoise.fillcolor(position[3])
        tortoise.pencolor("black")
        tortoise.down()
        tortoise.begin_fill()
        tortoise.circle(25)
        tortoise.end_fill()



        #TEAM 2

        tortoise.up()
        tortoise.goto(-110,10)
        tortoise.fillcolor(position[2])
        tortoise.pencolor("black")    #changes color to match the players in the same position's color on the other team
        tortoise.down()
        tortoise.begin_fill()
        tortoise.circle(25)
        tortoise.end_fill()

        tortoise.up()
        tortoise.goto(0,10)
        tortoise.fillcolor(position[1])
        tortoise.pencolor("black")
        tortoise.down()
        tortoise.begin_fill()
        tortoise.circle(25)
        tortoise.end_fill()

        tortoise.up()
        tortoise.goto(110,10)
        tortoise.fillcolor(position[0])
        tortoise.pencolor("black")
        tortoise.down()
        tortoise.begin_fill()
        tortoise.circle(25)
        tortoise.end_fill()

        tortoise.up()
        tortoise.goto(110,130)
        tortoise.fillcolor(position[5])
        tortoise.pencolor("black")
        tortoise.down()
        tortoise.begin_fill()
        tortoise.circle(25)
        tortoise.end_fill()

        tortoise.up()
        tortoise.goto(0,130)
        tortoise.fillcolor(position[4])
        tortoise.pencolor("black")
        tortoise.down()
        tortoise.begin_fill()
        tortoise.circle(25)
        tortoise.end_fill()

        tortoise.up()
        tortoise.goto(-110,130)
        tortoise.fillcolor(position[3])
        tortoise.pencolor("black")
        tortoise.down()
        tortoise.begin_fill()
        tortoise.circle(25)
        tortoise.end_fill()


def main():
    #creates turtle object and screen 
    george = turtle.Turtle() 
    screen = george.getscreen()
    george.hideturtle()
    court(george,6) #calls court function to initiate volleyball rotation simulation
    
    
    screen.update()
    screen.exitonclick()
   
main()





