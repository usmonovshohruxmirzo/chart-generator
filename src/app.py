import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

app_version = 1.0

root = tk.Tk()
root.title(f"Chart Generator v{app_version}")
root.geometry("1200x800")
root.resizable(False, False)

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=file_menu)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot([1, 2, 3, 4], [10, 4, 9, 10], marker="o", linestyle="-", color="blue")
ax.set_title("Line Chart")
ax.set_xlabel("X-axis Label")
ax.set_ylabel("Y-axis Label")
ax.grid(color="gray", linestyle=":", linewidth=0.5)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(pady=20)

def create_chart(chart_type, x=None, y=None, labels=None, **kwargs):
    ax.clear()
    if chart_type == "line":
        ax.plot(x, y, color=kwargs.get("color", "blue"), marker=kwargs.get("marker", "o"))
        ax.set_title("Line Chart")
        ax.set_xlabel(kwargs.get("xlabel", "X-axis"))
        ax.set_ylabel(kwargs.get("ylabel", "Y-axis"))
    elif chart_type == "bar":
        ax.bar(x, y, color=kwargs.get("color", "skyblue"))
        ax.set_title("Bar Chart")
        ax.set_xlabel(kwargs.get("xlabel", "Categories"))
        ax.set_ylabel(kwargs.get("ylabel", "Values"))
    ax.grid(kwargs.get("grid", True))
    canvas.draw()

def save_chart():
    fig.savefig("chart.png")
    messagebox.showinfo("Message", "Chart saved successfully as 'chart.png'!")

file_menu.add_command(label="Save as PNG", command=save_chart)

def update_chart_title():
    new_title = update_chart_title_input.get()
    if new_title:
        ax.set_title(new_title)
        clear_input_value(update_chart_title_input)
        canvas.draw()
    else:
        messagebox.showwarning("Warning", "Please enter a title.")

def clear_input_value(input):
    input.delete(0, tk.END)

def update_chart_color():
    new_color = update_chart_color_input.get()
    if new_color:
        try:
            ax.clear()
            ax.plot([1, 2, 3, 4], [10, 4, 9, 10], color=new_color, marker="o")
            ax.set_title("Line Chart")
            ax.set_xlabel("X-axis Label")
            ax.set_ylabel("Y-axis Label")
            ax.grid(color="gray", linestyle=":", linewidth=0.5)
            canvas.draw()
            clear_input_value(update_chart_color_input)
        except ValueError:
            messagebox.showerror("Error", "Invalid color. Please enter a valid color name.")
    else:
        messagebox.showwarning("Warning", "Please enter a color.")

def update_chart_plots():
    try:
        ax.clear()
        ax.grid()
        plots = [float(x) for x in update_chart_plots_input.get().split(",")]
        ax.plot(plots, marker="o", color="blue")
        ax.set_title("Updated Plot")
        ax.set_xlabel("Index")
        ax.set_ylabel("Value")
        canvas.draw()
        clear_input_value(update_chart_plots_input)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numbers separated by commas.")

update_chart_title_input_frame = tk.Frame(root)
update_chart_title_input_frame.pack(pady=10)

update_chart_title_input = ttk.Entry(update_chart_title_input_frame, width=22, font=("Arial", 20))
update_chart_title_input.pack(side=tk.LEFT, padx=5)

update_chart_title_input_button = tk.Button(
    update_chart_title_input_frame,
    text="Update Title",
    command=update_chart_title,
    font=("Arial", 14)
)
update_chart_title_input_button.pack(side=tk.LEFT)

update_chart_plots_input_frame = tk.Frame(root)
update_chart_plots_input_frame.pack(pady=10)

update_chart_plots_input = ttk.Entry(update_chart_plots_input_frame, width=22, font=("Arial", 20))
update_chart_plots_input.pack(side=tk.LEFT, padx=5)

update_chart_plots_input_button = tk.Button(
    update_chart_plots_input_frame,
    text="Update Plots",
    command=update_chart_plots,
    font=("Arial", 14)
)
update_chart_plots_input_button.pack(side=tk.LEFT)

update_chart_color_input_frame = tk.Frame(root)
update_chart_color_input_frame.pack(pady=10)

update_chart_color_input = ttk.Entry(update_chart_color_input_frame, width=22, font=("Arial", 20))
update_chart_color_input.pack(side=tk.LEFT, padx=5)

update_chart_color_input_button = tk.Button(
    update_chart_color_input_frame,
    text="Update Color",
    command=update_chart_color,
    font=("Arial", 14)
)
update_chart_color_input_button.pack(side=tk.LEFT)

root.mainloop()