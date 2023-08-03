from tkinter import *
from tkinter.ttk import *

# Updates the bar value
def progress_bar_update():
    print("Button Pressed")


if __name__ == "__main__":
    print("Start of the GUI")

    root = Tk()

    # Set fixed constraints and dimensions for the window
    root.resizable(FALSE, FALSE)
    root.geometry("600x300")
    root.title("The Unsatisfactory Loading Bar")

    # Load in a Loading Bar
    prog = Progressbar(root, orient=HORIZONTAL, length=500, mode="determinate")

    # Button to activate loading animation for bar
    start_prog = Button(root, text='Start', command=progress_bar_update)

    prog.place(relx=0.5, rely=0.5, anchor=CENTER)
    start_prog.place(relx=0.5, rely=0.6, anchor=CENTER)

    print("End of GUI")
    root.mainloop()

