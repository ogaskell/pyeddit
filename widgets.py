import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


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
