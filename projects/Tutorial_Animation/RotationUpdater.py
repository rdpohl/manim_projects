from manim import *

class RotationUpdater(Scene):
    def construct(self):
        
        def updater_forth(mobj, dt):
            #moves pendulum to the right
            mobj.rotate_about_origin(dt)
        
        def updater_back(mobj, dt):
            #moves pendulum to the left
            mobj.rotate_about_origin(-dt)
        
        line_reference = Line(ORIGIN, LEFT).set_color(WHITE)
        
        line_moving = Line(ORIGIN, LEFT).set_color(YELLOW)
        line_moving.add_updater(updater_forth)
        
        self.add(line_reference, line_moving)
        self.wait(2)
        
        #movers toggle back and forth
        #by removing one and adding the other
        line_moving.remove_updater(updater_forth)
        line_moving.add_updater(updater_back)
        
        self.wait(2)
        
        line_moving.remove_updater(updater_back)
        self.wait(0.5)