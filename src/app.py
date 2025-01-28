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
ax.plot([1, 2, 3, 4], [10, 4, 9, 10], marker="o", linestyle="-", color="skyblue")
ax.set_title("Line Chart")
ax.set_xlabel("X-axis Label")
ax.set_ylabel("Y-axis Label")
ax.grid(color="gray", linestyle=":", linewidth=0.5)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(pady=20)

def create_chart(chart_type, x=None, y=None, labels=None, **kwargs):
    ax.clear()
    
    match chart_type:
        case "line":
            ax.plot(x, y, color=kwargs.get("color", "blue"), marker=kwargs.get("marker", "o"))
            ax.set_title("Line Chart")
            ax.set_xlabel(kwargs.get("xlabel", "X-axis"))
            ax.set_ylabel(kwargs.get("ylabel", "Y-axis"))
        case "bar":
            ax.bar(x, y, color=kwargs.get("color", "skyblue"))
            ax.set_title("Bar Chart")
            ax.set_xlabel(kwargs.get("xlabel", "Categories"))
            ax.set_ylabel(kwargs.get("ylabel", "Values"))
        case "scatter":
            ax.scatter(x, y, color=kwargs.get("color", "blue"), marker=kwargs.get("marker", "o"))
            ax.set_title("Scatter Plot")
            ax.set_xlabel(kwargs.get("xlabel", "X-axis"))
            ax.set_ylabel(kwargs.get("ylabel", "Y-axis"))
        case "barh":
            ax.barh(x, y, color=kwargs.get("color", "skyblue"))
            ax.set_title("Bar Chart")
            ax.set_xlabel(kwargs.get("xlabel", "Categories"))
            ax.set_ylabel(kwargs.get("ylabel", "Values"))
        case "hist":
            if x is not None:
                ax.hist(x, bins=kwargs.get("bins", 10), color=kwargs.get("color", "skyblue"))
                ax.set_title("Histogram")
                ax.set_xlabel(kwargs.get("xlabel", "Data"))
                ax.set_ylabel(kwargs.get("ylabel", "Frequency"))
            else:
                messagebox.showwarning("Warning", "Please provide data for the histogram.")
        case "pie":
            if labels and y:
                ax.pie(y, labels=labels, autopct=kwargs.get("autopct", "%.1f%%"), colors=kwargs.get("colors", None))
                ax.set_title("Pie Chart")
            else:
                messagebox.showwarning("Warning", "Please provide both labels and data for the pie chart.")
        case "stackplot":
            ax.stackplot(x, y, color=kwargs.get("color", "skyblue"))
            ax.set_title("Stack Plot")
            ax.set_xlabel(kwargs.get("xlabel", "X-axis"))
            ax.set_ylabel(kwargs.get("ylabel", "Values"))
        case "area_chart":
            ax.fill_between(x, y, color=kwargs.get("color", "skyblue"))
            ax.set_title("Area Chart")
            ax.set_xlabel(kwargs.get("xlabel", "X-axis"))
            ax.set_ylabel(kwargs.get("ylabel", "Values"))
        case "boxplot":
            ax.boxplot(y, vert=False, patch_artist=True, boxprops=dict(facecolor=kwargs.get("color", "skyblue")))
            ax.set_title("Box Plot")
            ax.set_xlabel(kwargs.get("xlabel", "Categories"))
            ax.set_ylabel(kwargs.get("ylabel", "Values"))
        case "violinplot":
            ax.violinplot(y)
            ax.set_title("Violin Plot")
            ax.set_xlabel(kwargs.get("xlabel", "Categories"))
            ax.set_ylabel(kwargs.get("ylabel", "Values"))
        case "stem":
            ax.stem(x, y, basefmt=" ", linefmt=kwargs.get("color", "blue"), markerfmt=kwargs.get("marker", "o"))
            ax.set_title("Stem Plot")
            ax.set_xlabel(kwargs.get("xlabel", "X-axis"))
            ax.set_ylabel(kwargs.get("ylabel", "Y-axis"))
        case "errorbar":
            ax.errorbar(x, y, yerr=kwargs.get("yerr", 0.1), fmt=kwargs.get("marker", "o"), color=kwargs.get("color", "skyblue"))
            ax.set_title("Error Bar Plot")
            ax.set_xlabel(kwargs.get("xlabel", "X-axis"))
            ax.set_ylabel(kwargs.get("ylabel", "Y-axis"))
        case "quiver":
            ax.quiver(x, y, u=kwargs.get("u", [0]*len(x)), v=kwargs.get("v", [0]*len(y)))
            ax.set_title("Quiver Plot")
            ax.set_xlabel(kwargs.get("xlabel", "X-axis"))
            ax.set_ylabel(kwargs.get("ylabel", "Y-axis"))
        case "streamplot":
            ax.streamplot(x, y, color=kwargs.get("color", "blue"))
            ax.set_title("Stream Plot")
            ax.set_xlabel(kwargs.get("xlabel", "X-axis"))
            ax.set_ylabel(kwargs.get("ylabel", "Y-axis"))
        case "imshow":
            ax.imshow(y, cmap=kwargs.get("color", "viridis"))
            ax.set_title("Heatmap")
            ax.set_xlabel(kwargs.get("xlabel", "X-axis"))
            ax.set_ylabel(kwargs.get("ylabel", "Y-axis"))
        case "3d_line_plot":
            ax.plot(x, y, zs=kwargs.get("z", 0), zdir="z", label=kwargs.get("label", "3D Line"))
            ax.set_title("3D Line Plot")
            ax.set_xlabel(kwargs.get("xlabel", "X-axis"))
            ax.set_ylabel(kwargs.get("ylabel", "Y-axis"))
        case "3d_scatter_plot":
            ax.scatter(x, y, zs=kwargs.get("z", 0), zdir="z", label=kwargs.get("label", "3D Scatter"))
            ax.set_title("3D Scatter Plot")
            ax.set_xlabel(kwargs.get("xlabel", "X-axis"))
            ax.set_ylabel(kwargs.get("ylabel", "Y-axis"))
        case "3d_surface_plot":
            ax.plot_surface(x, y, z=kwargs.get("z", [[0]*len(x)]*len(y)), cmap=kwargs.get("color", "viridis"))
            ax.set_title("3D Surface Plot")
            ax.set_xlabel(kwargs.get("xlabel", "X-axis"))
            ax.set_ylabel(kwargs.get("ylabel", "Y-axis"))
        case "3d_wireframe_plot":
            ax.plot_wireframe(x, y, z=kwargs.get("z", [[0]*len(x)]*len(y)), cmap=kwargs.get("color", "viridis"))
            ax.set_title("3D Wireframe Plot")
            ax.set_xlabel(kwargs.get("xlabel", "X-axis"))
            ax.set_ylabel(kwargs.get("ylabel", "Y-axis"))
        case "3d_contour_plot":
            ax.contour3D(x, y, z=kwargs.get("z", [[0]*len(x)]*len(y)), cmap=kwargs.get("color", "viridis"))
            ax.set_title("3D Contour Plot")
            ax.set_xlabel(kwargs.get("xlabel", "X-axis"))
            ax.set_ylabel(kwargs.get("ylabel", "Y-axis"))
        case "3d_bar_chart":
            ax.bar3d(x, y, kwargs.get("z", [0]*len(x)), color=kwargs.get("color", "blue"))
            ax.set_title("3D Bar Chart")
            ax.set_xlabel(kwargs.get("xlabel", "X-axis"))
            ax.set_ylabel(kwargs.get("ylabel", "Y-axis"))
        case "polar_plot":
            ax.plot(x, y, color=kwargs.get("color", "blue"))
            ax.set_title("Polar Plot")
            ax.set_xlabel(kwargs.get("xlabel", "Angle"))
            ax.set_ylabel(kwargs.get("ylabel", "Radius"))
        case "step_plot":
            ax.step(x, y, where="mid", color=kwargs.get("color", "blue"))
            ax.set_title("Step Plot")
            ax.set_xlabel(kwargs.get("xlabel", "X-axis"))
            ax.set_ylabel(kwargs.get("ylabel", "Y-axis"))
        case "log-log_plot":
            ax.loglog(x, y, color=kwargs.get("color", "blue"))
            ax.set_title("Log-Log Plot")
            ax.set_xlabel(kwargs.get("xlabel", "X-axis"))
            ax.set_ylabel(kwargs.get("ylabel", "Y-axis"))
        case "semi-log_x_plot":
            ax.semilogx(x, y, color=kwargs.get("color", "blue"))
            ax.set_title("Semi-Log X Plot")
            ax.set_xlabel(kwargs.get("xlabel", "X-axis"))
            ax.set_ylabel(kwargs.get("ylabel", "Y-axis"))
        case "semi-log_y_plot":
            ax.semilogy(x, y, color=kwargs.get("color", "blue"))
            ax.set_title("Semi-Log Y Plot")
            ax.set_xlabel(kwargs.get("xlabel", "X-axis"))
            ax.set_ylabel(kwargs.get("ylabel", "Y-axis"))
        case "spectrogram":
            ax.specgram(y, NFFT=kwargs.get("NFFT", 256), Fs=kwargs.get("Fs", 1))
            ax.set_title("Spectrogram")
            ax.set_xlabel(kwargs.get("xlabel", "Frequency"))
            ax.set_ylabel(kwargs.get("ylabel", "Amplitude"))
        case "arrow_plot":
            ax.quiver(x, y, angles="xy", scale_units="xy", scale=1)
            ax.set_title("Arrow Plot")
            ax.set_xlabel(kwargs.get("xlabel", "X-axis"))
            ax.set_ylabel(kwargs.get("ylabel", "Y-axis"))
        case _:
            messagebox.showinfo("not found")

    ax.grid(kwargs.get("grid", True))
    canvas.draw()

