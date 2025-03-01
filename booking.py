import tkinter as tk
from tkinter import ttk

class BookingWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("New Booking")
        self.geometry("400x300")

        ttk.Label(self, text="Guest Name:").pack()
        self.name_entry = ttk.Entry(self)
        self.name_entry.pack()

        ttk.Button(self, text="Submit", command=self.submit_booking).pack()

    def submit_booking(self):
        guest_name = self.name_entry.get()
        print(f"Booking confirmed for {guest_name}")
