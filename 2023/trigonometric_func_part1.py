from manimlib.imports import *


class SineEg(GraphScene, MovingCameraScene):
    CONFIG = {
        'axis_config': {
            'stroke_color': WHITE
        },
        'max_val': {
            "x_min": -20,
            "x_max": 20,
            "y_min": -20,
            "y_max": 20
        },
        "graph_origin": ORIGIN,
        "y_line_frequency": 1,
        "x_line_frequency": 1,
        "axes_color": BLUE,
        "x_min": -20,
        "x_max": 20, "y_min": -20,
        "y_max": 20,
        "x_axis_width": 80,
        "y_axis_height": 80,
        'get_axis': 0,
        'x_labeled_nums': range(-20, 20, 1),
        'y_labeled_nums': range(-20, 20, 1),
        "camera_config": {
            "camera_frame_rate": 100
        }
    }
    def setup(self):
        MovingCameraScene.setup(self)
    def construct(self):
        self.camera_frame_rate = 100
        self.setup_axes(animate=True)
        circle = Circle(radius=2)
        moving_dot = Dot()
        moving_dot.move_to(RIGHT * 2)
        dot_x = Dot().move_to(RIGHT * 2)
        dot_y = Dot().move_to(UP * 2)
        line_x = Line()
        line_y = Line()
        line_x.add_updater(
            lambda m: m.become(
                Line(start=np.array([moving_dot.get_x(), moving_dot.get_y(), 0]),
                    end=np.array([moving_dot.get_x(), 0, 0]))
            )
        )
        line_y.add_updater(
            lambda m: m.become(
                Line(start=np.array([moving_dot.get_x(), moving_dot.get_y(), 0]), 
                    end=np.array([0, moving_dot.get_y(), 0]))
            )
        )
        system = VGroup(dot_x, dot_y, line_y, line_x, moving_dot)
        vt_line_x = ValueTracker()
        vt_line_x.add_updater(
            lambda v: v.set_value(moving_dot.get_y())
        )
        vt_line_y = ValueTracker()
        vt_line_y.add_updater(
            lambda v: v.set_value(moving_dot.get_x())
        )
        sin = TextMobject('sin')
        sin.move_to(UP * 3.2)
        degree = ValueTracker()
        dec_degree1 = DecimalNumber(num_decimal_places=5, unit=r'^{\circ}=')
        dec_degree1.next_to(sin, direction=RIGHT)
        dec_degree1.add_updater(
            lambda v: v.set_value(degree.get_value())
        )
        cos = TextMobject('cos')
        cos.next_to(sin, direction=DOWN)
        dec_degree2 = DecimalNumber(num_decimal_places=5, unit=r'^{\circ}=')
        dec_degree2.next_to(cos, direction=RIGHT)
        dec_degree2.add_updater(
            lambda v: v.set_value(degree.get_value())
        )
        dec_x = DecimalNumber(vt_line_x.get_value(), num_decimal_places=8)
        dec_x.next_to(dec_degree1, direction=RIGHT, buff=0.8)
        # Choose this or the next: the first one may make much error and the 2nd is finer
        # dec_x.add_updater(lambda v: v.set_value(moving_dot.get_y() / 2))
        dec_x.add_updater(lambda v: v.set_value(math.sin(degree.get_value() * DEGREES)))
        dec_y = DecimalNumber(vt_line_y.get_value(), num_decimal_places=8)
        dec_y.next_to(dec_degree2, direction=RIGHT, buff=0.8)
        # dec_y.add_updater(lambda v: v.set_value(moving_dot.get_x() / 2))
        dec_y.add_updater(lambda v: v.set_value(math.cos(degree.get_value() * DEGREES)))
        tan = TextMobject('tan').move_to(LEFT * 5.4 + DOWN * 3)
        dec_degree3 = DecimalNumber(num_decimal_places=5, unit=r'^{\circ}=')
        dec_degree3.next_to(tan, direction=RIGHT)
        dec_degree3.add_updater(
            lambda v: v.set_value(degree.get_value())
        )

        number = TextMobject('0.0000000000')
        frac_line = Line(start=np.array([- number.get_width() / 2, 0, 0]),
                         end=np.array([number.get_width() / 2, 0, 0]))
        frac_line.shift(UP * tan.get_y())
        dec_up = DecimalNumber(num_decimal_places=8)
        dec_up.next_to(frac_line, direction=UP)
        dec_down = DecimalNumber(num_decimal_places=8)
        dec_down.next_to(frac_line, direction=DOWN)
        dec_up.add_updater(
            lambda v: v.set_value(math.sin(degree.get_value() * DEGREES))
        )
        dec_down.add_updater(
            lambda v: v.set_value(math.cos(degree.get_value() * DEGREES))
        )
        equals = TextMobject('=')
        equals.next_to(frac_line, direction=RIGHT)
        dec_tan = DecimalNumber(num_decimal_places=8)
        dec_tan.next_to(equals, direction=RIGHT)
        dec_tan.add_updater(
            lambda v: v.set_value(math.tan(degree.get_value() * DEGREES))
        )
        rotating_line = Line()
        rotating_line.add_updater(
            lambda m: m.become(
                Line(start=ORIGIN, end=moving_dot.get_center()).set_color(YELLOW)
            )
        )
        dec_angle_value = DecimalNumber(num_decimal_places=3, unit=r'^{\circ}')
        dec_angle_value.scale(0.5)
        dec_angle_value.move_to(RIGHT * 0.5)
        dec_angle_value.add_updater(
            lambda v: v.set_value(degree.get_value())
        )
        dec_angle_value_path = Arc(radius=1, start_angle=0, angle=PI, center=ORIGIN)
        dec_angle_value_path.set_opacity(0)
        angle_size = TextMobject('Angle size:')
        angle_size.move_to(UP * 3 + LEFT * 5.5)
        angle_size_dec = DecimalNumber(num_decimal_places=3, unit=r'^{\circ}')
        angle_size_dec.add_updater(
            lambda v: v.set_value(degree.get_value())
        )
        angle_size_dec.next_to(angle_size)
        self.play(Write(circle))
        self.wait(2)
        self.play(Write(system))
        self.add(dec_x, dec_y, sin, cos, tan, dec_degree1, dec_degree2, dec_degree3,
                 dec_tan, dec_up, dec_down, equals, frac_line, rotating_line, dec_angle_value_path, dec_angle_value,
                 angle_size_dec, angle_size)
        self.play(degree.set_value, 360, MoveAlongPath(moving_dot, circle), run_time=100, rate_func=linear,
                  *[MoveAlongPath(dec_angle_value, dec_angle_value_path, run_time=100)]
        )
        self.wait(2)

