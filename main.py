# main.py
import tkinter as tk
from app_ui import CaffeineApp

def main():
    # Set up the main window
    root = tk.Tk()
    app = CaffeineApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
