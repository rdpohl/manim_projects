from manim import *

class MovingAngle(Scene):
    def construct(self):
        rotation_center = LEFT

        theta_tracker = ValueTracker(110) #110 = DEGREES
        line1 = Line(LEFT, RIGHT)
        line_moving = Line(LEFT, RIGHT)
        line_ref = line_moving.copy()
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )

        a = Angle(line1, line_moving, radius=0.5, other_angle=False)

        #latex text to place theta symbol on angle drawing
        tex = MathTex(r"\theta").move_to(
            Angle(
                line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )

        self.add(line1, line_moving, a, tex)
        self.wait()

        #line moving updater
        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )

        #angle updater
        a.add_updater(
            lambda x: x.become(Angle(line1, line_moving, radius=0.5, other_angle=False))
        )

        #latex symbol updater
        tex.add_updater(
            lambda x: x.move_to(
                Angle(
                    line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
                ).point_from_proportion(0.5)
            )
        )

        #moves line angle from 110 to 40 degrees
        self.play(theta_tracker.animate.set_value(40))
        #resets line angle to 180 degrees (140+40)
        self.play(theta_tracker.animate.increment_value(140))
        #turns theta symbol red
        self.play(tex.animate.set_color(RED), run_time=0.5)
        #moves line from 180 to 350 degrees
        self.play(theta_tracker.animate.set_value(350))
        self.wait(5)
