# ui.py
import tkinter as tk
from threading import Thread, Event
from datetime import datetime
from awake import wide_awake
from battery import check_battery
import webbrowser

class CaffeineApp:
    def __init__(self, root):
        self.root = root
        self.root.iconbitmap("Caffeine.ico")
        self.root.title("Caffeine 2.0 by SAM")
        self.root.geometry("300x200")
        
        # Set the minimum window size
        root.minsize(300, 200)

        # Event to signal stopping the function
        self.stop_event = Event()

        # Variable to track whether the function is running
        self.is_running = False
        self.start_time = None  # To store start time
        self.elapsed_time_label = None  # Label for showing elapsed time

        # Create status label
        self.status_label = tk.Label(root, text="Can catch some ZZZZ", font=("Arial", 16, "bold"), fg="red")
        self.status_label.pack(pady=10)
        
        # Create a frame to hold the play and pause buttons in a single line
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        # Create play button inside the button frame
        self.play_button = tk.Button(button_frame, text="▶", font=("Arial", 16, "bold"), command=self.start_function, bg="green", fg="white")
        self.play_button.pack(side="left", padx=10)

        # Create pause button inside the button frame
        self.pause_button = tk.Button(button_frame, text="▩", font=("Arial", 16, "bold"), command=self.stop_function, state="disabled", bg="red", fg="white")
        self.pause_button.pack(side="left", padx=10)

        # Create a frame to display the start time and elapsed time
        self.status_frame = tk.Frame(root, bg="white")
        self.status_frame.pack(pady=10)

        # Start time label
        self.start_time_label = tk.Label(self.status_frame, text="Start Time: Not Started", bg="white")
        self.start_time_label.pack()

        # Elapsed time label (initially blank)
        self.elapsed_time_label = tk.Label(self.status_frame, text="Elapsed Time: 0 seconds", bg="white")
        self.elapsed_time_label.pack()

        # Bottom-right hyperlink
        self.hyperlink = tk.Label(root, text="Creator: Sameer-Jha", fg="blue", cursor="hand2", font=("Arial", 7, "underline"))
        self.hyperlink.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)  # Position at bottom right with padding
        self.hyperlink.bind("<Button-1>", lambda e: self.open_link())

        # Battery status watcher
        self.check_battery()

    def open_link(self):
        # Open the link in the default web browser
        webbrowser.open("https://Sameer-Jha.github.io")

    def start_function(self):
        if not self.is_running:
            # Set the start time and update the label
            self.start_time = datetime.now()
            self.start_time_label.config(text=f"Start Time: {self.start_time.strftime('%d-%m-%y %H:%M:%S')}")

            # Clear the stop event to allow the function to run
            self.stop_event.clear()

            # Start the background function in a new thread
            self.thread = Thread(target=wide_awake, args=(self.stop_event, 1))
            self.thread.start()

            # Update button states and status label
            self.is_running = True
            self.play_button.config(state="disabled")
            self.pause_button.config(state="normal")
            self.status_label.config(text="Wide Awake", fg="green")

            # Start updating elapsed time
            self.update_elapsed_time()

    def stop_function(self):
        if self.is_running:
            # Set the stop event to signal the function to stop
            self.stop_event.set()
            # Wait for the thread to finish
            self.thread.join()
            # Update button states and status label
            self.is_running = False
            self.play_button.config(state="normal")
            self.pause_button.config(state="disabled")
            self.status_label.config(text="Can catch some ZZZZ", font=("Arial", 16, "bold"), fg="red")

    def check_battery(self):
        check_battery()
        # Check battery level every 60 seconds
        self.root.after(60000, self.check_battery)

    def update_elapsed_time(self):
        if self.is_running:
            # Calculate the elapsed time since the start
            elapsed_time = int((datetime.now() - self.start_time).total_seconds())
            self.elapsed_time_label.config(text=f"Elapsed Time: {elapsed_time} seconds")
            # Call this function again after 1 second to continuously update
            self.root.after(1000, self.update_elapsed_time)
