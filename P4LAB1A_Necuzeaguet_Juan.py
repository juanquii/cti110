# P4LAB1A
# Juan Necuzeaguet
# 07/02/2025
# This program uses the turtle module to draw a square and a triangle.

import turtle

# --- Screen Setup ---
wn = turtle.Screen()
wn.title("P4LAB1a - Shapes (Square and Triangle)")
wn.setup(width=600, height=600)

# --- Turtle Initialization ---
t = turtle.Turtle()
t.speed(1) # Set drawing speed

# --- Drawing the Square ---
t.penup()          # Lift the pen to move without drawing
t.goto(-100, 50)   # Move to start location for the square
t.pendown()        # Drop the pen down to start drawing
t.pencolor("blue") # Set pen color to blue
t.pensize(3)       # Set pen size

for _ in range(4): # Loop 4 times for the 4 sides of a square
    t.forward(100) # Go forwardd
    t.left(90)     # Turn left 90 degrees

# --- Drawing the Triangle ---
t.penup()          
t.goto(50, -50)    
t.pendown()        
t.pencolor("red")  
t.pensize(3)       

for _ in range(3): 
    t.forward(100) 
    t.left(120)    

# --- Keep Window Open ---
turtle.exitonclick() # Keep the window open until clicked
