from typing import Callable
import manim as m
import numpy as np
# from manim import Scene, Axes, np, BLUE, RED, VGroup, RIGHT, Dot, Tex, \
#      DOWN, FadeIn, FadeOut


prime_approx = m.Tex(r"$f'(x) \approx \frac{f(x+\delta) - f(x - \delta)}{2 \delta}$")


class Intro(m.Scene):
    def construct(self):
        title = m.Tex("Dérivée de $e^x$")
        g = m.Group(title, prime_approx).arrange(m.DOWN, buff=1)
        self.play(m.Write(title), run_time=2)
        self.wait(4)
        self.play(m.FadeIn(prime_approx))
        self.wait(4)
        self.play(m.FadeOut(g))


class DerivApprox(m.Scene):
    def construct(self):
        func_axes = m.Axes(
            x_range=[1, 3],
            y_range=[0, 8, 2],
            tips=False,
            axis_config={"include_numbers": True},
            x_length=4,
            y_length=4,
        )

        # Then write labels for the axes
        func_label = func_axes.get_axis_labels(x_label="x", y_label="x^2")
        func_graph = m.VGroup(func_axes, func_label)

        # Display the numerical approximation of the derivative
        prime_exact = m.Tex(r"$(x^2)' = 2x$", color=m.RED)
        prime_approx = m.Tex(r"$f'(x) \approx \frac{f(x+\delta) - f(x - \delta)}{2 \delta}$",
                             color=m.GREEN)
        tex_eqns = m.VGroup(prime_approx, prime_exact).arrange(m.DOWN, buff=1)
        m.VGroup(func_graph, tex_eqns).arrange(m.RIGHT)

        # Display the function and derivative axes
        curve = func_axes.plot(lambda x: x**2, color=m.BLUE)
        self.add(func_graph, curve)
        self.wait(1)
        # Add dot at x = 2
        dot = m.Dot(func_axes.coords_to_point(2, 4), color=m.RED)
        curve_prime = func_axes.plot(lambda x: 4 * (x - 2) + 4, color=m.RED, x_range=[1.5, 2.5])
        self.play(m.FadeIn(dot, curve_prime, prime_exact))
        self.wait(1)
        # Add tangent line
        dot2 = m.Dot(func_axes.coords_to_point(2.5, 2.5**2), color=m.GREEN)
        dot3 = m.Dot(func_axes.coords_to_point(1.5, 1.5**2), color=m.GREEN)
        tangent = m.Line(func_axes.coords_to_point(1.5, 1.5**2),
                         func_axes.coords_to_point(2.5, 2.5**2),
                         color=m.GREEN)
        self.play(m.FadeIn(tangent, dot2, dot3, prime_approx))
        self.wait(1)


class Square(m.Scene):
    def construct(self):
        deriv_approx(scene=self,
                     func=lambda x: x ** 2,
                     func_x_range=[-3, 3],
                     func_y_range=[0, 9, 2],
                     func_label="x^2",
                     prime=lambda x: 2 * x,
                     prime_x_range=[-3, 3],
                     prime_y_range=[-6, 6, 2],
                     prime_label="2 x")


class Exp(m.Scene):
    def construct(self):
        group_exp, group_prime, dots = deriv_approx(scene=self,
                                                    func=np.exp,
                                                    func_x_range=[-3, 3],
                                                    func_y_range=[0, 20, 4],
                                                    func_label="e^x",
                                                    prime=np.exp)
        self.wait(2)

        # Merge the two graphs by centering them
        xExp, _, _ = group_exp.get_center()
        xPrime, _, _ = group_prime.get_center()
        prime_label = group_prime[1]
        group_prime = m.VGroup(group_prime[0], group_prime[2])
        self.play(m.FadeOut(prime_label), *[m.FadeOut(d) for d in dots])
        self.play(group_exp.animate.shift(m.RIGHT * abs(xExp)),
                  group_prime.animate.shift(m.LEFT * abs(xPrime)),
                  run_time=2, rate_func=m.linear)

        # Display the derivative of the exponential function
        prime_exact = m.Tex(r"$(e^x)' = e^x$")
        graphs = m.VGroup(group_exp, group_prime)
        prime_exact.next_to(graphs, m.DOWN, buff=1)
        self.play(m.Write(prime_exact), run_time=2)
        self.wait(2)


