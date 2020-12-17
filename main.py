import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf

from widgets import WmButtons


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="pyeddit")

        self.layout = Gtk.Grid()
        self.add(self.layout)

        self.headerbar = self.Header()
        self.headerbar.connect_window(self)
        self.set_titlebar(self.headerbar)

    class Header(Gtk.HeaderBar):
        def __init__(self):
            Gtk.HeaderBar.__init__(self)
            self.set_show_close_button(True)
            self.set_title("pyeddit")

            self.menu_btn = Gtk.Button.new_from_icon_name("help-contents", 3)

            self.logo_pixbuf = GdkPixbuf.Pixbuf.new_from_file("./images/On Dark/PNG/Reddit_Mark_OnDark.png")
            self.logo_pixbuf = self.logo_pixbuf.scale_simple(24, 24, GdkPixbuf.InterpType.BILINEAR)
            self.logo = Gtk.Image.new_from_pixbuf(self.logo_pixbuf)

            self.search = Gtk.SearchBar()
            self.search_entry = Gtk.SearchEntry()
            self.search.connect_entry(self.search_entry)

            self.pack_start(self.logo)
            self.pack_start(self.menu_btn)

            self.pack_end(self.search_entry)
            self.pack_end(self.search)


win = MainWindow()
win.connect("destroy", Gtk.main_quit)

if __name__ == "__main__":
    win.show_all()
    Gtk.main()
