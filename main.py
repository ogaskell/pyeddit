#!/usr/bin/env python

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf, Gdk, Gio
from widgets import Post


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="pyeddit")

        css_file = Gio.File.new_for_path("main.css")
        css_provider = Gtk.CssProvider()
        css_provider.load_from_file(css_file)
        context = Gtk.StyleContext()
        screen = Gdk.Screen.get_default()
        context.add_provider_for_screen(screen, css_provider,
                                        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        self.layout = Gtk.Grid()
        self.add(self.layout)

        self.headerbar = self.Header()
        self.set_titlebar(self.headerbar)

        self.testpost = Post(testimg=True)
        self.layout.attach(self.testpost, 0, 0, 1, 1)

        self.connect("configure-event", self.resize)

        for n in range(3):
            self.layout.attach(Post(title="Post " + str(n + 1)), 0, n + 1, 1, 1)

    def resize(self, x, y):
        width = self.get_allocation().width

        self.testpost.resize(width)

    class Header(Gtk.HeaderBar):
        def __init__(self):
            Gtk.HeaderBar.__init__(self)
            self.set_show_close_button(True)
            self.set_title("pyeddit")

            self.menu_btn = Gtk.Button.new_from_icon_name("help-contents", 3)

            self.logo_pixbuf = GdkPixbuf.Pixbuf.new_from_file("./images/On Dark/PNG/Reddit_Mark_OnDark.png")
            self.logo_pixbuf = self.logo_pixbuf.scale_simple(24, 24, GdkPixbuf.InterpType.BILINEAR)
            self.logo = Gtk.Image.new_from_pixbuf(self.logo_pixbuf)

            self.search_entry = Gtk.SearchEntry()

            self.pack_start(self.logo)
            self.pack_start(self.menu_btn)

            self.pack_end(self.search_entry)


win = MainWindow()
win.connect("destroy", Gtk.main_quit)

if __name__ == "__main__":
    win.show_all()
    Gtk.main()
