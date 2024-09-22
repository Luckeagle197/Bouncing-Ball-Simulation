import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Bouncing Ball Simulation")
screen.bgcolor("white")
screen.setup(width=600, height=600)

# Create the ball object
ball = turtle.Turtle()
ball.shape("circle")
ball.color("blue")
ball.penup()  # Ensure the ball does not draw on the screen

# Set the initial position and velocity
y_pos = 0  # Initial y position
y_velocity = 0  # Initial velocity
gravity = -0.5  # Gravity acceleration (negative to move the ball downwards)
ground_level = -250  # The y position of the ground

# Main loop
def bounce():
    global y_pos, y_velocity
    try:
        while True:
            # Update velocity and position
            y_velocity += gravity  # Simulate gravity
            y_pos += y_velocity  # Update ball position

            # Bounce the ball when it hits the ground
            if y_pos <= ground_level:
                y_pos = ground_level
                y_velocity = -y_velocity * 0.8  # Reverse velocity with some energy loss

            # Update the ball's position on screen
            ball.sety(y_pos)

            # Pause for a short moment to slow down the animation
            time.sleep(0.02)

    except turtle.Terminator:
        print("Turtle window closed.")

# Call bounce function inside turtle's timer
screen.ontimer(bounce, 1)

# Keep the window open until user clicks
screen.exitonclick()
