import manim as m

# Global script parameters
computer_scale = 0.25
old_dns_opacity = 0.4
tex_default_size = 32
myLaTeX = m.TexTemplate()
myLaTeX.add_to_preamble(r"\usepackage[T1]{fontenc} \usepackage{fontawesome}")


def myTex(*args: str, font_size=None) -> m.Tex:
    """
    Return a m.Tex object with the given arguments.
    """
    if font_size is None:
        font_size = tex_default_size
    return m.Tex(*args, tex_template=myLaTeX, font_size=font_size)


def computer() -> m.VGroup:
    """
    Return a VGroup representing a computer.
    The VGroup is made of a screen, a cursor, a keyboard and lines on the keyboard.
    """
    screen = m.RoundedRectangle(width=4, height=3, corner_radius=0.1)
    # Add cursor to the screen
    cursor_tip_shift = m.RIGHT * 0.3 + m.DOWN * 0.2
    cursor_line1 = m.Line(start=screen.get_corner(m.UP + m.LEFT),
                          end=screen.get_corner(m.UP + m.LEFT) + cursor_tip_shift)
    cursor_line2 = m.Line(start=screen.get_corner(m.UP + m.LEFT) + m.DOWN * 0.4,
                          end=screen.get_corner(m.UP + m.LEFT) + cursor_tip_shift)
    line3_base = screen.get_corner(m.UP + m.LEFT) + cursor_tip_shift + m.DOWN * 0.2
    cursor_line3 = m.Line(start=line3_base + m.RIGHT * 0.1,
                          end=line3_base + m.RIGHT * 0.4)

    cursor = m.VGroup(cursor_line1, cursor_line2, cursor_line3)
    cursor.move_to(screen.get_corner(m.UP + m.LEFT) + m.RIGHT * 0.8 + m.DOWN * 0.5)

    keyboard = m.RoundedRectangle(width=4, height=1, corner_radius=0.1)
    keyboard.next_to(screen, m.DOWN, buff=0.33)
    # Add lines to the keyboard
    keyboard_lines = m.VGroup()
    for i in range(1, 3):
        line = m.Line(start=keyboard.get_corner(m.DL) + m.RIGHT * 0.2,
                      end=keyboard.get_corner(m.DR) - m.RIGHT * 0.2)
        line.shift(m.UP * (0.3 * i))
        keyboard_lines.add(line)

    computer = m.VGroup(screen, cursor, keyboard, keyboard_lines)

    # Center the group
    computer.center()

    return computer


