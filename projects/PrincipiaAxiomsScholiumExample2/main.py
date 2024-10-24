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
        self.play(
            Write(E_Text)
        )
