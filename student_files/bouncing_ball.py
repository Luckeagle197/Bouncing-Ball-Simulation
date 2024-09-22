# student_files/bouncing_ball.py
# Instructions: Complete the code to create a simple bouncing ball simulation.

import time

# Step 1: Define initial position and velocity
y_pos =  # Initial y position of the ball
y_velocity =  # Initial velocity
gravity = 0.5  # Gravity acceleration
ground_level = -250  # The y position of the ground

# Step 2: Main loop to simulate the bouncing ball
while True:
    # Update the velocity and position
    y_velocity +=  # Add gravity to the velocity
    y_pos +=  # Update the y position of the ball

    # Step 3: Bounce the ball when it hits the ground
    if y_pos <= ground_level:
        y_pos = ground_level
        y_velocity =  # Reverse the velocity to simulate a bounce

    # Print the ball's current position (for testing purposes)
    print(f"Ball position: {y_pos}")

    # Pause for a short moment to slow down the simulation
    time.sleep(0.02)
