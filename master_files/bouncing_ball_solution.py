# Fully working text-based bouncing ball simulation.

import time

# Set the initial position and velocity
y_pos = 200  # Initial y position (starts above ground)
y_velocity = 0  # Initial velocity (stationary)
gravity = -0.5  # Gravity (negative to simulate downward motion)
ground_level = 0  # Ground level (below the starting point)

# Main loop to simulate the bouncing ball
while True:
    # Update velocity and position
    y_velocity += gravity  # Simulate gravity (pull down)
    y_pos += y_velocity  # Update the ball's position

    # Bounce the ball when it hits the ground
    if y_pos <= ground_level:
        y_pos = ground_level  # Stop at ground level
        y_velocity = -y_velocity * 0.8  # Reverse velocity with energy loss (bounce)

    # Print the ball's current position (for testing purposes)
    print(f"Ball position: {y_pos}")

    # Pause for a short moment to slow down the simulation
    time.sleep(0.02)
