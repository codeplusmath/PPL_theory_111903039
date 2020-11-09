#!/usr/bin/env python
import gtk
import pygtk
pygtk.require('2.0')
w = gtk.Window(gtk.WINDOW_TOPLEVEL)

# observe: All class names are in "Title case".
# Line below: b becomes an object of type Button with the text
b = gtk.Button("Click me")
# this adds the button to the window. Try commenting the line below.
# Now we'll set some "event handlers"


def hello(widget, data=None):
    print "hello there!,this is ppl assignment"


# in the above, observe what is printed for p. Note that it is the object (self) getting passed.
# "clicked" has been pre-defined by gtk to mean left-mouse click.
b.connect_object("clicked", hello, None)


def delete_event(widget, data=None):
    print "Delete event has occured"
    return False


def destroy(widget, data=None):
    print "Destroy event has occured"
    gtk.main_quit()


w.connect_object("delete_event", delete_event, None)
w.connect_object("destroy", destroy, None)

w.add(b)
w.show()
b.show()
gtk.main()
