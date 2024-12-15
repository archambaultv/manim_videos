import manim as m


myLaTeX = m.TexTemplate()
myLaTeX.add_to_preamble(r"\usepackage[T1]{fontenc}")


def computer() -> m.VGroup:
    """
    Return a VObject representing a computer.
    """
    screen = m.Rectangle(width=4, height=3)
    # Add a > symbol to the screen
    cursor = m.Tex(r"\bf > \_", tex_template=myLaTeX)
    cursor.move_to(screen.get_corner(m.UP + m.LEFT) + m.RIGHT * 0.8 + m.DOWN * 0.5)

    keyboard = m.Rectangle(width=4, height=1)
    keyboard.next_to(screen, m.DOWN, buff=0.33)

    # Add lines to the keyboard
    key_lines = m.VGroup()
    for i in range(1, 3):
        line = m.Line(start=keyboard.get_corner(m.DL) + m.RIGHT * 0.2, end=keyboard.get_corner(m.DR) - m.RIGHT * 0.2)
        line.shift(m.UP * (0.3 * i))
        key_lines.add(line)

    computer = m.VGroup(screen, cursor, keyboard, key_lines)
    return computer


class DNS(m.Scene):
    def construct(self):
        myLaTeX = m.TexTemplate()
        myLaTeX.add_to_preamble(r"\usepackage[T1]{fontenc}")
        title = m.Tex("Système de nom de domaine (DNS)",
                      tex_template=myLaTeX)

        c1 = computer()

        self.play(m.FadeIn(title), run_time=3)
        self.play(m.FadeOut(title))
        self.play(m.Create(c1))
        self.wait(2)
