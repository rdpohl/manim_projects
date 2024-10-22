from manim import *
import math as m
import numpy as np

class ParalellogramProjectile(Scene):
    def construct(self):
        ax = Axes(
            x_range     = [-2, 10, 1],
            y_range     = [-2, 10, 1],
            axis_config = {"include_numbers": True,}
        )
        ax.set_color(BLACK)
        labels = ax.get_axis_labels(x_label="Distance", y_label="Gravity")
        labels.set_color(BLACK)
        self.add(ax, labels)

        t = ValueTracker(0)

        def func(x):
            #a ball tossed from a height
            v0 = 1 #m/s
            theta = 1 #in degrees
            gravity = 9.81
            height = 5 #meters

            #time of flight
            t_flight = np.sqrt(2 * height / gravity)

            #time array
            #t = np.linspace(0, t_flight, 100)

            #xpos = v0 * np.cos(np.deg2rad(theta)) * x
            #ypos = height + v0 * np.sin(np.deg2rad(theta)) * xpos - 0.5 * gravity * t**2

            return (v0 * np.cos(np.deg2rad(theta)) * x)
        
        def funcTry(x):
            return (x + 1)
        graph = ax.plot(funcTry, color=MAROON)

        initial_point = [ax.coords_to_point(t.get_value(), funcTry(t.get_value()))]

        x_space = np.linspace(*ax.x_range[:2],200)
        minimum_index = funcTry(x_space).argmin()

        self.add(graph)

        dot_A   = Dot(ax.coords_to_point(1,5), color=BLACK)
        dot_C   = Dot(ax.coords_to_point(1,0), color=BLACK)
        line_CA = Line()
        line_CA.put_start_and_end_on(dot_A.get_center(), dot_C.get_center())
        line_CA.set_color(BLACK)

        dot_B = Dot(ax.coords_to_point(5,6), color=BLACK)
        line_AB = Line()
        line_AB.put_start_and_end_on(dot_A.get_center(), dot_B.get_center())
        line_AB.set_color(BLACK)

        dot_D = Dot(ax.coords_to_point(5,1), color=BLACK)
        line_BD = Line()
        line_BD.put_start_and_end_on(dot_B.get_center(), dot_D.get_center())
        line_BD.set_color(BLACK)

        line_DC = Line()
        line_DC.put_start_and_end_on(dot_D.get_center(), dot_C.get_center())
        line_DC.set_color(BLACK)

        self.add(dot_C, dot_A, dot_B, dot_D)
        self.add(line_CA, line_AB, line_BD, line_DC)

        dot_A_Text = Text('A').next_to(dot_A, UP*0.3).scale(0.75)
        dot_A_Text.set_color(BLACK)
        dot_B_Text = Text('B').next_to(dot_B, UP*0.3).scale(0.75)
        dot_B_Text.set_color(BLACK)
        dot_C_Text = Text('C').next_to(dot_C, RIGHT*0.3).shift(UP*0.4).scale(0.75)
        dot_C_Text.set_color(BLACK)
        dot_D_Text = Text('D').next_to(dot_D, RIGHT*0.25).scale(0.75)
        dot_D_Text.set_color(BLACK)
        self.add(dot_A_Text, dot_B_Text, dot_C_Text, dot_D_Text)

        self.play(t.animate.set_value(x_space[minimum_index]), run_time=1)
        self.wait()