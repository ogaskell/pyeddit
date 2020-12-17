import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="pyeddit")

        self.layout = Gtk.Grid()
        self.add(self.layout)

        self.titlebar = self.Titlebar()
        self.layout.attach(self.titlebar, 0, 0, 1, 1)

    class Titlebar(Gtk.Box):
        def __init__(self):
            Gtk.Box.__init__(self, Gtk.Orientation.HORIZONTAL, 6)

            self.menu_btn = Gtk.Button.new_from_icon_name("help-contents", 3)

            self.logo_pixbuf = GdkPixbuf.Pixbuf.new_from_file("./images/On Dark/PNG/Reddit_Mark_OnDark.png")
            self.logo_pixbuf = self.logo_pixbuf.scale_simple(50, 50, GdkPixbuf.InterpType.BILINEAR)
            self.logo = Gtk.Image.new_from_pixbuf(self.logo_pixbuf)

            self.title = Gtk.Label(label="pyeddit", halign=Gtk.Align.CENTER)

            self.add(self.menu_btn)
            self.add(self.logo)
            self.add(self.title)


win = MainWindow()
win.connect("destroy", Gtk.main_quit)

if __name__ == "__main__":
    win.show_all()
    Gtk.main()
