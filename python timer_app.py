import tkinter as tk
import winsound  # For sound alert

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Timer")
        
        # Customize appearance
        self.root.configure(bg="#F0F0F0")  # Background color
        self.timer_font = ("Helvetica", 48, "bold")  # Font for timer display
        self.button_font = ("Helvetica", 14)  # Font for buttons
        
        # Make window always on top
        self.root.attributes("-topmost", True)
        
        # Optionally remove window borders
        self.root.overrideredirect(True)  # Remove window title bar

        # Optionally set window transparency (alpha value between 0.0 and 1.0)
        # self.root.attributes("-alpha", 0.8)  # 80% opacity, adjust as needed

        # Initialize time (in seconds)
        self.time_left = 0

        # Set up labels
        self.time_display = tk.Label(root, text="00:00", font=self.timer_font, width=10, height=2, bg="#F0F0F0")
        self.time_display.pack(pady=20)

        # Set up buttons and inputs
        self.start_button = tk.Button(root, text="Start Timer", command=self.start_timer, font=self.button_font, bg="#4CAF50", fg="white")
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop Timer", command=self.stop_timer, font=self.button_font, bg="#f44336", fg="white")
        self.stop_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Reset Timer", command=self.reset_timer, font=self.button_font, bg="#008CBA", fg="white")
        self.reset_button.pack(pady=5)

        self.time_entry_label = tk.Label(root, text="Enter Time (HH:MM:SS):", font=self.button_font, bg="#F0F0F0")
        self.time_entry_label.pack(pady=5)

        self.time_entry = tk.Entry(root, font=self.button_font, width=15)
        self.time_entry.pack(pady=5)

    def update_time_display(self):
        minutes, seconds = divmod(self.time_left, 60)
        hours, minutes = divmod(minutes, 60)
        time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
        self.time_display.config(text=time_str)

    def start_timer(self):
        try:
            # Get input time in HH:MM:SS format
            time_input = self.time_entry.get()
            hours, minutes, seconds = map(int, time_input.split(":"))
            self.time_left = (hours * 3600) + (minutes * 60) + seconds
            self.update_time_display()
            self.run_timer()
        except ValueError:
            self.time_display.config(text="Invalid input format")

    def run_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.update_time_display()
            self.root.after(1000, self.run_timer)  # Update every second
        else:
            self.time_display.config(text="Time's up!")
            winsound.Beep(1000, 1000)  # Play a beep sound when time is up

    def stop_timer(self):
        self.time_left = 0
        self.update_time_display()

    def reset_timer(self):
        self.time_left = 0
        self.update_time_display()

    def close(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    
    # Allow the window to be closed using the 'X' button in the top right corner
    root.protocol("WM_DELETE_WINDOW", app.close)
    
    root.mainloop()
