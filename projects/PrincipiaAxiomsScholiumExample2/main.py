'''
Richard Pohl, October, 2024
From Newton's Principia, Axioms,
     Axioms, Scholium, Example 2
'''

import math as m
import numpy as np
from scipy.integrate import odeint
from manim import *

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

class TwoSwingingBalls(Scene):
    '''
        document here
    '''
    def construct(self):

        # Parameters
        g = 9.81  # m/s^2
        L = 1.0  # m
        b = 0.1  # Damping coefficient (adjust based on air resistance)
        theta0 = np.pi / 2  # Initial angle (radians)
        omega0 = 0  # Initial angular velocity (radians/s)
        t_max = 1 # Total simulation time (seconds)
        dt = 0.1  # Time step

        #Time array
        t = np.arange(0, t_max, dt)

        # Initial conditions
        state0 = [theta0, omega0]

        # Solve the differential equations
        solution = odeint(pendulum_equation, state0, t, args=(g, L, b))
        index_tracker = ValueTracker(0)

        ax = Axes(
            x_range=[-1,10,1],
            y_range=[-1,10,1],
            axis_config={"include_numbers": True,},
            x_length=10.89,
            y_length=6.5,
        )
        ax.set_color(BLACK)
        labels = ax.get_axis_labels(x_label="X",
                                    y_label="Y")
        labels.set_color(BLACK)
        self.add(ax, labels)

        #set in the dots
        dot_E  = Dot(ax.coords_to_point(1,7), color=BLACK)
        dot_G  = Dot(ax.coords_to_point(2,7), color=BLACK)
        dot_F  = Dot(ax.coords_to_point(7,7), color=BLACK)
        dot_H  = Dot(ax.coords_to_point(8,7), color=BLACK)
        dot_C  = Dot(ax.coords_to_point(4,7), color=BLACK)
        dot_D  = Dot(ax.coords_to_point(5,7), color=BLACK)
        dots_group = VGroup(dot_E,dot_G, dot_F,dot_H, dot_C, dot_D)
        self.add(dots_group)

        #add the labels for the dots
        E_Text    = Text('E').scale(0.5).next_to(dot_E, UP*0.3)
        E_Text.set_color(BLACK)
        #self.play(Write(E_Text))
        G_Text    = Text('G').scale(0.5).next_to(dot_G, UP*0.3)
        G_Text.set_color(BLACK)
        #self.play(Write(G_Text))
        C_Text    = Text('C').scale(0.5).next_to(dot_C, UP*0.3)
        C_Text.set_color(BLACK)
        #self.play(Write(C_Text))
        D_Text    = Text('D').scale(0.5).next_to(dot_D, UP*0.45)
        D_Text.set_color(BLACK)
        #self.play(Write(D_Text))
        F_Text    = Text('F').scale(0.5).next_to(dot_F, UP*0.3)
        F_Text.set_color(BLACK)
        #self.play(Write(F_Text))
        H_Text   = Text('H').scale(0.5).next_to(dot_H, UP*0.3)
        H_Text.set_color(BLACK)
        #self.play( Write(H_Text))
        text_group = VGroup(E_Text, G_Text, C_Text, D_Text, F_Text, H_Text)
        self.play( Write(text_group))

        #set in the line connecting the dots
        line_EH  = Line()
        line_EH.put_start_and_end_on(dot_E.get_center(),
                                     dot_H.get_center())
        line_EH.set_color(BLACK)
        self.play(Write(line_EH))

        radius = 3
        start_angle = 0
        arc_angle = PI * -1

        #draw the weight labeled A
        A_Color = PURE_BLUE
        dot_A   = Dot(ax.coords_to_point(4,2), radius=0.3, color=A_Color)
        dot_A_Text = Text('A').scale(0.5).next_to(dot_A, DOWN*0.3)
        dot_A_Text.set_color(A_Color)

        #draw line from C to A
        line_CA = Line()
        line_CA.put_start_and_end_on(dot_C.get_center(),
                                     dot_A.get_top())
        line_CA.set_color(A_Color)
        self.play(Write(line_CA))

        self.add(dot_A)
        self.play(Write(dot_A_Text))

        # #draw the template for arc ECF
        arc_EAF = Arc(radius=radius,
                      start_angle=start_angle,
                      angle=arc_angle,
                      arc_center=dot_C.get_center())
        arc_EAF.set_color(A_Color)
        self.play(Create(arc_EAF))

        #create line CA Ball group
        CA_Group = VGroup(dot_C, line_CA, dot_A, dot_A_Text)
        self.add(CA_Group)

        #run ball back to x-axis
        for x in solution:
            self.play(Rotating(CA_Group, radians=x[0], about_point=dot_C.get_center(), run_time=1))
        
        B_Color = ORANGE
        #draw the weight labeled B
        dot_B   = Dot(ax.coords_to_point(5,2), radius=0.2, color=B_Color)
        dot_B_Text = Text('B').scale(0.5).next_to(dot_B, DOWN*0.3)
        dot_B_Text.set_color(B_Color)
        self.add(dot_B)
        self.play(Write(dot_B_Text))

        #draw the line from D to B
        line_DB = Line()
        line_DB.put_start_and_end_on(dot_D.get_center(),
                                     dot_B.get_center())
        line_DB.set_color(B_Color)
        self.play(Write(line_DB))

        #draw the template for arc GBH
        arc_GBH = Arc(radius=radius, start_angle=start_angle, angle=arc_angle, arc_center=dot_D.get_center())
        arc_GBH.set_color(B_Color)
        self.play(Create(arc_GBH))

        self.wait(2)
