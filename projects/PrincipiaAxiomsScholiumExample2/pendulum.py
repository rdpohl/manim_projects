#!/usr/bin/env python
'''
Pendulum Program
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint

# Pendulum parameters
g = 9.81  # Acceleration due to gravity (m/s^2)
L = 1.0  # Length of the pendulum (m)
theta_0 = np.radians(30)  # Initial angle (radians)
omega_0 = 0.0  # Initial angular velocity (rad/s)
t_max = 10.0  # Total time (s)
dt = 0.01  # Time step (s)

# Function to calculate the derivatives of theta and omega
def derivatives(state, t):
    '''
    def
    '''
    theta, omega = state
    return [omega, -g/L * np.sin(theta)]

# Create an array of time values
t = np.arange(0, t_max, dt)

# Solve the differential equations using odeint
sol = odeint(derivatives, [theta_0, omega_0], t)

# Extract theta values from the solution
theta = sol[:, 0]

# Create a figure and axes
fig, ax = plt.subplots()

# Set up the plot
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 0.2)
ax.set_aspect('equal')
ax.set_title('Pendulum Motion')

# Initialize the line for the pendulum
line, = ax.plot([], [], 'o-', lw=2)

# Animation function
def animate(i):
    '''
    def
    '''
    x = L * np.sin(theta[i])
    y = -L * np.cos(theta[i])
    line.set_data([0, x], [0, y])
    return line,

# Create the animation
ani = FuncAnimation(fig, animate, frames=len(t), interval=dt*1000, blit=True)

# Show the animation
plt.show()
