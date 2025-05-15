'''
gemini code
'''

import math as m
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def pendulum_equation(state, t, g, L, b):
    """
    Defines the differential equations for a damped pendulum.
    
    Args:
        state: A list containing the current angle (theta) and angular velocity (omega).
        t: Time.
        g: Acceleration due to gravity.
        L: Length of the pendulum.
        b: Damping coefficient (air resistance).
    
    Returns:
        A list containing the derivatives of theta and omega.
    """
    theta, omega = state
    dtheta_dt = omega
    domega_dt = -(g / L) * np.sin(theta) - (b / L) * omega
    return [dtheta_dt, domega_dt]

# Parameters
g = 9.81  # m/s^2
L = 1.0  # m
b = 0.1  # Damping coefficient (adjust based on air resistance)
theta0 = np.pi / 2  # Initial angle (radians)
omega0 = 0  # Initial angular velocity (radians/s)
t_max = 1 # Total simulation time (seconds)
dt = 0.01  # Time step

# Time array
t = np.arange(0, t_max, dt)

# Initial conditions
state0 = [theta0, omega0]

# Solve the differential equations
solution = odeint(pendulum_equation, state0, t, args=(g, L, b))

#print(f"shape {solution.shape[0]} \n")
mdegrees = 0
mdegrees_hold = 0

for x in solution:
    mdegrees = m.degrees(x[0])
    write_data_str = f"{x[0]:>8.4f} {mdegrees:>8.4f} {x[1]:>8.4f}"
    print(f"{write_data_str}")
    #fileout.write(f"{write_data_str} \n")

theta = solution[:, 0]

#fileout.close()

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(t, theta)
plt.xlabel("Time (s)")
plt.ylabel("Angle (radians)")
plt.title("Damped Pendulum Swing")
plt.show()
