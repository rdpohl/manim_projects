'''
Richard Pohl, October, 2024
From Newton's Principia, Axioms,
     Axioms, Scholium, Example 2
'''

from manim import *

class TwoSwingingBalls(Scene):
    '''
        document here
    '''
    def construct(self):

        ax = Axes(
            x_range=[-1,10,1],
            y_range=[-1,10,1],
            axis_config={"include_numbers": True,}
        )
        ax.set_color(BLACK)
        labels = ax.get_axis_labels(x_label="X",
                                    y_label="Y")
        labels.set_color(BLACK)
        self.add(ax, labels)

        dot_E  = Dot(ax.coords_to_point(1,7), color=BLACK)
        dot_G  = Dot(ax.coords_to_point(2,7), color=BLACK)
        dot_F  = Dot(ax.coords_to_point(7,7), color=BLACK)
        dot_H  = Dot(ax.coords_to_point(8,7), color=BLACK)
        dot_C  = Dot(ax.coords_to_point(4,7), color=BLACK)
        dot_D  = Dot(ax.coords_to_point(5,7), color=BLACK)
        dots_group = VGroup(dot_E,dot_G, dot_F,dot_H, dot_C, dot_D)
        self.add(dots_group)

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

        line_EH  = Line()
        line_EH.put_start_and_end_on(dot_E.get_center(),
                                     dot_H.get_center())
        line_EH.set_color(BLACK)
        self.play(Write(line_EH))

        dot_A   = Dot(ax.coords_to_point(4,2), radius=0.4, color=BLACK)
        dot_A_Text = Text('A').scale(0.5).next_to(dot_A, DOWN*0.3)
        dot_A_Text.set_color(RED)
        self.add(dot_A)
        self.play(Write(dot_A_Text))

        line_CA = Line()
        line_CA.put_start_and_end_on(dot_C.get_center(),
                                     dot_A.get_center())
        line_CA.set_color(BLACK)
        self.play(Write(line_CA))

        dot_B   = Dot(ax.coords_to_point(5,2), radius=0.2, color=BLACK)
        dot_B_Text = Text('B').scale(0.5).next_to(dot_B, DOWN*0.3)
        dot_B_Text.set_color(BLACK)
        self.add(dot_B)
        self.play(Write(dot_B_Text))

        line_DB = Line()
        line_DB.put_start_and_end_on(dot_D.get_center(),
                                     dot_B.get_center())
        line_DB.set_color(BLACK)
        self.play(Write(line_DB))

        circle_C = Circle(radius=1, color=BLACK)
        #circle_C.move_to([4, 7, 0])
        self.add(circle_C)

        self.wait(2)
