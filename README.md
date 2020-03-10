## Problem Set 3: HTT3 & HTT5

No starting code for this homework assignment.

At the start of each of these problems, the name of a Python file is given in blue: foo.py.  You should create and save the requested Python program source code in a file with the same name.  Also add a comment at the top of each file giving your name.

When finished, upload each .py file with the specified name to the Canvas H3 Assignment link.  Do each of the following. Create an empty folder then open as a new PyCharm project.  Within the project, create each of the following files as described below. For the turtle graphics problem, be sure to have wn.exitonclick() as the last statement of your script.

### H3-1 (rand100.py) 
Write a program that prints out 100 random integers, each in the range 1 through 6.  
### H3-2 (randavg.py) 
Write a program that reads an int numRolls from the user, then generates numRolls random integers, each in the range 1 through 6. This simulates rolling a single fair (unbiased) die. 

Use a for-loop and the accumulator pattern to add together the values of these rolls in the integer variable sum, then compute the average roll value (sum / numRolls).  Print out this average.  What do you expect for this average, as numRolls gets larger and larger? 
### H3-3 (calcpi2.py) 
Here's another way of approximating Pi, using the Madhava-Leibniz formula:  

```Pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...```

Notice how the signs alternate between + and - for each term of this series (1, -1/3, 1/5, -1/7, etc.). Write a program which reads num_terms as an int, then computes the above approximation of Pi/4 by summing the first num_terms terms of this series.  Then multiply your computed sum by 4 and print out the resulting approximate calculated value of Pi as well the error: the absolute value of its difference with math.pi.  Hint: use a loop with header for count in range(num_terms), after you initialize a float accumulator pi_estimate to 0.0 and sign to 1.0.  Your indented loop body should first calculate ```term = sign / (2*count + 1)```, then add term to your pi_estimate accumulator.  The final statement within your loop body should be sign = -sign so that the term calculated in the next iteration of the for-loop will have the opposite sign. After the loop ends, calculate and print ```4*pi_estimate``` and its absolute value difference from math.pi:  ```abs(math.pi-4*pi_estimate)```.

### H3-4 (http4_6.py) 
Do Exercise 6 at the end of Chapter 4 in your HTT online book.  Your program should prompt and read the int number of sides, the int length of each side, the str (line) color for each side with all sides having this same color, and the str color with which to fill the polygon.  Hint: you can draw a polygon with n sides by repeating the following n times: move forward the length of a side, then turn left 360/n. Study the chapter examples to see how to set the color of each side, as well as how to fill your polygon with a given color. You can find all legal colors for setting on the Turtle Colors link next to this handout on Canvas, as well as here: https://www.tcl.tk/man/tcl8.5/TkCmd/colors.htm

### H3-5 (trace_me.py) 
The Python program trace_me.py is posted next to this handout within the H3 Assignment on Canvas. Download it and add to your project for this assignment. Set breakpoints on the two print("set...") statements in this program.  Finally, run your program in the PyCharm debugger and enter 5 for the first input, then the values 3.0, 3.1, 3.14, 3.13, 3.141 for the five subsequent inputs.  

When your program stops at each breakpoint, write down the values of a, b, and val.  Then resume until the next breakpoint is encountered.  Finally, add comments (lines starting with #) at the end of the program which lists the five sets of values for breakpoint at LOCATION 1 that you wrote down, followed by the values for the final breakpoint at LOCATION 2.  Your program should thus end with a comment that lists six total sets of the values for a, b, and val.  Submit your code with these comments as your delivery for this problem.
