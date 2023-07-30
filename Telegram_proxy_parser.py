import re, os
import tkinter as tk
import pyglet


def on_button_click(button_id):
    global server_text
    global server_button
    global port_text
    global port_button
    global secret_text
    global secret_button

    if button_id == 1: # confrim
        # get link and validate it
        link = link_input.get()
        if re.match(pattern, link) is None: # doesn't match
            # create popup window and show error
            top = tk.Toplevel(window)
            top.geometry("650x250")
            top.title("Error")
            error_icon = tk.PhotoImage(file=dir_path + "\\image\\error.png")
            top.iconphoto(False, error_icon)

            tk.Label(top, text="Your link is not valied !", fg="red", font=("VazirMatn", 20)).pack()
            tk.Label(top, text="Please review the link.\nIf you sure that link is coorect,\nplease creating an issue in Gitea or Github to fix the bug.", font=("VazirMatn, 18")).pack()
            tk.Label(top, text="Gitea ID: deep_dreamer\nGithub ID: galaxy248", fg="#32458F", font=("VazirMatn, 18")).pack()
            tk.Button(
                top,
                text="OK",
                width=8,
                height=1,
                bg="blue",
                fg="yellow",
                font=("Roboto", 10),
                command=lambda: top.destroy()
            ).pack()
        
        else:
            sections = re.findall(pattern, link)
            proxy["server"] = sections[0][0]
            proxy["port"] = sections[0][7]
            proxy["secret"] = sections[0][8]

            server_text = tk.Label(window, text="Server", bg="#BDBDBD", font=("VazirMatn", "18"))
            server_text.place(x=20, y=195)
            server_button = tk.Button(
                window,
                text="Copy",
                width=8,
                height=1,
                bg="blue",
                fg="yellow",
                font=("Roboto", 12),
                command=lambda: copy_button_click(1)
            )
            server_button.place(x=120, y=200)

            port_text = tk.Label(window, text="Port", bg="#BDBDBD", font=("VazirMatn", "18"))
            port_text.place(x=20, y=250)
            port_button = tk.Button(
                window,
                text="Copy",
                width=8,
                height=1,
                bg="blue",
                fg="yellow",
                font=("Roboto", 12),
                command=lambda: copy_button_click(2)
            )
            port_button.place(x=120, y=250)

            secret_text = tk.Label(window, text="Secret", bg="#BDBDBD", font=("VazirMatn", "18"))
            secret_text.place(x=20, y=300)
            secret_button = tk.Button(
                window,
                text="Copy",
                width=8,
                height=1,
                bg="blue",
                fg="yellow",
                font=("Roboto", 12),
                command=lambda: copy_button_click(3)
            )
            secret_button.place(x=120, y=300)
        
    elif button_id == 2: # clear
        link_input.delete(0, tk.END)
        try:
            server_text.destroy()
            server_button.destroy()

            port_text.destroy()
            port_button.destroy()

            secret_text.destroy()
            secret_button.destroy()

        except Exception as e:
            pass


def copy_button_click(button_id):
    global proxy
    # paste arguments to clipboard
    if button_id == 1:
        window.clipboard_clear()
        window.clipboard_append(proxy["server"])
        window.update()
    elif button_id == 2:
        window.clipboard_clear()
        window.clipboard_append(proxy["port"])
        window.update()
    elif button_id == 3:
        window.clipboard_clear()
        window.clipboard_append(proxy["secret"])
        window.update()
    else:
        pass


# regex pattern for validate proxy link
pattern = r"https:\/\/t\.me\/proxy\?server=((2[01234]\d|25[0-5]|1\d{2}|\d{2}|\d)\.(2[01234]\d|25[0-5]|1\d{2}|\d{1,2})\.(2[01234]\d|25[0-5]|1\d{2}|\d{2}|\d)\.(2[01234]\d|25[0-5]|1\d{2}|\d{2}|\d)|((\w|\.|\-|\_)+))&port=(\d{1,4}|[1-5]\d{4}|6[0-5][0-5][0-3][0-5])&secret=(.+)"
# add fonts to app
dir_path = os.path.dirname(os.path.abspath(__file__))
pyglet.options['win32_gdi_font'] = True
pyglet.font.add_file(dir_path + "\\font\\Vazirmatn.ttf")
pyglet.font.add_file(dir_path + "\\font\\Colakind.ttf")
pyglet.font.add_file(dir_path + "\\font\\Roboto.ttf")

# set default values
proxy = {
    "server": None,
    "port": None,
    "secret": None
}
server_text = None
server_button = None
port_text = None
port_button = None
secret_text = None
secret_button = None

# create window and set configs
window = tk.Tk()
window.geometry("512x400")
window.configure(background="#BDBDBD")
window.title("Telegram Proxy")
app_icon = tk.PhotoImage(file=dir_path + "\\image\\Telegram_logo.png")
window.iconphoto(False, app_icon)

# set header
header = tk.Label(window, text="Telegram Proxy", fg="#00A2E8", bg="#EFE4B0", width="512", font=("ColaKind", 40))
header.pack()

# get proxy link
text0 = tk.Label(window, text="Please Type Your Telegram Proxy Link", bg="#BDBDBD", font=("VazirMatn", "14"))
text0.place(x=10, y=80)

link_input = tk.Entry(window, fg="yellow", bg="#7F7F7F", width=80)
link_input.config(highlightthickness=1, highlightbackground="#8F7500")
link_input.place(x=10, y=110)
link_input.get()

confrim_button = tk.Button(
    window,
    text="Confrim",
    width=10,
    height=0,
    bg="blue",
    fg="yellow",
    font=("Roboto", 10),
    command=lambda: on_button_click(1)
)
confrim_button.place(x=10, y=135)

clear_button = tk.Button(
    window,
    text="Clear",
    width=10,
    height=0,
    bg="blue",
    fg="yellow",
    font=("Roboto", 10),
    command=lambda: on_button_click(2)
)
clear_button.place(x=110, y=135)

window.mainloop()
