""" CLI tool to mount/umount devices."""
import urwid
import subprocess

def handle_top_inputs(key):
    if key == 'q':
        raise urwid.ExitMainLoop()

device_screen = None
mntpnt_screen = None

def getDeviceScreen():
    """ Return the device screen."""
    global device_screen
    if device_screen != None:
        return device_screen

    # actual setup
    title = urwid.Text("Select device: ", 'center')
    contents_ = subprocess.check_output("lsblk -o NAME,SIZE", shell=True)
    contents = urwid.Text(contents_, 'center')

    input_box = urwid.Edit('Enter device name: ', align='center', edit_text='sdb1')
    enter_button = urwid.Button('Next', on_press=nextScreen)
    button_columns = urwid.Columns([enter_button, ])
    button_line = urwid.Padding(button_columns, 'center', ('relative', 25))

    device_screen = urwid.Pile([title, urwid.Divider(), contents, input_box, button_line, ])
    return device_screen

def nextScreen(button):
    """ Function to go from init screen to mount point selection screen. """
    global top

    body = urwid.Filler(getMntpntScreen(), 'middle', min_height=10)
    ui = getScreen(body)

    top.original_widget = ui 

def getMntpntScreen():
    """ Return the mount point screen. """
    global mntpnt_screen
    if mntpnt_screen != None:
        return mntpnt_screen

    title = urwid.Text("Select mount point: ", 'center')
    mntpnt_screen = urwid.Pile([title, urwid.Divider(),])
    return mntpnt_screen

def getScreen(body):
    """ Actually creates a screen given a body widget.

    Adds the application level header and footer.
    """
    header = urwid.Text("Mounter", 'center')
    footer = urwid.Text("q to quit.", 'right')

    f = urwid.Frame(body, header=header, footer=footer)
    ui = urwid.Pile([(25, f)])
    return ui

def main():
    """ Main interface """
    global top
    palette = []

    body = urwid.Filler(getDeviceScreen(), 'middle', min_height=10)
    ui = getScreen(body)
    top = urwid.Filler(ui, 'middle')

    loop = urwid.MainLoop(top, palette, unhandled_input=handle_top_inputs)
    loop.run()

if __name__ == "__main__":
    main()
