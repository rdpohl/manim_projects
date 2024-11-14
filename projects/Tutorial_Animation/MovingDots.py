from manim import *
import numpy as np

class MovingDots(Scene):
    def construct(self):
        
        d1, d2 = Dot(color=BLUE), Dot(color=GREEN)

        #group dots
        dg = VGroup(d1, d2).arrange(RIGHT, buff=1)
        
        #draw line from dot centers
        l1 = Line(d1.get_center(),d2.get_center()).set_color(RED)

        x = ValueTracker(0)
        y = ValueTracker(0)
        
        d1.add_updater(lambda z: z.set_x(x.get_value()))    #moves blue dot
        d2.add_updater(lambda z: z.set_y(y.get_value()))    #move green dot
        
        #line updater center to center on dots
        #line moves doesn't have to part of the dots group:
        #it appears to move because it is always redrawn on animation
        l1.add_updater(lambda z: z.become(Line(d1.get_center(), d2.get_center())))
        
        self.add(d1, d2,l1)
        self.play(x.animate.set_value(5))   #set value to move 5 relative steps on x-axis
        self.play(y.animate.set_value(-3))   #set value to move 4 relative steps on y-axis
        self.wait()
        