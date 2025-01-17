from manim import *

class ContinuousMotion(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UL + np.cos(pos[1] / 2) * RIGHT
        stream_lines = StreamLines(func, stroke_width=3, max_anchors_per_line=20)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)