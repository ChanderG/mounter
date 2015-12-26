""" CLI tool to mount/umount devices."""
import urwid

def handle_top_inputs(key):
    if key == 'q':
        raise urwid.ExitMainLoop()

def main():
    """ Main interface """
    palette = []

    header = urwid.Text("Mounter", 'center')
    body = urwid.Filler(urwid.Text("Hello world.", 'center'), 'middle', min_height=10)
    footer = urwid.Text("q to quit.", 'right')

    ui = urwid.Pile([(25, urwid.Frame(body, header=header, footer=footer))])
    loop = urwid.MainLoop(urwid.Filler(ui, 'middle'), palette, unhandled_input=handle_top_inputs)
    loop.run()

if __name__ == "__main__":
    main()