def deriv_approx(scene: m.Scene,
                 *,
                 func: Callable[[float], float],
                 func_x_range: list[float],
                 func_y_range: list[float],
                 func_label: str,
                 prime: Callable[[float], float],
                 prime_x_range: list[float] | None = None,
                 prime_y_range: list[float] | None = None,
                 prime_label: str | None = None) -> tuple[m.VGroup, m.VGroup, list[m.Dot]]:
    if prime_x_range is None:
        prime_x_range = func_x_range
    if prime_y_range is None:
        prime_y_range = func_y_range
    if prime_label is None:
        prime_label = f"({func_label})'"

    # Axes for the exponential function and its derivative
    func_axes = m.Axes(
        x_range=func_x_range,
        y_range=func_y_range,
        tips=False,
        axis_config={"include_numbers": True},
        x_length=4,
        y_length=4,
    )

    prime_axes = m.Axes(
        x_range=prime_x_range,
        y_range=prime_y_range,
        tips=False,
        axis_config={"include_numbers": True},
        x_length=4,
        y_length=4,
    )

    # First position the axis
    m.VGroup(func_axes, prime_axes).arrange(m.RIGHT, buff=1)

    # Then write labels for the axes
    mo_func_label = func_axes.get_axis_labels(x_label="x", y_label=func_label)
    mo_prime_label = prime_axes.get_axis_labels(x_label="x", y_label=prime_label)
    func_graph_1 = m.VGroup(func_axes, mo_func_label)
    prime_graph_1 = m.VGroup(prime_axes, mo_prime_label)
    graphs = m.VGroup(func_graph_1, prime_graph_1)

    # Display the numerical approximation of the derivative
    prime_approx = m.Tex(r"$f'(x) \approx \frac{f(x+\delta) - f(x - \delta)}{2 \delta}$")
    m.VGroup(graphs, prime_approx).arrange(m.DOWN, buff=1)

    # Display the function and derivative axes
    curve = func_axes.plot(func, color=m.BLUE)
    curve_prime = prime_axes.plot(prime, color=m.RED)
    scene.add(func_graph_1)
    scene.play(m.FadeIn(curve), run_time=3)
    scene.wait(2)
    scene.play(m.FadeIn(prime_approx), run_time=3)
    scene.wait(2)

    # Display the numerical approximation of the derivative
    points = [0, 1, 2, 3, -1, -2, -3]
    dots = [m.Dot(func_axes.coords_to_point(x, func(x)), color=m.RED) for x in points]
    scene.remove(prime_approx)
    scene.play(m.FadeIn(prime_graph_1))
    for i, x in enumerate(points):
        fprime = (func(x + 0.01) - func(x - 0.01)) / 0.02
        s = rf"$f'({x}) \approx \frac{{f({x}+0.01) - f({x} - 0.01)}}{{0.02}} \approx {fprime:.3f}$"
        tex = m.Tex(s)
        # VGroup(graphs, tex).arrange(DOWN, buff=1)
        tex.next_to(graphs, m.DOWN, buff=1)
        dot = dots[i]
        scene.add(dot, tex)
        scene.wait(0.5)
        scene.play(dot.animate.move_to(prime_axes.coords_to_point(x, fprime)))
        scene.wait(0.5)
        scene.remove(tex)
    scene.wait(1)
    scene.add(curve_prime)
    scene.wait(3)

    func_graph = m.VGroup(func_axes, mo_func_label, curve)
    prime_graph = m.VGroup(prime_axes, mo_prime_label, curve_prime)
    return func_graph, prime_graph, dots
