""" CLI tool to mount/umount devices."""
import urwid

def handle_top_inputs(key):
    if key == 'q':
        raise urwid.ExitMainLoop()

def main():
    """ Main interface """
    palette = []
    body = urwid.Text("Hello world.", 'center')
    ui = urwid.Filler(body, 'middle')
    loop = urwid.MainLoop(ui, palette, unhandled_input=handle_top_inputs)
    loop.run()

if __name__ == "__main__":
    main()
