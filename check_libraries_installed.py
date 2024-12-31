def check_installed_libraries():
    try:
        import sqlite3
        print("sqlite3 is installed.")
    except ImportError:
        print("sqlite3 is not installed.")
    
    try:
        import tkinter as tk
        from tkinter import ttk, messagebox
        print("tkinter is installed.")
    except ImportError:
        print("tkinter is not installed.")
    
    try:
        from PIL import Image, ImageTk
        print("Pillow is installed.")
    except ImportError:
        print("Pillow is not installed.")

if __name__ == "__main__":
    check_installed_libraries()
