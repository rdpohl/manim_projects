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
            axis_config={"include_numbers": True,},
            x_length=10.89,
            y_length=6.5,
        )
        ax.set_color(BLACK)
        labels = ax.get_axis_labels(x_label="X",
                                    y_label="Y")
        labels.set_color(BLACK)
        self.add(ax, labels)

        #set in the dots
        dot_E  = Dot(ax.coords_to_point(1,7), color=BLACK)
        dot_G  = Dot(ax.coords_to_point(2,7), color=BLACK)
        dot_F  = Dot(ax.coords_to_point(7,7), color=BLACK)
        dot_H  = Dot(ax.coords_to_point(8,7), color=BLACK)
        dot_C  = Dot(ax.coords_to_point(4,7), color=BLACK)
        dot_D  = Dot(ax.coords_to_point(5,7), color=BLACK)
        dots_group = VGroup(dot_E,dot_G, dot_F,dot_H, dot_C, dot_D)
        self.add(dots_group)

        #add the labels for the dots
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

        #set in the line connecting the dots
        line_EH  = Line()
        line_EH.put_start_and_end_on(dot_E.get_center(),
                                     dot_H.get_center())
        line_EH.set_color(BLACK)
        self.play(Write(line_EH))

        radius = 3
        start_angle = 0
        arc_angle = PI * -1

        #draw the weight labeled A
        A_Color = PURE_BLUE
        dot_A   = Dot(ax.coords_to_point(4,2), radius=0.3, color=A_Color)
        dot_A_Text = Text('A').scale(0.5).next_to(dot_A, DOWN*0.3)
        dot_A_Text.set_color(A_Color)
        self.add(dot_A)
        self.play(Write(dot_A_Text))

        #draw line from C to A
        line_CA = Line()
        line_CA.put_start_and_end_on(dot_C.get_center(),
                                     dot_A.get_top())
        line_CA.set_color(A_Color)
        self.play(Write(line_CA))

        # #draw the template for arc ECF
        arc_EAF = Arc(radius=radius, start_angle=start_angle, angle=arc_angle, arc_center=dot_C.get_center())
        arc_EAF.set_color(A_Color)
        self.play(Create(arc_EAF))

        #create line CA Ball group
        CA_Group = VGroup(dot_C, line_CA, dot_A, dot_A_Text)
        self.add(CA_Group)

        #updaters
        def updater_forth(mobj, dt):
            mobj.rotate(dt,
                        about_point=dot_C.get_center())

        def updater_back(mobj, dt):
            mobj.rotate(-dt,
                        about_point=dot_C.get_center())

        #run ball back to x-axis
        self.play(Rotating(CA_Group,
                            radians=0.5*PI,
                            about_point=dot_C.get_center(),
                            run_time=1))
        
        #CA_theta_tracker = ValueTracker(0)
        #CA_Group.add_updater(
        #    lambda x: x.become(CA_Group.copy()).rotate(
        #        CA_theta_tracker.get_value() * DEGREES * -1,
        #        about_point=dot_C.get_center()))
        #self.play(CA_theta_tracker.animate.set_value(10))
        self.wait(0.5)
        CA_Group.add_updater(updater_back)
        #elf.wait(0.5)
        #CA_Group.remove_updater(updater_back)
        #self.wait(0.5)
        #CA_Group.add_updater(updater_forth)
        #self.wait(0.5)
        
        '''
        B_Color = ORANGE
        #draw the weight labeled B
        dot_B   = Dot(ax.coords_to_point(5,2), radius=0.2, color=B_Color)
        dot_B_Text = Text('B').scale(0.5).next_to(dot_B, DOWN*0.3)
        dot_B_Text.set_color(B_Color)
        self.add(dot_B)
        self.play(Write(dot_B_Text))

        #draw the line from D to B
        line_DB = Line()
        line_DB.put_start_and_end_on(dot_D.get_center(),
                                     dot_B.get_center())
        line_DB.set_color(B_Color)
        self.play(Write(line_DB))

        #draw the template for arc GBH
        arc_GBH = Arc(radius=radius, start_angle=start_angle, angle=arc_angle, arc_center=dot_D.get_center())
        arc_GBH.set_color(B_Color)
        self.play(Create(arc_GBH))
        '''

        self.wait(2)
