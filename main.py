import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="pyeddit")

        self.layout = Gtk.Grid()
        self.add(self.layout)

        self.headerbar = self.Header()
        self.set_titlebar(self.headerbar)

    class Header(Gtk.HeaderBar):
        def __init__(self):
            Gtk.HeaderBar.__init__(self)
            self.set_show_close_button(True)

            self.menu_btn = Gtk.Button.new_from_icon_name("help-contents", 3)

            self.logo_pixbuf = GdkPixbuf.Pixbuf.new_from_file("./images/On Dark/PNG/Reddit_Mark_OnDark.png")
            self.logo_pixbuf = self.logo_pixbuf.scale_simple(24, 24, GdkPixbuf.InterpType.BILINEAR)
            self.logo = Gtk.Image.new_from_pixbuf(self.logo_pixbuf)

            self.pack_start(self.logo)
            self.pack_start(self.menu_btn)
            self.add(self.title)


win = MainWindow()
win.connect("destroy", Gtk.main_quit)

if __name__ == "__main__":
    win.show_all()
    Gtk.main()
