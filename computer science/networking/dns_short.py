import manim as m

# Global script parameters
computer_scale = 0.3
myLaTeX = m.TexTemplate()
myLaTeX.add_to_preamble(r"\usepackage[T1]{fontenc} \usepackage{fontawesome}")


def computer() -> m.VGroup:
    """
    Return a VGroup representing a computer.
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dns_server = None

    def construct(self):
        title = m.Tex("Système de nom de domaine (DNS)",
                      tex_template=myLaTeX)

        # Display title
        self.play(m.FadeIn(title), run_time=2)
        self.wait(2)
        self.play(m.FadeOut(title))

        # Display user and maisonneuve
        user, user_ip, maisonneuve, maisonneuve_ip = self.create_user_and_maisonneuve()
        self.play(m.FadeIn(user, user_ip, maisonneuve, maisonneuve_ip), run_time=2)
        self.wait(2)

        # Display recursive resolver
        recursive, recursive_ip = self.recursive_resolver(user=user)

        # Display root server
        self.add_dns_request(recursive=recursive,
                             maisonneuve=maisonneuve,
                             request=".ca ?",
                             response="185.159.196.2",
                             dns_address=r"{\faGlobe} 192.203.230.10")

        # Top level domain server
        self.add_dns_request(recursive=recursive,
                             maisonneuve=maisonneuve,
                             request="cmaisonneuve.qc.ca ?",
                             response="162.219.54.2",
                             dns_address=r"{\faGlobe} 185.159.196.2")

        # Authoritative server
        self.add_dns_request(recursive=recursive,
                             maisonneuve=maisonneuve,
                             request="www.cmaisonneuve.qc.ca ?",
                             response="151.101.2.133",
                             dns_address=r"{\faGlobe} 162.219.54.2")

        # Transmit the IP address to the user
        arrow = m.Arrow(start=recursive_ip.get_corner(m.DOWN),
                        end=user.get_corner(m.UP))
        ip_address = m.Tex("151.101.2.133",
                           tex_template=myLaTeX)
        ip_address.next_to(arrow, m.RIGHT)
        self.play(m.GrowArrow(arrow))
        self.play(m.FadeIn(ip_address))
        self.wait(2)
        self.play(m.FadeOut(recursive, recursive_ip, arrow, ip_address))

        # Change ??? to the IP address
        maisonneuve_new_ip = m.Tex(r"{\faUniversity} ",
                                   "151.101.2.133",
                                   tex_template=myLaTeX)
        maisonneuve_new_ip.move_to(maisonneuve_ip.get_center())
        arrow2 = m.Arrow(start=user.get_corner(m.RIGHT),
                         end=maisonneuve.get_corner(m.LEFT))
        self.play(m.Transform(maisonneuve_ip, maisonneuve_new_ip))
        self.wait(2)
        self.play(m.GrowArrow(arrow2))

    def create_user_and_maisonneuve(self):
        user = computer().scale(computer_scale)
        user.shift(m.LEFT * 4 + m.DOWN)
        user_ip = m.Tex(r"{\faUser} 192.168.1.15", tex_template=myLaTeX)
        user_ip.next_to(user, m.DOWN)

        maisonneuve = computer().scale(computer_scale)
        maisonneuve.shift(m.RIGHT * 4 + m.DOWN)
        maisonneuve_ip = m.Tex(r"{\faUniversity} ", "???.???.???.???",
                               tex_template=myLaTeX)
        maisonneuve_ip.set_color_by_tex("???", m.RED)
        maisonneuve_ip.next_to(maisonneuve, m.DOWN)
        return user, user_ip, maisonneuve, maisonneuve_ip

    def recursive_resolver(self, *, user: m.VGroup):
        recursive = computer().scale(computer_scale)
        recursive.next_to(user, m.UP, buff=2)
        recursive_ip = m.Tex(r"{\faServer} ", "1.1.1.1",
                             tex_template=myLaTeX)
        recursive_ip.next_to(recursive, m.DOWN)

        arrow2 = m.Arrow(start=user.get_corner(m.UP), end=recursive_ip.get_corner(m.DOWN))
        address = ["www", ".",
                   "cmaisonneuve", ".",
                   "qc", ".",
                   "ca"]
        request2 = m.Tex(*address, " ?",
                         tex_template=myLaTeX)
        request2.next_to(arrow2, m.RIGHT)

        self.play(m.FadeIn(recursive, recursive_ip), run_time=2)
        self.play(m.GrowArrow(arrow2))
        self.play(m.FadeIn(request2))

        self.wait(2)
        request2[6].set_color(m.GREEN)
        self.wait(2)
        request2[4].set_color(m.GREEN)
        self.wait(2)
        request2[2].set_color(m.GREEN)
        self.wait(2)
        request2[0].set_color(m.GREEN)
        self.wait(2)
        request2.set_color(m.WHITE)
        self.play(m.FadeOut(request2, arrow2))
        self.wait(2)
        return recursive, recursive_ip

    def add_dns_request(self,
                        *,
                        recursive: m.VGroup,
                        maisonneuve: m.VGroup,
                        request: str,
                        response: str,
                        dns_address: str):
        """
        Add a DNS request to the self.
        """
        first_time = False
        if self.dns_server is None:
            first_time = True
            self.dns_server = computer().scale(computer_scale)
            self.dns_server.next_to(maisonneuve, m.UP, buff=2)

        dns = self.dns_server
        dns_ip = m.Tex(dns_address,
                       tex_template=myLaTeX)
        dns_ip.next_to(dns, m.DOWN)
        arrow_in = m.Arrow(start=recursive.get_corner(m.UR),
                           end=dns.get_corner(m.UL))
        request_tex = m.Tex(request,
                            tex_template=myLaTeX)
        request_tex.next_to(arrow_in, m.UP)

        arrow_out = m.Arrow(start=dns.get_corner(m.DL),
                            end=recursive.get_corner(m.DR))
        response_tex = m.Tex(response,
                             tex_template=myLaTeX)
        response_tex.next_to(arrow_out, m.DOWN)

        if first_time:
            self.play(m.FadeIn(dns, dns_ip), run_time=2)
        else:
            self.play(m.FadeIn(dns_ip), run_time=2)
        self.play(m.GrowArrow(arrow_in))
        self.play(m.FadeIn(request_tex))

        self.wait(2)
        self.play(m.GrowArrow(arrow_out))
        self.play(m.FadeIn(response_tex))

        self.wait(2)
        self.play(m.FadeOut(dns_ip, arrow_in, request_tex, arrow_out, response_tex))

        self.wait(2)
