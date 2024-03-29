"""Library of custom widgets."""

from math import floor

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf


class WmButtons(Gtk.Box):
    """Buttons for the Window Border (close, maximise etc)."""

    def __init__(self) -> None:
        Gtk.Box.__init__(self, Gtk.Orientation.HORIZONTAL, 1)

        self.wm_close = Gtk.Button.new_from_icon_name("window-close-symbolic", 2)
        self.wm_maximise = Gtk.Button.new_from_icon_name("window-maximize-symbolic", 2)
        self.wm_minimise = Gtk.Button.new_from_icon_name("window-minimize-symbolic", 2)

        self.wm_close.connect("clicked", Gtk.main_quit)

        self.add(self.wm_minimise)
        self.add(self.wm_maximise)
        self.add(self.wm_close)

        self.win = None

    def connect_window(self, win: Gtk.Window) -> None:
        """Connect widget to parent window."""
        self.win = win

        self.wm_maximise.connect("clicked", lambda x: self.maximise())
        self.wm_minimise.connect("clicked", lambda x: win.iconify())

    def maximise(self) -> None:
        """Maximise window.

        Callback for maximise button.
        """
        if self.win is not None:
            try:
                if self.win.style_get_property("maximize_initially"):
                    self.win.unmaximise()
                else:
                    self.win.maximise()
            except ValueError:
                print("error :(")
                self.win.maximize()


class Post(Gtk.Box):
    """Widget to represent a single Post."""

    def __init__(self,
                 sub: str = "r/test",
                 user: str = "u/test",
                 title: str = "Test Post",
                 testimg: bool = False) -> None:
        self.sub = sub
        self.user = user
        self.title = title

        Gtk.Box.__init__(self, Gtk.Orientation.VERTICAL, 0)
        self.set_orientation(Gtk.Orientation.VERTICAL)
        Gtk.StyleContext.add_class(self.get_style_context(), "frame")
        Gtk.StyleContext.add_class(self.get_style_context(), "post")
        self.set_hexpand(True)
        self.set_homogeneous(False)

        self.subuser_box = self.Post_header()
        self.pack_start(self.subuser_box, True, True, 2)

        self.post_title = Gtk.Label(label=self.title)
        self.post_title.set_alignment(0, 0)
        Gtk.StyleContext.add_class(self.post_title.get_style_context(), "post_title")
        self.pack_start(self.post_title, True, True, 2)

        self.content = self.Content_box(type="img", location="local", url="images/test.jpg", test=testimg)
        Gtk.StyleContext.add_class(self.content.get_style_context(), "post_content")
        self.pack_start(self.content, True, True, 10)

        self.actions = self.Action_bar()
        self.pack_start(self.actions, True, True, 0)

    def resize(self, width: int) -> None:
        """Resize the widget."""
        self.content.resize(width)

    class Post_header(Gtk.Box):
        """Header of the post."""

        def __init__(self, sub: str = "r/test", user: str = "u/test") -> None:
            self.sub = sub
            self.user = user

            Gtk.Box.__init__(self, Gtk.Orientation.HORIZONTAL, 10)
            Gtk.StyleContext.add_class(self.get_style_context(), "post_header")
            self.set_hexpand(True)

            self.sub_label = Gtk.Label(label=self.sub)
            self.user_label = Gtk.Label(label=self.user)
            Gtk.StyleContext.add_class(self.sub_label.get_style_context(), "post_sub")
            Gtk.StyleContext.add_class(self.user_label.get_style_context(), "post_user")
            self.pack_start(self.sub_label, False, False, 10)
            self.pack_end(self.user_label, False, False, 10)

    class Content_box(Gtk.Box):
        """Widget to hold the post's content (text, image etc)."""

        def __init__(self,
                     type: int,
                     location: str = "local",
                     url: str = "images/test.png",
                     test: bool = False) -> None:
            Gtk.Box.__init__(self)

            if test:
                self.img_pixbuf = GdkPixbuf.Pixbuf.new_from_file("./images/test.png")
                self.img = Gtk.Image.new_from_pixbuf(self.img_pixbuf)

                self.add(self.img)

        def resize(self, width: int) -> None:
            """Resize the content."""
            width -= 100
            print(width)
            self.img_pixbuf = GdkPixbuf.Pixbuf.new_from_file("./images/test.png")\
                .scale_simple(width, floor(width * (9 / 16)), GdkPixbuf.InterpType.BILINEAR)
            self.img.set_from_pixbuf(self.img_pixbuf)

    class Action_bar(Gtk.Box):
        """Post's action bar (upvotes, comments etc)."""

        def __init__(self) -> None:
            Gtk.Box.__init__(self)
            Gtk.StyleContext.add_class(self.get_style_context(), "frame")
            Gtk.StyleContext.add_class(self.get_style_context(), "post_actions")
            self.set_hexpand(True)

            self.upvote = Gtk.Button(label="⬆")
            self.dnvote = Gtk.Button(label="⬇")
            self.score = Gtk.Label(label="1")

            Gtk.StyleContext.add_class(self.upvote.get_style_context(), "vote")
            Gtk.StyleContext.add_class(self.dnvote.get_style_context(), "vote")
            Gtk.StyleContext.add_class(self.upvote.get_style_context(), "action_button")
            Gtk.StyleContext.add_class(self.dnvote.get_style_context(), "action_button")

            self.comments = Gtk.Button(label="[com] 0")
            Gtk.StyleContext.add_class(self.comments.get_style_context(), "comments")
            Gtk.StyleContext.add_class(self.comments.get_style_context(), "action_button")

            self.award = Gtk.Button(label="* Award")
            Gtk.StyleContext.add_class(self.award.get_style_context(), "award")
            Gtk.StyleContext.add_class(self.award.get_style_context(), "action_button")

            self.more = Gtk.Button(label="...")
            Gtk.StyleContext.add_class(self.more.get_style_context(), "more")
            Gtk.StyleContext.add_class(self.more.get_style_context(), "action_button")

            self.pack_start(Spacer(), True, True, 0)

            self.pack_start(self.upvote, False, False, 2)
            self.pack_start(self.score, False, False, 4)
            self.pack_start(self.dnvote, False, False, 2)

            self.pack_start(Spacer(), True, True, 0)

            self.pack_start(self.comments, False, False, 4)

            self.pack_start(Spacer(), True, True, 0)

            self.pack_start(self.award, False, False, 4)

            self.pack_start(Spacer(), True, True, 0)

            self.pack_start(self.more, False, False, 4)

            self.pack_start(Spacer(), True, True, 0)


class Spacer(Gtk.Box):
    """Spacer widget.

    Probably bad practice, but works for now.
    """

    def __init__(self) -> None:
        Gtk.Box.__init__(self)

        self.set_hexpand(True)