class DNS(m.Scene):
    def construct(self):

        # Display title
        title = m.Tex("Système de nom de domaine (DNS)",
                      tex_template=myLaTeX)
        self.play(m.FadeIn(title), run_time=2)
        self.wait(12)
        self.play(m.FadeOut(title))

        # Display user and maisonneuve
        user, user_ip, maisonneuve, maisonneuve_ip = self.create_user_and_maisonneuve()
        s = myTex("www.cmaisonneuve.qc.ca ?")
        s.next_to(user, m.RIGHT, buff=1)
        self.play(m.FadeIn(user, user_ip, maisonneuve, maisonneuve_ip), run_time=2)
        self.wait(10)
        self.play(m.FadeIn(s))
        self.wait(8)
        self.play(m.FadeOut(s))

        # Display recursive resolver
        recursive, recursive_ip, recursive_name = self.recursive_resolver(user=user)

        # Display dns server
        root, root_name, root_response = self.add_root_dns(
                          recursive=recursive,
                          request=".ca ?",
                          response="185.159.196.2",
                          dns_address=r"{\faGlobe} 192.203.230.10")
        tld, tld_name, tld_response = self.add_tld_dns(
                         recursive=recursive,
                         previous_response=root_response,
                         request="cmaisonneuve.qc.ca ?",
                         response="162.219.54.2",
                         dns_address=r"{\faGlobe} 185.159.196.2")
        auth, auth_name, auth_response = self.add_authoritative_dns(
                                   recursive=recursive,
                                   previous_response=tld_response,
                                   request="www.cmaisonneuve.qc.ca ?",
                                   response="151.101.2.133",
                                   dns_address=r"{\faGlobe} 162.219.54.2")

        # Transmit the IP address to the user
        arrow = m.Arrow(start=recursive.get_corner(m.LEFT),
                        end=user.get_corner(m.RIGHT))
        arrow.color = m.YELLOW
        ip_address = myTex("151.101.2.133")
        ip_address.set_color(m.YELLOW)
        ip_address.rotate(arrow.get_angle() + m.PI)
        ip_address.next_to(arrow, m.ORIGIN)
        ip_address.shift(m.UP * 0.4 + m.LEFT * 0.4)
        self.play(m.GrowArrow(arrow))
        self.play(m.ReplacementTransform(auth_response, ip_address))
        self.wait(2)

        self.play(m.FadeOut(arrow, recursive_ip),
                  recursive.animate.set_opacity(old_dns_opacity),
                  recursive_name.animate.set_opacity(old_dns_opacity))

        # Change ??? to the IP address
        maisonneuve_new_ip = myTex(r"{\faUniversity} ",
                                   "151.101.2.133")
        maisonneuve_new_ip.move_to(maisonneuve_ip.get_center())
        arrow2 = m.Arrow(start=user.get_corner(m.RIGHT),
                         end=maisonneuve.get_corner(m.LEFT))
        arrow2.color = m.BLUE
        self.play(m.ReplacementTransform(ip_address, maisonneuve_new_ip),
                  m.FadeOut(maisonneuve_ip))
        self.wait(2)
        self.play(m.GrowArrow(arrow2))
        self.wait(2)

        # DNS is a pyramidal system
        for x, y in [(root, root_name), (tld, tld_name), (auth, auth_name),
                     (recursive, recursive_name)]:
            x.set_opacity(1)
            y.set_opacity(1)
            self.play(m.Indicate(x), m.Indicate(y))
            self.wait(2)
            x.set_opacity(old_dns_opacity)
            y.set_opacity(old_dns_opacity)
        self.wait(2)

    def create_user_and_maisonneuve(self):
        user = computer().scale(computer_scale)
        user.color = m.BLUE
        user.shift(m.LEFT * 4 + m.DOWN * 2)
        user_ip = myTex(r"{\faUser} 192.168.1.15")
        user_ip.next_to(user, m.DOWN)

        maisonneuve = computer().scale(computer_scale)
        maisonneuve.color = m.DARK_BLUE
        maisonneuve.shift(m.RIGHT * 4 + m.DOWN * 2)
        maisonneuve_ip = myTex(r"{\faUniversity} ", "???.???.???.???")
        maisonneuve_ip.set_color_by_tex("???", m.RED)
        maisonneuve_ip.next_to(maisonneuve, m.DOWN)
        return user, user_ip, maisonneuve, maisonneuve_ip

    def recursive_resolver(self, *, user: m.VGroup):
        recursive = computer().scale(computer_scale)
        recursive.color = m.GREEN
        recursive.shift(m.DOWN * 0.5)

        recursive_name = myTex("serveur récursif")
        recursive_name.next_to(recursive, m.DOWN)

        recursive_ip = myTex(r"{\faGlobe} ", "1.1.1.1")
        recursive_ip.next_to(recursive_name, m.DOWN)

        arrow2 = m.Arrow(start=user.get_corner(m.UP), end=recursive.get_corner(m.UL))
        arrow2.color = m.YELLOW
        address = ["www", ".",
                   "cmaisonneuve", ".",
                   "qc", ".",
                   "ca"]
        request2 = myTex(*address, " ?")
        request2.color = m.YELLOW
        request2.rotate(arrow2.get_angle())
        request2.next_to(arrow2, m.ORIGIN)
        request2.shift(m.UP * 0.4 + m.LEFT * 0.4)

        self.play(m.FadeIn(recursive, recursive_ip, recursive_name), run_time=2)
        self.wait(10)
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
        self.play(m.FadeOut(request2, arrow2))
        self.wait(2)
        return recursive, recursive_ip, recursive_name

    def add_root_dns(self,
                     *,
                     recursive: m.VGroup,
                     request: str,
                     response: str,
                     dns_address: str):
        """
        Add the root DNS request to the scene.
        """
        dns = computer().scale(computer_scale)
        dns.color = m.GREEN_D
        dns.shift(m.LEFT * 4 + m.UP * 1.5)
        dns_name = myTex("serveur racine")
        dns_name.next_to(dns, m.DOWN)
        dns_ip = myTex(dns_address)
        dns_ip.next_to(dns_name, m.DOWN)
        dns_group = m.VGroup(dns, dns_name, dns_ip)

        arrow_in = m.Arrow(start=recursive.get_corner(m.UL),
                           end=dns_group.get_corner(m.UR))
        arrow_in.color = m.YELLOW
        request_tex = myTex(request)
        request_tex.color = m.YELLOW
        request_tex.rotate(arrow_in.get_angle() + m.PI)
        request_tex.next_to(arrow_in, m.ORIGIN)
        request_tex.shift(m.UP * 0.2 + m.RIGHT * 0.2)

        arrow_out = m.Arrow(start=dns_group.get_corner(m.UR),
                            end=recursive.get_corner(m.UL))
        arrow_out.shift(m.DOWN * 0.5 + m.LEFT * 0.3)
        arrow_out.color = m.YELLOW

        response_tex = myTex(response)
        response_tex.color = m.YELLOW
        response_tex.rotate(arrow_out.get_angle())
        response_tex.next_to(arrow_out, m.ORIGIN)
        response_tex.shift(m.DOWN * 0.25 + m.LEFT * 0.25)

        self.add_dns(dns, dns_name, dns_ip, arrow_in, request_tex, arrow_out, response_tex)

        return (dns, dns_name, response_tex)

    def add_tld_dns(self,
                    *,
                    previous_response: m.Tex,
                    recursive: m.VGroup,
                    request: str,
                    response: str,
                    dns_address: str):
        """
        Add the top level domain DNS request to the scene.
        """
        dns = computer().scale(computer_scale)
        dns.color = m.GREEN_D
        dns.shift(m.UP * 3)
        dns_name = myTex("serveur du domaine de premier niveau")
        dns_name.next_to(dns, m.DOWN)
        dns_ip = myTex(dns_address)
        dns_ip.next_to(dns_name, m.DOWN)

        arrow_in = m.Arrow(start=recursive.get_corner(m.UP),
                           end=dns_ip.get_corner(m.DOWN))
        arrow_in.shift(m.RIGHT * 0.25)
        arrow_in.color = m.YELLOW
        request_tex = myTex(request)
        request_tex.color = m.YELLOW
        request_tex.next_to(arrow_in, m.RIGHT)

        arrow_out = m.Arrow(start=dns_ip.get_corner(m.DOWN),
                            end=recursive.get_corner(m.UP))
        arrow_out.shift(m.LEFT * 0.25)
        arrow_out.color = m.YELLOW
        response_tex = myTex(response)
        response_tex.color = m.YELLOW
        response_tex.next_to(arrow_out, m.LEFT)

        self.add_dns(dns, dns_name, dns_ip, arrow_in, request_tex, arrow_out, response_tex,
                     previous_response)

        return (dns, dns_name, response_tex)

    def add_authoritative_dns(self,
                              *,
                              previous_response: m.Tex,
                              recursive: m.VGroup,
                              request: str,
                              response: str,
                              dns_address: str):
        """
        Add the authoritative DNS request to the scene.
        """
        dns = computer().scale(computer_scale)
        dns.color = m.GREEN_D
        dns.shift(m.RIGHT * 4 + m.UP * 1.5)
        dns_name = myTex("serveur faisant autorité")
        dns_name.next_to(dns, m.DOWN)
        dns_ip = myTex(dns_address)
        dns_ip.next_to(dns_name, m.DOWN)

        arrow_in = m.Arrow(start=recursive.get_corner(m.UR),
                           end=dns.get_corner(m.UL))
        arrow_in.scale(0.9)
        arrow_in.color = m.YELLOW

        request_tex = m.Tex(request, tex_template=myLaTeX, font_size=30)
        request_tex.color = m.YELLOW
        request_tex.next_to(arrow_in, m.LEFT)
        request_tex.shift(m.RIGHT * 1)

        arrow_out = m.Arrow(start=dns.get_corner(m.UL),
                            end=recursive.get_corner(m.UR))
        arrow_out.color = m.YELLOW
        arrow_out.scale(0.75)
        arrow_out.shift(m.DOWN * 2 + m.RIGHT * 0.75)

        response_tex = myTex(response)
        response_tex.color = m.YELLOW
        response_tex.rotate(arrow_out.get_angle() + m.PI)
        response_tex.next_to(arrow_out, m.ORIGIN)
        response_tex.shift(m.DOWN * 0.25 + m.RIGHT * 0.25)

        self.add_dns(dns, dns_name, dns_ip, arrow_in, request_tex, arrow_out, response_tex,
                     previous_response)

        return (dns, dns_name, response_tex)

    def add_dns(self, dns, dns_name, dns_ip, arrow_in, request_tex, arrow_out, response_tex,
                previous_response=None):
        if previous_response is not None:
            self.play(m.FadeIn(dns, dns_name), m.ReplacementTransform(previous_response, dns_ip))
        else:
            self.play(m.FadeIn(dns, dns_name, dns_ip))
        self.play(m.GrowArrow(arrow_in))
        self.play(m.FadeIn(request_tex))

        self.wait(2)
        self.play(m.GrowArrow(arrow_out))
        self.play(m.FadeIn(response_tex))

        self.wait(2)
        self.play(m.FadeOut(arrow_in, request_tex, arrow_out, dns_ip),
                  dns_name.animate.set_opacity(old_dns_opacity),
                  dns.animate.set_opacity(old_dns_opacity))
        self.wait(2)
