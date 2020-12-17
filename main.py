import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="pyeddit")

        self.title = Gtk.Label(label="pyeddit", halign=Gtk.Align.CENTER)

        self.add(self.title)


win = MainWindow()
win.connect("destroy", Gtk.main_quit)

if __name__ == "__main__":
    win.show_all()
    Gtk.main()