chart_img_num = 0
def save_chart():
    global chart_img_num
    chart_img_num += 1
    fig.savefig(f"./images/chart-{chart_img_num}.png")
    messagebox.showinfo("Message", "Chart saved successfully as 'chart.png' in /images folder")

file_menu.add_command(label="Save as PNG", command=save_chart)

chart_types = [
    "Line Plot",
    "Scatter Plot",
    "Bar Chart",
    "Horizontal Bar Chart",
    "Histogram",
    "Pie Chart",
    "Stack Plot",
    "Area Chart",
    "Box Plot",
    "Violin Plot",
    "Stem Plot",
    "Error Bar Plot",
    "Quiver Plot",
    "Stream Plot",
    "Heatmap",
    "3D Line Plot",
    "3D Scatter Plot",
    "3D Surface Plot",
    "3D Wireframe Plot",
    "3D Contour Plot",
    "3D Bar Chart",
    "Polar Plot",
    "Step Plot",
    "Log-Log Plot",
    "Semi-Log X Plot",
    "Semi-Log Y Plot",
    "Spectrogram",
    "Arrow Plot",
]

def select_chart_type(event=None):
    selected_option = select_chart.get()
    match selected_option:
        case "Line Plot":
            create_chart(
                "line",
                x=[1, 2, 3, 4],
                y=[10, 15, 20, 25],
            ) 
        case "Bar Chart":
            create_chart(
                "bar",
                x=["A", "B", "C", "D"],
                y=[10, 20, 15, 25],
            )
        case "Scatter Plot":
            create_chart(
                "scatter",
                x=[1, 2, 3, 4],
                y=[10, 15, 20, 25],
            ) 
        case "Horizontal Bar Chart":
            create_chart(
                "barh",
                x=["A", "B", "C", "D"],
                y=[10, 20, 15, 25],
            )
        case "Histogram":
            create_chart(
                "hist",
                x=["A", "B", "C", "D"],
                y=[10, 20, 15, 25],
            )
        case "Pie Chart":
            create_chart(
                "pie",
                y=[10, 20, 15, 25],
                labels=["A", "B", "C", "D"],
                colors=["red", "green", "blue", "yellow"]
            )
        case "Stack Plot":
            create_chart(
                "stackplot",
                x=["A", "B", "C", "D"],
                y=[10, 20, 15, 25],
            )
        case "Area Chart":
            create_chart(
                "area_chart",
                x=["A", "B", "C", "D"],
                y=[10, 20, 15, 25],
            )
        case "Box Plot":
            create_chart(
                "boxplot",
                x=["A", "B", "C", "D"],
                y=[10, 20, 15, 25],
            )
        case "Violin Plot":
            create_chart(
                "violinplot",
                y=[10, 20, 15, 25],
            )
        case "Stem Plot":
            create_chart(
                "stem",
                x=["A", "B", "C", "D"],
                y=[10, 20, 15, 25],
            )
        case "Error Bar Plot":
            create_chart(
                "errorbar",
                x=["A", "B", "C", "D"],
                y=[10, 20, 15, 25],
            )
        case "Quiver Plot":
            create_chart(
                "quiver",
                x=["A", "B", "C", "D"],
                y=[10, 20, 15, 25],
            )
        case "Stream Plot":
            create_chart(
                "streamplot",
                x=[1, 2, 3, 4],
                y=[10, 15, 20, 25],
            )
        case "Heatmap":
            create_chart(
                "imshow",
                x=[1, 2, 3, 4],
                y=[[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120], [130, 140, 150, 160]],
            )
        case "3D Line Plot":
            create_chart(
                "3d_line_plot",
                x=["A", "B", "C", "D"],
                y=[10, 20, 15, 25],
            )
        case "3D Scatter Plot":
            create_chart(
                "3d_scatter_plot",
                x=[1, 2, 3, 4],
                y=[10, 15, 20, 25],
                z=[5, 10, 15, 20]
            )
        case "3D Surface Plot":
            create_chart(
                "3d_surface_plot",
                x=[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                y=[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                z=[[10, 20, 30], [40, 50, 60], [70, 80, 90]],
            )
        case "3D Wireframe Plot":
            create_chart(
                "3d_wireframe_plot",
                x=[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                y=[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                z=[[10, 20, 30], [40, 50, 60], [70, 80, 90]],
            )
        case "3D Contour Plot":
            create_chart(
                "3d_contour_plot",
                x=[1, 2, 3],
                y=[1, 2, 3],
                z=[[10, 20, 30], [40, 50, 60], [70, 80, 90]],
            )
        case "3D Bar Chart":
            create_chart(
                "3d_bar_chart",
                x=[1, 2, 3],
                y=[10, 20, 30],
                z=[5, 10, 15],
            )
        case "Polar Plot":
            create_chart(
                "polar_plot",
                x=[0, 30, 60, 90],
                y=[1, 2, 3, 4],
            )
        case "Step Plot":
            create_chart(
                "step_plot",
                x=[1, 2, 3, 4],
                y=[10, 20, 30, 40],
            )
        case "Log-Log Plot":
            create_chart(
                "log-log_plot",
                x=[1, 2, 3, 4],
                y=[10, 100, 1000, 10000],
            )
        case "Semi-Log X Plot":
            create_chart(
                "semi-log_x_plot",
                x=[1, 2, 3, 4],
                y=[10, 100, 1000, 10000],
            )
        case "Semi-Log Y Plot":
            create_chart(
                "semi-log_y_plot",
                x=[1, 2, 3, 4],
                y=[10, 100, 1000, 10000],
            )
        case "Spectrogram":
            create_chart(
                "spectrogram",
                y=[10, 20, 30, 40, 50],
                NFFT=128,
                Fs=10,
            )
        case "Arrow Plot":
            create_chart(
                "arrow_plot",
                x=[1, 2, 3, 4],
                y=[10, 15, 20, 25],
            )
        case _:
            messagebox.showwarning("Warning", f"{selected_option} not implemented yet!")
        
select_chart = ttk.Combobox(root, values=chart_types, width=33)
select_chart.pack()
select_chart.bind("<<ComboboxSelected>>", select_chart_type)

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
        selected_option = select_chart.get()

        match selected_option:
            case "Line Plot":
                ax.plot(plots, marker="o", color="blue")
                ax.set_title("Updated Line Plot")
                ax.set_xlabel("Index")
                ax.set_ylabel("Value")
            case "Bar Chart":
                ax.bar(range(len(plots)), plots, color="blue")
                ax.set_title("Updated Bar Chart")
                ax.set_xlabel("Categories")
                ax.set_ylabel("Values")
            case _:
                messagebox.showwarning("Warning", f"{selected_option} updates not supported yet!")
                return

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