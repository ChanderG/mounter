""" CLI tool to mount/umount devices."""
import urwid
import subprocess

def handle_top_inputs(key):
    if key == 'q':
        raise urwid.ExitMainLoop()

device_screen = None

def getDeviceScreen():
    """ Return the device screen."""
    global device_screen
    if device_screen != None:
        return device_screen

    # actual setup
    title = urwid.Text("Select device: ", 'center')
    contents_ = subprocess.check_output("lsblk -o NAME,SIZE", shell=True)
    contents = urwid.Text(contents_, 'center')
    device_screen = urwid.Pile([title, urwid.Divider(), contents, ])
    return device_screen

def main():
    """ Main interface """
    palette = []

    header = urwid.Text("Mounter", 'center')
    body = urwid.Filler(getDeviceScreen(), 'middle', min_height=10)
    footer = urwid.Text("q to quit.", 'right')

    ui = urwid.Pile([(25, urwid.Frame(body, header=header, footer=footer))])
    loop = urwid.MainLoop(urwid.Filler(ui, 'middle'), palette, unhandled_input=handle_top_inputs)
    loop.run()

if __name__ == "__main__":
    main()
