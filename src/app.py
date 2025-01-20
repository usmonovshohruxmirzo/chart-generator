import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

root = tk.Tk()
root.geometry("1000x800")
root.resizable(False, False)

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=file_menu)

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

def update_chart_color():
    new_color = update_chart_color_input.get()
    plt.plot([1, 2, 3, 4], [10, 4, 9, 10], color=new_color)
    canvas.draw()

update_chart_title_input_frame = tk.Frame(root)
update_chart_title_input_frame.pack(pady=10)

update_chart_title_input = ttk.Entry(update_chart_title_input_frame, width=22, font=("Arial", 20))
update_chart_title_input.pack(side=tk.LEFT, padx=5)
update_chart_title_input_button = tk.Button(update_chart_title_input_frame, text="Update Title", command=update_chart_title, font=("Arial", 14))
update_chart_title_input_button.pack(side=tk.LEFT)

update_chart_plots_input_frame = tk.Frame(root)
update_chart_plots_input_frame.pack(pady=10)

update_chart_plots_input = ttk.Entry(update_chart_plots_input_frame, width=22, font=("Arial", 20))
update_chart_plots_input.pack(side=tk.LEFT, padx=5)
update_chart_plots_input_button = tk.Button(update_chart_plots_input_frame, text="Update Plots", command=update_chart_title, font=("Arial", 14))
update_chart_plots_input_button.pack(side=tk.LEFT)

update_chart_color_input_frame = tk.Frame(root)
update_chart_color_input_frame.pack(pady=10)

update_chart_color_input = ttk.Entry(update_chart_color_input_frame, width=22, font=("Arial", 20))
update_chart_color_input.pack(side=tk.LEFT, padx=5)
update_chart_color_input_button = tk.Button(update_chart_color_input_frame, text="Update color", command=update_chart_color, font=("Arial", 14))
update_chart_color_input_button.pack(side=tk.LEFT)


save_button = tk.Button(root, text="Save chart", command=save_chart, font=("Arial", 20))
save_button.pack()

root.mainloop()
