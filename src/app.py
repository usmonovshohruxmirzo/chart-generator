import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

root = tk.Tk()
root.geometry("1000x800")
root.resizable(False, False)

fig, ax = plt.subplots(figsize=(5, 5))
ax.plot([1, 2, 3, 4], [10, 4, 9, 10])
ax.set_title("Line Chart")

prev_button = ttk.Button(root, text="Prev")
prev_button.pack(side=tk.RIGHT, padx=20)

next_button = ttk.Button(root, text="Next")
next_button.pack(side=tk.LEFT, padx=20)

def save_chart():
    fig.savefig("chart.png")
    messagebox.showinfo("Message", "Downloaded Successfully!")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(pady=20)

def update_chart_title():
    new_title = update_chart_title_input.get()
    ax.set_title(new_title)
    canvas.draw()

update_chart_title_input_frame = tk.Frame(root)
update_chart_title_input_frame.pack(pady=10)

update_chart_title_input = ttk.Entry(update_chart_title_input_frame)
update_chart_title_input.pack(side=tk.LEFT, padx=5)

update_chart_title_input_button = ttk.Button(update_chart_title_input_frame, text="Update Title", command=update_chart_title)
update_chart_title_input_button.pack(side=tk.LEFT)

update_chart_plots_input_frame = tk.Frame(root)
update_chart_plots_input_frame.pack(pady=10)

update_chart_plots_input = ttk.Entry(update_chart_plots_input_frame)
update_chart_plots_input.pack(side=tk.LEFT, padx=5)

update_chart_plots_input_button = ttk.Button(update_chart_plots_input_frame, text="Update Plots", command=update_chart_title)
update_chart_plots_input_button.pack(side=tk.LEFT)

save_button = ttk.Button(root, text="Save chart", command=save_chart)
save_button.pack()

root.mainloop()
