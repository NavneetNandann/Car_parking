import tkinter as tk
from tkinter import messagebox, font

class ParkingGUI:
    def __init__(self, root, parking_lot):
        self.root = root
        self.parking_lot = parking_lot
        self.root.title("Parking Management System")
        self.root.geometry("500x500")
        self.root.configure(bg="#E8F6EF")

        # Define fonts
        self.title_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.label_font = font.Font(family="Helvetica", size=14)
        self.button_font = font.Font(family="Helvetica", size=12, weight="bold")

        # Create a main frame to center content
        main_frame = tk.Frame(root, bg="#E8F6EF")
        main_frame.pack(expand=True, padx=20, pady=20)

        # Title Label
        self.title_label = tk.Label(main_frame, text="Parking Management System", font=self.title_font, fg="#2C3E50", bg="#E8F6EF")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Input for vehicle ID
        self.vehicle_id_label = tk.Label(main_frame, text="Enter Vehicle ID:", font=self.label_font, fg="#2980B9", bg="#E8F6EF")
        self.vehicle_id_label.grid(row=1, column=0, pady=5, sticky="e")
        self.vehicle_id_entry = tk.Entry(main_frame, font=self.label_font, width=20)
        self.vehicle_id_entry.grid(row=1, column=1, pady=5, sticky="w")

        # Button Frame for Park Car and Park Bike buttons
        button_frame = tk.Frame(main_frame, bg="#E8F6EF")
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)

        # Park Car and Park Bike buttons, placed in button_frame to center them
        self.park_car_button = tk.Button(button_frame, text="Park Car", command=self.park_car, font=self.button_font, bg="#3498DB", fg="white", width=10)
        self.park_bike_button = tk.Button(button_frame, text="Park Bike", command=self.park_bike, font=self.button_font, bg="#E74C3C", fg="white", width=10)
        self.park_car_button.grid(row=0, column=0, padx=10, pady=5)
        self.park_bike_button.grid(row=0, column=1, padx=10, pady=5)

        # Remove vehicle button
        self.remove_button = tk.Button(main_frame, text="Remove Vehicle", command=self.remove_vehicle, font=self.button_font, bg="#C0392B", fg="white", width=20)
        self.remove_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Status display
        self.status_label = tk.Label(main_frame, text=self.get_status_text(), font=self.label_font, fg="#8E44AD", bg="#E8F6EF")
        self.status_label.grid(row=4, column=0, columnspan=2, pady=20)

    def get_status_text(self):
        # Fetch the available spots for both cars and bikes from parking_lot
        car_spots = self.parking_lot.available_spots("car")
        bike_spots = self.parking_lot.available_spots("bike")
        return f"Available Car Spots: {car_spots} | Available Bike Spots: {bike_spots}"

    def update_status(self):
        # Update the text of the status label with the latest parking status
        self.status_label.config(text=self.get_status_text())

    def park_car(self):
        self.park_vehicle("car")

    def park_bike(self):
        self.park_vehicle("bike")

    def park_vehicle(self, vehicle_type):
        vehicle_id = self.vehicle_id_entry.get().strip()
        if vehicle_id:
            # Try to park the vehicle and update the spot if successful
            spot = self.parking_lot.park_vehicle(vehicle_id, vehicle_type)
            if spot is not None:
                messagebox.showinfo("Success", f"{vehicle_type.capitalize()} {vehicle_id} parked at spot {spot}")
            else:
                messagebox.showwarning("Error", f"No available spots for {vehicle_type}s")
            self.update_status()  # Refresh the status label
            self.vehicle_id_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Enter a valid Vehicle ID")

    def remove_vehicle(self):
        vehicle_id = self.vehicle_id_entry.get().strip()
        if vehicle_id:
            # Try to remove the vehicle and update the spot if successful
            info = self.parking_lot.remove_vehicle(vehicle_id)
            if info:
                spot, vehicle_type = info
                messagebox.showinfo("Success", f"{vehicle_type.capitalize()} {vehicle_id} removed from spot {spot}")
            else:
                messagebox.showwarning("Error", "Vehicle not found")
            self.update_status()  # Refresh the status label
            self.vehicle_id_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Enter a valid Vehicle ID")
