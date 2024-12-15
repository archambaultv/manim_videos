import manim as m


myLaTeX = m.TexTemplate()
myLaTeX.add_to_preamble(r"\usepackage[T1]{fontenc}")


def computer() -> m.VGroup:
    """
    Return a VObject representing a computer.
    """
    screen = m.RoundedRectangle(width=4, height=3, corner_radius=0.1)
    # Add cursor to the screen
    cursor_tip_shift = m.RIGHT * 0.3 + m.DOWN * 0.2
    cursor_line1 = m.Line(start=screen.get_corner(m.UP + m.LEFT),
                          end=screen.get_corner(m.UP + m.LEFT) + cursor_tip_shift)
    cursor_line2 = m.Line(start=screen.get_corner(m.UP + m.LEFT) + m.DOWN * 0.4,
                          end=screen.get_corner(m.UP + m.LEFT) + cursor_tip_shift)
    cursor_line3 = m.Line(start=screen.get_corner(m.UP + m.LEFT) + cursor_tip_shift + m.DOWN * 0.2 + m.RIGHT * 0.1,
                          end=screen.get_corner(m.UP + m.LEFT) + cursor_tip_shift + m.DOWN * 0.2 + m.RIGHT * 0.4)

    cursor = m.VGroup(cursor_line1, cursor_line2, cursor_line3)
    cursor.move_to(screen.get_corner(m.UP + m.LEFT) + m.RIGHT * 0.8 + m.DOWN * 0.5)

    keyboard = m.RoundedRectangle(width=4, height=1, corner_radius=0.1)
    keyboard.next_to(screen, m.DOWN, buff=0.33)
    # Add lines to the keyboard
    keyboard_lines = m.VGroup()
    for i in range(1, 3):
        line = m.Line(start=keyboard.get_corner(m.DL) + m.RIGHT * 0.2, end=keyboard.get_corner(m.DR) - m.RIGHT * 0.2)
        line.shift(m.UP * (0.3 * i))
        keyboard_lines.add(line)

    computer = m.VGroup(screen, cursor, keyboard, keyboard_lines)
    return computer


class DNS(m.Scene):
    def construct(self):
        myLaTeX = m.TexTemplate()
        myLaTeX.add_to_preamble(r"\usepackage[T1]{fontenc} \usepackage{fontawesome}")
        title = m.Tex("Système de nom de domaine (DNS)",
                      tex_template=myLaTeX)

        # Display title
        self.play(m.FadeIn(title), run_time=2)
        self.wait(2)
        self.play(m.FadeOut(title))

        # Display user and maisonneuve
        user = computer().scale(0.5)
        user.shift(m.LEFT * 3)
        user_ip = m.Tex(r"{\faUser} 192.168.1.15", tex_template=myLaTeX)
        user_ip.next_to(user, m.DOWN)

        maisonneuve = computer().scale(0.5)
        maisonneuve.shift(m.RIGHT * 3)
        maisonneuve_ip = m.Tex(r"{\faUniversity} ???.???.???.???",
                               color=m.RED,
                               tex_template=myLaTeX)
        maisonneuve_ip.next_to(maisonneuve, m.DOWN)

        arrow = m.Arrow(start=user.get_corner(m.RIGHT), end=maisonneuve.get_corner(m.LEFT))
        self.play(m.FadeIn(user, user_ip, maisonneuve, maisonneuve_ip), run_time=2)
        self.play(m.GrowArrow(arrow))
        self.wait(2)
