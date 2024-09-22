# student_files/bouncing_ball_visual.py
# Instructions: Complete the code below to visualize the bouncing ball using the turtle library.

import turtle
import time

# Step 1: Set up the screen
screen = turtle.Screen()
screen.title("Bouncing Ball Simulation")
screen.bgcolor("white")
screen.setup(width=600, height=600)

# Step 2: Create the ball object
ball = turtle.Turtle()
ball.shape("circle")
ball.color("blue")
ball.penup()  # Ensure the ball does not draw on the screen

# Step 3: Define initial position and velocity
y_pos =  # Initial y position of the ball
y_velocity =  # Initial velocity
gravity =  # Gravity acceleration
ground_level = -250  # The y position of the ground

# Main loop to simulate the bouncing ball
while True:
    # Update velocity and position
    y_velocity +=  # Simulate gravity
    y_pos +=  # Update ball position

    # Bounce the ball when it hits the ground
    if y_pos <= ground_level:
        y_pos = ground_level
        y_velocity =  # Reverse velocity with some energy loss

    # Update the ball's position on screen
    ball.sety(y_pos)

    # Pause for a short moment to slow down the animation
    time.sleep(0.02)

# Keep the window open until the user clicks
screen.exitonclick()
