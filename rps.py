import tkinter
from tkinter import ttk
import time

def start_progress(bar: ttk.Progressbar, button: tkinter.Button, root: tkinter.Tk, label: tkinter.Label):
    button.destroy()
    speed = 100
    bar.start(speed)

    total_ms = bar["maximum"]*speed
    change_label(label, "Initializing checks...")
    root.after(int(total_ms/10), lambda: change_label(label, "Connecting to NASA databases"))
    root.after(int(4*total_ms/10), lambda: change_label(label, "Fighthing in Troyan wars"))
    root.after(int(7*total_ms/10), lambda: change_label(label, "Found a virus!!!!!"))
    root.after(int(8*total_ms/10), lambda: change_label(label, "Never mind..."))
    root.after(int(9*total_ms/10), lambda: change_label(label, "Mining crypto currencies"))
    root.after(total_ms, lambda: (on_done(bar, root), change_label(label, "")))

def change_label(label: tkinter.Label, text: str):
    label.config(text=text)

def on_done(bar: ttk.Progressbar, root: tkinter.Tk):
    bar.stop()
    bar["value"]=100

    result = tkinter.Label(root, text="No issues found. Your device is safe now!\n(Hint: run safety checks regularly to avoid issues in the future)")
    result.pack()

def main():
    root = tkinter.Tk()
    root.title("Windows Defender")
    root.minsize(500,500)

    label = tkinter.Label(root, text="Scan your device's safety")
    label.pack()

    progress = ttk.Progressbar(root, orient='horizontal', length=300, mode="determinate")
    progress.pack()

    label2 = tkinter.Label(root, text="")
    label2.pack()

    button = tkinter.Button(root, text="Start safety check", command= lambda: start_progress(progress, button, root, label2))
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()