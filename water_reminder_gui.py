import time
import threading
from plyer import notification
import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk

class WaterReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Water Reminder")
        self.root.geometry("400x200")
        self.root.configure(bg="lightblue")
        
        self.frame = tk.Frame(root, bg="lightblue")
        self.frame.pack(pady=20, padx=20)

        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.root.iconbitmap("C:/Users/cinty/OneDrive/Desktop/Coding/Projects/cyber-security/Project_237_Creating_a_Executable_Python_File/water_reminder.ico")
        self.root.resizable(False, False)

        font_style = tkFont.Font(family="Cascadia Mono Light", size=12)

        self.interval_label = ttk.Label(self.frame, text="Interval (minutes):", background="lightblue", font=font_style)
        self.interval_label.grid(row=0, column=0, pady=10, padx=10)

        self.interval_entry = ttk.Entry(self.frame)
        self.interval_entry.grid(row=0, column=1, pady=10, padx=10)

        self.start_button = ttk.Button(self.frame, text="Start", command=self.start_reminder, style="TButton")
        self.start_button.grid(row=1, column=0, pady=5, padx=10)

        self.stop_button = ttk.Button(self.frame, text="Stop", command=self.stop_reminder, style="TButton")
        self.stop_button.grid(row=1, column=1, pady=5, padx=10)

        self.status_bar = tk.Label(root, text="Welcome to Water Reminder!", bd=1, relief=tk.SUNKEN, anchor=tk.W, bg="lightblue", font=font_style)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        self.reminder_thread = None
        self.running = False

    def start_reminder(self):
        if not self.running:
            interval = int(self.interval_entry.get())
            if interval != 1:
                self.update_status(f"Reminder started every {interval} minutes.")
            else:
                self.update_status(f"Reminder started every {interval} minute.")
            self.running = True
            self.reminder_thread = threading.Thread(target=self.remind_to_drink_water, args=(interval,))
            self.reminder_thread.start()
    
    def stop_reminder(self):
        self.running = False
        self.update_status("Reminder stopped.")
        if self.reminder_thread:
            self.reminder_thread.join()
    
    def remind_to_drink_water(self, interval_minutes):
        while self.running:
            try:
                notification.notify(
                title="💦 Hydration Reminder 💦",
                message="It's time to drink water!",
                app_name="Water Reminder",
                timeout=10
                )
                time.sleep(interval_minutes * 60)
            except NotImplementedError as e:
                print(f'notification failed: {e}')
    
    def update_status(self, message):
        self.status_bar.config(text=message)

if __name__ == "__main__":
    root = tk.Tk()
    app = WaterReminderApp(root)
    root.mainloop()