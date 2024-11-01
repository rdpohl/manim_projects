'''
example
'''

import numpy as np
from math import *
import matplotlib.pyplot as plt

def simplePendulumSimulation(theta0, omega0, tau, m, g, l, numSteps, plotFlag):
	'''
	def
	'''
	# This function simulates a simple pendulum using the Euler-Cromer method.
	# Inputs: theta0 (the initial angle, in rad)
	#		  omega0 (the initial angular velocity, in rad/s)
	#		  tau (the time step)
	#		  m (mass of the pendulum)
	#	      g (gravitational constant)
	#		  l (length of the pendulum)
	#		  numSteps (number of time steps to take, in s)
	#	      plotFlag (set to 1 if you want plots, 0 otherwise)
	# Outputs: t_vec (the time vector)
	#		   theta_vec (the angle vector)

	# initialize vectors

	time_vec = [0]*numSteps
	theta_vec = [0]*numSteps
	omega_vec = [0]*numSteps
	KE_vec = [0]*numSteps
	PE_vec = [0]*numSteps

	# set initial conditions

	theta = theta0
	omega = omega0
	#time = 0

	# begin time stepping

	for i in range(0,numSteps):

		omega_old = omega
		theta_old = theta
		# update the values
		omega = omega_old - (g/l)*sin(theta_old)*tau
		theta = theta_old + omega*tau
		# record the values
		time_vec[i] = tau*i
		theta_vec[i] = theta
		omega_vec[i] = omega
		KE_vec[i] = (1/2)*m*l**2*omega**2
		PE_vec[i] = m*g*l*(1-cos(theta))

	TE_vec = np.add(KE_vec,PE_vec)

	# make graphs

	if plotFlag == 1:

		plt.figure(0)
		plt.plot(time_vec,theta_vec)
		plt.xlabel('Time (s)')
		plt.ylabel('Displacement (rad)')
		#plt.savefig('plot1.png', bbox_inches='tight')

		plt.figure(1)
		plt.plot(time_vec,KE_vec,label='Kinetic Energy')
		plt.plot(time_vec,PE_vec,label='Potential Energy')
		plt.plot(time_vec,TE_vec,label='Total Energy')
		plt.legend(loc='upper left')
		plt.xlabel('Time (s)')
		plt.ylabel('Energy (J)')
		#plt.savefig('plot2.png', bbox_inches='tight')

		plt.figure(2)
		plt.plot(theta_vec,omega_vec)
		plt.xlabel('Displacement (rad)')
		plt.ylabel('Velocity (rad/s)')
		#plt.savefig('plot3.png', bbox_inches='tight')

		plt.show()

	# return the vectors

simplePendulumSimulation(4.71,  #theta0 (the initial angle, in rad)
						 1,     #omega0 (the initial angular velocity, in rad/s)
						 1,     #tau (the time step)
						 10,   #m (mass of the pendulum)
						 9.81,  #g (gravitational constant)
						 3,     #l (length of the pendulum)
						 3000,  #numSteps (number of time steps to take, in s)
						 1      #plotFlag (set to 1 if you want plots, 0 otherwise)
						 )

