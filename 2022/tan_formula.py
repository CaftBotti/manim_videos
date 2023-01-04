from manimlib.imports import *
from manimlib.once_useful_constructs.region import *


class IntroduceTanTheorem(TeacherStudentsScene):
    def construct(self):
        self.change_student_modes('happy', 'hooray', 'tease')
        self.teacher_says(
            'Maybe you have heard \\\\the $\\tan$(a+b) theorem',
            target_mode='speaking'
        )
        self.wait(3)
        self.play(RemovePiCreatureBubble(self.teacher, target_mode='happy'))
        self.play(
            Write(
                TexMobject(
                    r'\tan {(a+b)=}\frac{\tan a+\tan b}{1-\tan a \times \tan b}'
                ).move_to(UP * 2).scale(1.3)
            )
        )
        self.wait(2)
        self.teacher_says(
            "Let's proof it today"
        )
        self.change_student_modes(
            'erm', 'happy', 'thinking'
        )
        self.wait(2)
        self.teacher_says(
            'We will use geometry \\\\ to make it interesting!'
        )
        self.change_student_modes(
            'well', 'hooray', 'hesitant'
        )
        self.wait(2)
        self.student_says(
            "Let's go!",
            student_index=2,
            target_mode='happy'
        )
        self.wait(2)
        for object in self.mobjects:
            self.play(
                FadeOut(
                    object
                )
            )


