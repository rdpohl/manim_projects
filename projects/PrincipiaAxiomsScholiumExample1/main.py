'''
Richard D Pohl, October, 2024
'''
from manim import *
import numpy as np

class ParalellogramProjectile(Scene):
    '''
        document here
    '''
    def construct(self):
        ax = Axes(
            x_range     = [-2, 10, 1],
            y_range     = [-2, 10, 1],
            axis_config = {"include_numbers": True,}
        )
        ax.set_color(BLACK)
        labels = ax.get_axis_labels(x_label="Distance", y_label="Gravity")
        labels.set_color(BLACK)
        self.next_section()
        self.add(ax, labels)

        dot_A      = Dot(ax.coords_to_point(1,5), color=BLACK)
        dot_C      = Dot(ax.coords_to_point(1,0), color=BLACK)
        dot_A_Text = Text('A').next_to(dot_A, UP*0.3).scale(0.75)
        dot_A_Text.set_color(BLACK)
        dot_C_Text = Text('C').next_to(dot_C, RIGHT*0.3).shift(UP*0.4).scale(0.75)
        dot_C_Text.set_color(BLACK)
        dot_C      = Dot(ax.coords_to_point(1,0), color=BLACK)
        line_CA    = Line()
        line_CA.put_start_and_end_on(dot_C.get_center(), dot_A.get_center())
        line_CA.set_color(BLACK)
        self.add(dot_A, dot_A_Text, dot_C, dot_C_Text)
        self.play(Write(dot_A_Text))
        self.play(Write(dot_C_Text))
        self.play(Write(line_CA))

        dot_B = Dot(ax.coords_to_point(5,6), color=BLACK)
        dot_B_Text = Text('B').next_to(dot_B, UP*0.3).scale(0.75)
        dot_B_Text.set_color(BLACK)
        line_AB = Line()
        line_AB.put_start_and_end_on(dot_A.get_center(), dot_B.get_center())
        line_AB.set_color(BLACK)
        self.add(dot_B, dot_B_Text)
        self.play(Write(dot_C_Text))
        self.play(Write(line_AB))

        dot_D = Dot(ax.coords_to_point(5,1), color=BLACK)
        dot_D_Text = Text('D').next_to(dot_D, RIGHT*0.25).scale(0.75)
        dot_D_Text.set_color(BLACK)
        line_BD = Line()
        line_BD.put_start_and_end_on(dot_B.get_center(), dot_D.get_center())
        line_BD.set_color(BLACK)
        self.add(dot_D, dot_D_Text)
        self.play(Write(dot_D_Text))
        self.play(Write(line_BD))

        line_DC = Line()
        line_DC.put_start_and_end_on(dot_D.get_center(), dot_C.get_center())
        line_DC.set_color(BLACK)
        self.play(Write(line_DC))

        t = ValueTracker(0)

        def func(x):
            return x + 1
        graph = ax.plot(func, color=MAROON)
        self.add(graph)

        x_space = np.linspace(*ax.x_range[:2],200)
        minimum_index = func(x_space).argmin()

        #self.play(t.animate.set_value(x_space[minimum_index]), run_time=1)
