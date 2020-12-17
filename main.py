import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

win = Gtk.Window(title="Pyeddit")
win.connect("destroy", Gtk.main_quit)

if __name__ == "__main__":
    win.show_all()
    Gtk.main()