class Proof(MovingCameraScene):
    def construct(self):
        main_square = Square()
        main_square.scale(3)
        point_r = np.array([-3, -3, 0])
        point_p = np.array([-3, 3, 0])
        point_q = np.array([3, 3, 0])
        point_t = np.array([3, 0, 0])
        point_u = np.array([1.5, 3, 0])
        point_s = np.array([3, -3, 0])
        rt = Line(
            start=point_r, end=point_t
        )
        pq = Line(
            start=point_p, end=point_q
        )
        ru = Line(
            start=point_r, end=point_u
        )
        arc_r = Arc(angle=53.130102354156 * DEGREES).move_to(np.array([-2.6, -2.78, 0]))
        arc_r.scale(0.5)
        arc_u = Arc(angle=53.130102354156 * DEGREES).move_to(np.array([1.12, 2.79, 0]))
        arc_u.scale(0.5)
        arc_t = Arc(angle=26.565051177078 * DEGREES).move_to(np.array([2.88, 0.49, 0]))
        arc_t.scale(0.5)
        arc_t.rotate(90 * DEGREES)
        arc_u.rotate(180 * DEGREES)
        ut = Line(
            start=point_t, end=point_u
        )
        rs = Line(
            start=point_r, end=point_s
        )
        st = Line(
            start=point_s, end=point_t
        )
        number_plane = NumberPlane()

        a_mark_r = TexMobject('a').move_to(np.array([-2.16, -2.83, 0]))
        a_mark_r.scale(0.8)

        a_mark_t = TexMobject('a').move_to(np.array([2.78, 0.94, 0]))
        a_mark_t.scale(0.8)

        b_mark_r = TexMobject('b').move_to(np.array([-2.35, -2.48, 0]))
        b_mark_r.scale(0.8)

        ab_mark_u = TexMobject('a+b').move_to(np.array([0.46, 2.62, 0]))
        ab_mark_u.scale(0.8)

        side_length = TextMobject('1').move_to(np.array([0, -3.26, 0]))

        tan_a_ts = TextMobject('$\\tan a$').rotate(90 * DEGREES, axis=IN).set_color(WHITE)
        tan_a_ts.move_to(np.array([3.5, -1.5, 0]))

        tan_b_qt = TextMobject('$\\tan b$').rotate(90 * DEGREES, axis=IN).set_color(WHITE)
        tan_b_qt.move_to(np.array([3.5, 1.5, 0]))

        tan_a_tan_b_uq = TextMobject('$\\tan a\\times\\tan b$').scale(0.5)
        tan_a_tan_b_uq.move_to(np.array([2.25, 3.28, 0]))

        one_minus_tan_a_tan_b_pu = TextMobject('$1-\\tan a\\tan b$').scale(0.75)
        one_minus_tan_a_tan_b_pu.move_to(np.array([-0.75, 3.35, 0]))

        one_div_cos_a_rt = TextMobject('$\\frac{1}{\\cos a}$')
        one_div_cos_a_rt.move_to(np.array([0, -1, 0]))
        one_div_cos_a_rt.rotate(26.565051177078 * DEGREES)

        tan_b_div_cos_a_ut = TextMobject('$\\frac{\\tan b}{\\cos a}$')
        tan_b_div_cos_a_ut.move_to(np.array([1.65, 1.3, 0]))

        tan_a_plus_tan_b_rp = TextMobject('$\\tan {a}+\\tan b$')
        tan_a_plus_tan_b_rp.move_to(np.array([-3.5, 0, 0]))
        tan_a_plus_tan_b_rp.rotate(90 * DEGREES)

        p_label = TexMobject('P').next_to(point_p, direction=UL)
        u_label = TexMobject('U').next_to(point_u, direction=UL)
        r_label = TexMobject('R').next_to(point_r, direction=DL)
        q_label = TexMobject('Q').next_to(point_q, direction=UR)
        t_label = TexMobject('T').next_to(point_t, direction=RIGHT)
        s_label = TexMobject('S').next_to(point_s, direction=DR)

        square_group = VGroup(p_label, q_label, r_label, s_label, main_square)

        right_angle_label_t = VGroup(
            Square().move_to(np.array([2.723, 0.096, 0])).scale(0.2).rotate(26.565051177078 * DEGREES)
        )

        all = VGroup(
            main_square, ut, ru, pq, u_label,
        )
        all_mobjects = VGroup(
            main_square, ut, ru, pq, rs, s_label, q_label, r_label, t_label, u_label, p_label,
        )

        # Texts

        this_is_square = TextMobject('This is a square').move_to(np.array([0, 6, 0]))
        this_is_square.scale(2.5)

        its_side_length = TextMobject('Its side length is 1').move_to(np.array([0, 6, 0]))
        its_side_length.scale(2.5)

        point_group_1 = VGroup(
            r_label, s_label, q_label, p_label
        )

        take_point_t = TextMobject('Take any point $\\mathit{T}$ \\\\'
                                   'on the line $\\mathit{QS}$')
        take_point_t.move_to(np.array([-0.5, 0.6, 0]))
        take_point_t.scale(0.8)

        point_t_arrow = Arrow(start=take_point_t, end=point_t, max_tip_length_to_length_ratio=0.1)
        point_t_arrow.set_stroke(width=2)

        group_1 = VGroup(take_point_t, point_t_arrow)

        connect_rt = TextMobject('Connect $\\mathit{RT}$')
        connect_rt.move_to(np.array([-0.5, 0.6, 0]))

        connect_rt_arrow = Arrow(start=connect_rt, end=rt.get_center(), max_tip_length_to_length_ratio=0.1)
        connect_rt_arrow.set_stroke(width=2)

        group_2 = VGroup(connect_rt_arrow, connect_rt)

        draw_vertical_ut = TextMobject('Draw the vertical line of $\\mathit{RT}$ \\\\'
                                       'which intersects with $\\mathit{PQ}$ \\\\'
                                       'at point $\\mathit{U}$').scale(0.8)
        draw_vertical_ut.move_to(np.array([-1, 0.6, 0]))
        draw_ut_arrow = Arrow(start=draw_vertical_ut.get_center() + UP, end=point_u,
                              max_tip_length_to_length_ratio=0.08)
        draw_ut_arrow.set_stroke(width=2)

        group_3 = VGroup(draw_ut_arrow, draw_vertical_ut)

        connect_ru = TextMobject('Connect $\\mathit{RU}$')
        connect_ru.move_to(np.array([-3.8, 2, 0]))

        connect_ru_arrow = Arrow(start=connect_ru, end=ru.get_center(),
                                 max_tip_length_to_length_ratio=0.08)
        connect_ru_arrow.set_stroke(width=2)

        group_4 = VGroup(connect_ru_arrow, connect_ru)

        anim_1 = VGroup(
            u_label, ru, ut, right_angle_label_t
        )
        anim_2 = VGroup(
            st, rs, s_label, r_label
        )

        now_look_at_tsr = TextMobject('Now look at $\\triangle$$\\mathit{TSR}$')
        now_look_at_tsr.move_to(
            np.array([-0.5, 0.6, 0])
        )

        now_look_at_tsr_arrow = Arrow(
            start=now_look_at_tsr.get_center() + DOWN * 0.5,
            end=rt.get_center(),
            max_tip_length_to_length_ratio=0.08
        )
        now_look_at_tsr_arrow.set_stroke(
            width=2
        )

        group_5 = VGroup(
            now_look_at_tsr_arrow, now_look_at_tsr
        )

        tan_a_equals = TexMobject(R'\tan {a}=\frac{TS}{RS}\\'
                                  R'\mathrm{and~}TS=1\times\tan {a}\\'
                                  R'\mathrm{so~}TS=\tan {a}')
        tan_a_equals.move_to(np.array([-1.3, 1.2, 0]))
        tan_a_equals_arrow = Arrow(start=tan_a_equals.get_center() + DOWN * 2,
                                   end=st.get_center(),
                                   max_tip_length_to_length_ratio=0.05)
        tan_a_equals_arrow.set_stroke(width=2)
        group_6 = VGroup(tan_a_equals_arrow, tan_a_equals)

        self.camera_frame.save_state()
        self.camera_frame.set_width(main_square.get_width() * 5)

        self.play(Write(main_square))
        self.wait(2)
        self.play(Write(this_is_square))
        self.wait(3)
        self.play(Transform(this_is_square, its_side_length))
        self.wait(3)
        self.play(Restore(self.camera_frame),
                  Write(side_length))
        self.wait(3)
        self.play(Write(point_group_1))
        self.wait(2.5)
        self.play(square_group.fade, 0.5)
        self.play(Write(group_1))
        self.wait()
        self.play(Write(t_label))
        self.wait(3)
        self.play(ReplacementTransform(group_1, group_2))
        self.wait()
        self.play(Write(rt))
        self.wait(3)
        self.play(ReplacementTransform(group_2, group_3))
        self.wait()
        self.play(Write(ut))
        self.play(Write(u_label))
        self.play(Write(right_angle_label_t))
        self.wait(3)
        self.play(ReplacementTransform(group_3, group_4))
        self.play(Write(ru))
        self.wait(3)
        self.play(
            anim_1.fade,
            anim_2.fade,
            VGroup(r_label, s_label).set_opacity, 1
        )
        self.play(ReplacementTransform(group_4, group_5))
        self.wait(2)
        self.play(ReplacementTransform(group_5, group_6))
        self.wait(2)
        self.play(Write(tan_a_ts))


class Flip(Scene):
    def construct(self):
        text = TextMobject('Flip flip')
        text.flip(axis=RIGHT)
        self.add(text)
