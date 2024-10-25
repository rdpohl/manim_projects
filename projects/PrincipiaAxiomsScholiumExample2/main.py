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

        dot_E  = Dot(ax.coords_to_point(1,7),   color=RED)
        dot_G  = Dot(ax.coords_to_point(2,6.7), color=BLUE)
        dot_F  = Dot(ax.coords_to_point(7,7),   color=RED)
        dot_H  = Dot(ax.coords_to_point(8,6.7), color=BLUE)

        self.add(dot_E,dot_G, dot_F,dot_H)

        E_Text    = Text('E').scale(0.5).next_to(dot_E, LEFT*0.3)
        E_Text.set_color(RED)
        self.play(Write(E_Text))
        F_Text    = Text('F').scale(0.5).next_to(dot_F, RIGHT*0.3)
        F_Text.set_color(RED)
        self.play(Write(F_Text))
        #dots_EF   = VGroup(dot_E, dot_F)

        G_Text = Text('G').scale(0.5).next_to(dot_G, LEFT*0.3)
        G_Text.set_color(BLUE)
        self.play(Write(G_Text))
        H_Text = Text('H').scale(0.5).next_to(dot_H, RIGHT*0.3)
        H_Text.set_color(BLUE)
        self.play( Write(H_Text))
        #dots_GH = VGroup(dot_G, dot_H)

        line_EF    = Line()
        line_EF.put_start_and_end_on(dot_E.get_center(),
                                     dot_F.get_center())
        line_EF.set_color(RED)
        self.play(Write(line_EF))

        line_GH    = Line()
        line_GH.put_start_and_end_on(dot_G.get_center(),
                                     dot_H.get_center())
        line_GH.set_color(BLUE)
        self.play(Write(line_GH))

        dot_C  = Dot(ax.coords_to_point(4,7), color=RED)
        dot_D  = Dot(ax.coords_to_point(5,6.7), color=BLUE)
        self.add(dot_C, dot_D)

        C_Text = Text('C').scale(0.5).next_to(dot_C, UP*0.3)
        C_Text.set_color(RED)
        self.play(Write(C_Text))

        D_Text = Text('D').scale(0.5).next_to(dot_D, UP*0.45)
        D_Text.set_color(BLUE)
        self.play(Write(D_Text))

        dot_A = LabeledDot(Text("A", color=RED))
        #dot_A_Text = Text('A').scale(0.5)
        #dot_A_Text.set_color(RED)
        self.add(dot_A)

        line_CA    = Line()
        line_CA.put_start_and_end_on(dot_C.get_center(),
                                     dot_A.get_center())
        line_CA.set_color(BLUE)
        self.play(Write(line_CA))

        self.wait(2)
