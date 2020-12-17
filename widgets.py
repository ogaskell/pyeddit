import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class WmButtons(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self, Gtk.Orientation.HORIZONTAL, 1)

        self.wm_close = Gtk.Button.new_from_icon_name("window-close-symbolic", 2)
        self.wm_maximise = Gtk.Button.new_from_icon_name("window-maximize-symbolic", 2)
        self.wm_minimise = Gtk.Button.new_from_icon_name("window-minimize-symbolic", 2)

        self.add(self.wm_minimise)
        self.add(self.wm_maximise)
        self.add(self.wm_close)
