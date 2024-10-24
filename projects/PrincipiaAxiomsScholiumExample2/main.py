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

        E_Text = Text('E').scale(0.75)
        E_Text.set_color(BLACK)
        self.play(
            Write(E_Text)
        )
        self.play(E_Text.animate.shift(LEFT*4))
        self.play(E_Text.animate.shift(UP*2))

        G_Text = Text('G').scale(0.75)
        G_Text.set_color(BLACK)
        self.play(
            Write(G_Text)
        )
        self.play(G_Text.animate.shift(LEFT*3))
        self.play(G_Text.animate.shift(UP*2))

        F_Text = Text('F').scale(0.75)
        F_Text.set_color(BLACK)
        self.play(
            Write(F_Text)
        )
        self.play(F_Text.animate.shift(RIGHT*3))
        self.play(F_Text.animate.shift(UP*2))

        H_Text = Text('H').scale(0.75)
        H_Text.set_color(BLACK)
        self.play(
            Write(H_Text)
        )
        self.play(H_Text.animate.shift(RIGHT*4))
        self.play(H_Text.animate.shift(UP*2))

        '''C_Text = Text('C').scale(0.75)
        C_Text.set_color(BLACK)
        self.play(
            Write(C_Text)
        )
        self.play(C_Text.animate.shift(LEFT))
        
        D_Text = Text('D').scale(0.75)
        D_Text.set_color(BLACK)
        self.play(
            Write(D_Text)
        )
        self.play(D_Text.animate.shift(RIGHT*0.5))
        '''

        self.wait(2)
