import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x200")
root.configure(bg="black")

clock = tk.Label(
    root,
    font=("Arial", 50, "bold"),
    bg="black",
    fg="lime"
)
clock.pack(expand=True)

def show_time():
    current_time = strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(1000, show_time)

show_time()

root.mainloop()