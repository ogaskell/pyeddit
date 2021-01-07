import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf

from math import floor


class WmButtons(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self, Gtk.Orientation.HORIZONTAL, 1)

        self.wm_close = Gtk.Button.new_from_icon_name("window-close-symbolic", 2)
        self.wm_maximise = Gtk.Button.new_from_icon_name("window-maximize-symbolic", 2)
        self.wm_minimise = Gtk.Button.new_from_icon_name("window-minimize-symbolic", 2)

        self.wm_close.connect("clicked", Gtk.main_quit)

        self.add(self.wm_minimise)
        self.add(self.wm_maximise)
        self.add(self.wm_close)

        self.win = None

    def connect_window(self, win):
        self.win = win

        self.wm_maximise.connect("clicked", lambda x: self.maximise())
        self.wm_minimise.connect("clicked", lambda x: win.iconify())

    def maximise(self):
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
    def __init__(self, sub="r/test", user="u/test", title="Test Post"):
        self.sub = sub
        self.user = user
        self.title = title

        Gtk.Box.__init__(self, Gtk.Orientation.VERTICAL, 0)
        self.set_orientation(Gtk.Orientation.VERTICAL)
        Gtk.StyleContext.add_class(self.get_style_context(), "frame")
        Gtk.StyleContext.add_class(self.get_style_context(), "post")
        self.set_hexpand(True)

        self.subuser_box = self.Post_header()
        self.pack_start(self.subuser_box, True, True, 10)

        self.post_title = Gtk.Label(label=self.title)
        self.post_title.set_alignment(0, 0)
        Gtk.StyleContext.add_class(self.post_title.get_style_context(), "post_title")
        self.pack_start(self.post_title, True, True, 10)

        self.content = self.Content_box(type="img", location="local", url="images/test.jpg")
        Gtk.StyleContext.add_class(self.content.get_style_context(), "post_content")
        self.pack_start(self.content, True, True, 10)

        self.actions = self.Action_bar()
        self.pack_start(self.actions, True, True, 0)

    class Post_header(Gtk.Box):
        def __init__(self, sub="r/test", user="u/test"):
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
        def __init__(self, type, location="local", url="images/test.jpg"):
            Gtk.Box.__init__(self)

    class Action_bar(Gtk.Box):
        def __init__(self):
            Gtk.Box.__init__(self)
            Gtk.StyleContext.add_class(self.get_style_context(), "frame")
            Gtk.StyleContext.add_class(self.get_style_context(), "post_actions")
            self.set_hexpand(True)
