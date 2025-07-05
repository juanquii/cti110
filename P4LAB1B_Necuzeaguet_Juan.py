# P4LAB1B
# Juan Necuzeaguet
# 07/02/2025
# This program will use the turtle module to draw the initials 'J' and 'N'.

import turtle

# --- Screen Setup ---

wn = turtle.Screen()
wn.title("P4LAB1b - Initials (J and N)")
wn.setup(width=600, height=600)

# --- Turtle Initialization ---

t = turtle.Turtle()
t.speed(3)       
t.pencolor("purple") 
t.pensize(5)     

# --- Drawing the 'J' ---

t.penup()
t.goto(-150, 100) # Start position for 'J'
t.pendown()
t.right(90)      
t.forward(150)   
t.circle(-40, 180) 

t.penup()
t.goto(-100, 100) 
t.pendown()
t.left(90)       
t.forward(100)   


# --- Moving to the 'N' ---

t.penup()
t.goto(50, 100) # Start position for 'N' (top-left of N)
t.pendown()

# --- Drawing the 'N' 

t.setheading(270) 
t.forward(150)    

t.penup()         
t.goto(50, 100)   
t.pendown()       

t.setheading(303.69) 
t.forward(180.28) 

t.penup()         
t.goto(150, 100)  
t.pendown()       

t.setheading(270) 
t.forward(150)    

turtle.exitonclick()
