""" CLI tool to mount/umount devices."""
import urwid
import subprocess

def handle_top_inputs(key):
    if key == 'q':
        raise urwid.ExitMainLoop()

device_screen = None
mntpnt_screen = None
command_screen = None

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
    enter_button = urwid.Button('Next', goToScreen, getMntpntScreen)
    button_columns = urwid.Columns([enter_button, ])
    button_line = urwid.Padding(button_columns, 'center', ('relative', 25))

    device_screen = urwid.Pile([title, urwid.Divider(), contents, input_box, button_line, ])
    return device_screen

def goToScreen(button, getRelevantScreen):
    global top

    body = urwid.Filler(getRelevantScreen(), 'middle', min_height=10)
    ui = getScreen(body)

    top.original_widget = ui 

def getMntpntScreen():
    """ Return the mount point screen. """
    global mntpnt_screen
    if mntpnt_screen != None:
        return mntpnt_screen

    title = urwid.Text("Select mount point: ", 'center')
    contents_ = subprocess.check_output("ls /media", shell=True)
    contents = urwid.Text(contents_, 'center')

    input_box = urwid.Edit('Enter device name: ', align='center', edit_text='External')
    back_button = urwid.Button('Back', goToScreen, getDeviceScreen)
    enter_button = urwid.Button('Next', goToScreen, getCommandScreen)
    button_columns = urwid.Columns([back_button, enter_button, ])
    button_line = urwid.Padding(button_columns, 'center', ('relative', 25))

    mntpnt_screen = urwid.Pile([title, urwid.Divider(),contents, urwid.Divider(), input_box, button_line, ])
    return mntpnt_screen

def getCommandScreen():
    """ Return the command screen. """
    global command_screen
    if command_screen != None:
        return command_screen

    title = urwid.Text("Verify command: ", 'center')
    contents_ = "TODO" # TODO
    contents = urwid.Text(contents_, 'center')

    back_button = urwid.Button('Back', goToScreen, getMntpntScreen)
    finish_button = urwid.Button('Finish', goToScreen, getCommandScreen)
    button_columns = urwid.Columns([back_button, finish_button, ])
    button_line = urwid.Padding(button_columns, 'center', ('relative', 25))

    command_screen = urwid.Pile([title, urwid.Divider(), contents, urwid.Divider(), button_line, ])
    return command_screen

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
