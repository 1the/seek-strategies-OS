# GUI for all the 6 algorithms
# for GUI
import tkinter as tk
from tkinter import messagebox

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
# for algrithms calss calling
from FCFS import fcfs_algorithm
from SSTF import sstf_algorithm
from SCAN import scan_algorithm
from LOOK import look_algorithm
from CSCAN import cscan_algorithm
from CLOOK import clook_algorithm

# Global variables to store the canvas and plot
canvas = None
plot = None
# Function to update the plot
def update_plot(sequence):
    global canvas, plot

    if canvas:
        plot.clear()

    # Plot requests including the head at the beginning
    plot.plot(sequence, range(len(sequence)), marker='o', label="Requests")

    plot.set_xlabel("Track Position")
    plot.set_ylabel("Request Number")
    plot.set_title("Disk Movement")
    plot.grid(True)
    plot.set_xlim(-1, max(sequence) + 1)
    plot.set_ylim(-1, len(sequence) + 1)
    plot.grid(True)
    plot.legend()
    plot.figure.canvas.draw()

# Function to handle algorithm selection
def run_algorithm():
    algorithm = algorithm_var.get()
    direction = direction_var.get()
    tracks = int(tracks_entry.get())

    requests = list(map(int, requests_entry.get().split(',')))
    # handling empty requests
    if not requests:
        messagebox.showerror("Error", "Please enter valid request numbers.")

    # handling the head position errors
    try:
        head_position = int(head_entry.get())
        if head_position < 0 or head_position >= tracks:
            raise ValueError

    except ValueError:
      messagebox.showerror("Error", "Please enter a valid head position.")


    if algorithm == "FCFS":
        # only head position and requests needed as it proceeds in the entry order and doesnot go to any edge unless there is a request
        sequence, total_tracks, average_tracks = fcfs_algorithm(head_position, requests)
    elif algorithm == "SSTF":
        # same as FCFS but orders requests and proceed according to the distance
        sequence, total_tracks, average_tracks = sstf_algorithm(head_position, requests)
    elif algorithm == "SCAN":
        # here we need a direction "in/out" and #of tracks as it proceeds to the edge track
        sequence, total_tracks, average_tracks = scan_algorithm(head_position, direction, tracks, requests)
    elif algorithm == "LOOK":
        # here we only need direction as it doesnot go to any edge unless there is a request
        sequence, total_tracks, average_tracks = look_algorithm(head_position, direction, requests)
    elif algorithm == "C-SCAN":
        # scan is always scan
        sequence, total_tracks, average_tracks = cscan_algorithm(head_position, direction, tracks, requests)
    elif algorithm == "C-LOOK":
        # look is look
        sequence, total_tracks, average_tracks = clook_algorithm(head_position, direction, requests)

    result_label.config(text=f"Sequence of tracks visited:\n{sequence}\n"
                             f"Total Traveled Tracks: {total_tracks: .2f}\n" 
                             f"average Traveled Tracks: {average_tracks: .2f}\n")

    update_plot(sequence)

# Create the main window
window = tk.Tk()
window.title("Disk Scheduling Algorithms")
window.geometry("700x750")

# Function to display coordinates on mouse motion
def on_motion(event):
    x, y = event.xdata, event.ydata
    if x is not None and y is not None:
        coordinates_label.config(text=f"X: {x:.2f}, Y: {y:.2f}")
    else:
        coordinates_label.config(text="")

# Create a frame for input fields
input_frame = tk.Frame(window)
input_frame.pack(pady=10)

# Algorithm selection
algorithm_label = tk.Label(input_frame, text="Algorithm:")
algorithm_label.grid(row=0, column=0, sticky="E")

algorithm_var = tk.StringVar(input_frame)
algorithm_var.set("FCFS")

algorithm_menu = tk.OptionMenu(input_frame, algorithm_var, "FCFS","SSTF" , "SCAN", "LOOK" , "C-SCAN" , "C-LOOK")
algorithm_menu.grid(row=0, column=1, padx=10)

# Head position
head_label = tk.Label(input_frame, text="Head Position:")
head_label.grid(row=1, column=0, sticky="E")

head_entry = tk.Entry(input_frame)
head_entry.grid(row=1, column=1, padx=10)

# Head direction
direction_label = tk.Label(input_frame, text="Direction:")
direction_label.grid(row=2, column=0, sticky="E")

direction_var = tk.StringVar(input_frame)
direction_var.set("Inward")

direction_menu = tk.OptionMenu(input_frame, direction_var, "Inward", "Outward")
direction_menu.grid(row=2, column=1, padx=10)

# Requests
requests_label = tk.Label(input_frame, text="Requests (comma-separated):")
requests_label.grid(row=3, column=0, sticky="E")

requests_entry = tk.Entry(input_frame)
requests_entry.grid(row=3, column=1, padx=10)

# Number of tracks
tracks_label = tk.Label(input_frame, text="Number of Tracks:")
tracks_label.grid(row=4, column=0, sticky="E")

tracks_entry = tk.Entry(input_frame)
tracks_entry.grid(row=4, column=1, padx=10)

# Button to run the algorithm
run_button = tk.Button(input_frame, text="Run Algorithm", command=run_algorithm)
run_button.grid(row=5, columnspan=2, pady=10)

# Frame for result display and plot
result_frame = tk.Frame(window)
result_frame.pack(pady=10)

# Label to display the result
result_label = tk.Label(result_frame, text="")
result_label.pack()

# Graph area for the plot
graph_frame = tk.Frame(window)
graph_frame.pack(pady=10)

# Create a Matplotlib figure and canvas
fig = plt.figure(figsize=(6, 4), dpi=100)
plot = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.get_tk_widget().pack()

# Label to display the coordinates
coordinates_label = tk.Label(window, text="")
coordinates_label.pack(pady=10)

# Bind the motion event to the canvas
canvas.mpl_connect("motion_notify_event", on_motion)

# Function to handle window close event
def on_close():
    window.quit()
    window.destroy()

#Set the close event handler
window.protocol("WM_DELETE_WINDOW", on_close)
# Start the GUI event loop
window.mainloop()