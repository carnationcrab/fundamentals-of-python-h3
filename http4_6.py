# SAM MARTORANA

# ################################# [H3_4] ################################# #
# Do Exercise 6 at the end of Chapter 4 in your HTT online book.  Your
# program should prompt and read the int number of sides, the int length of
# each side, the str (line) color for each side with all sides having this
# same color, and the str color with which to fill the polygon.  Hint: you
# can draw a polygon with n sides by repeating the following n times: move
# forward the length of a side, then turn left 360/n. Study the chapter
# examples to see how to set the color of each side, as well as how to fill
# your polygon with a given color. You can find all legal colors for setting
# on the Turtle Colors link next to this handout on Canvas, as well as here:
# https://www.tcl.tk/man/tcl8.5/TkCmd/colors.htm
# ########################################################################## #

# arrange
import turtle

wn = turtle.Screen()

dave = turtle.Turtle()

numSides = int(input('How many sides? '))
sideLen = int(input('How long is each side? '))
sideColor = input('What color are the lines of the shape? ')
fillColor = input('What color is your shape? ')


# act
def drawShape(sides, length, color, fill):
    dave.color(color)
    dave.fillcolor(fill)
    dave.pendown()

    rotation = 360 / sides
    dave.begin_fill()

    for i in range(sides):
        dave.forward(length)
        dave.left(rotation)

    dave.end_fill()


drawShape(numSides, sideLen, sideColor, fillColor)

wn.exitonclick()
