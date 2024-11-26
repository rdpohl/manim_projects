'''
Manim tutorial example but doesn't run as it
'''

import numpy as np
from manim import *

class SineCurveUnitCircle(Scene):
    def construct(self):
        #x_start = np.array([-6,0,0])
        #x_end = np.array([6,0,0])

        #y_start = np.array([-4,-2,0])
        #y_end = np.array([-4,2,0])

        #x_axis = Line(x_start, x_end)
        #y_axis = Line(y_start, y_end)

        #self.add(x_axis, y_axis)
        
        #self.add_x_labels()    #only gets error
        #x_labels = [
        #    MathTex("\\pi"),   #changed fromm \pi to \\pi
        #    MathTex("2\\pi"),
        #    MathTex("3\\pi"), 
        #    MathTex("4\\pi"),
        #]

        #for i in range(len(x_labels)):
        #    x_labels[i].next_to(np.array([-1 + 2*i, 0, 0]), DOWN)
        #    self.add(x_labels[i])

        self.origin_point = np.array([-4,0,0])
        self.curve_start = np.array([-3,0,0])

        circle = Circle(radius=1)
        circle.move_to(self.origin_point)
        self.add(circle)
        self.circle = circle

        orbit = self.circle
        origin_point = self.origin_point

        dot = Dot(radius=0.08, color=YELLOW)
        dot_sine = Dot(radius=0.08, color=RED)
        dot.move_to(orbit.point_from_proportion(0))
        dot_sine.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25
    
        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return Line(origin_point, dot.get_center(), color=BLUE)

        #def dot_on_sine(mob, dt):
        #    self.t_offset += (dt * rate)
        #    mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_curve():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )

        self.curve = VGroup()
        self.curve.add(Line(self.curve_start,
                            self.curve_start))
        
        def get_curve():
            last_line = self.curve[-1]
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
            self.curve.add(new_line)
            return self.curve

        dot.add_updater(go_around_circle)
        #dot_sine.add_updater(dot_on_sine)

        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line = always_redraw(get_line_to_curve)
        sine_curve_line = always_redraw(get_curve)

        self.add(dot) #), dot_sine)
        self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line)
        self.wait(8.5)

        dot.remove_updater(go_around_circle)
        #dot_sine.remove_updater(dot_on_sine)
    