from tkinter import Tk
from database import Database
from parking_lot import ParkingLot
from gui import ParkingGUI
import tkinter as tk
from tkinter import Toplevel, font


def show_parked_vehicles(root, parking_lot):
    # Create a new window to show parked vehicle details
    vehicle_window = Toplevel(root)
    vehicle_window.title("Parked Vehicles")
    vehicle_window.geometry("300x300")
    vehicle_window.configure(bg="#F2F4F4")

    # Define font for title and labels
    title_font = font.Font(family="Helvetica", size=16, weight="bold")
    label_font = font.Font(family="Helvetica", size=12)

    # Title for the window
    title = tk.Label(vehicle_window, text="Parked Vehicles", font=title_font, fg="#34495E", bg="#F2F4F4")
    title.pack(pady=10)

    # Get all parked vehicles and their spots
    vehicles = parking_lot.db.get_all_vehicles()

    # Display each vehicle and its parking spot
    if vehicles:
        for vehicle_id, spot_id in vehicles.items():
            vehicle_label = tk.Label(vehicle_window, text=f"Vehicle ID: {vehicle_id} - Spot: {spot_id}",
                                     font=label_font, fg="#2C3E50", bg="#F2F4F4")
            vehicle_label.pack(pady=2)
    else:
        no_vehicles_label = tk.Label(vehicle_window, text="No vehicles currently parked.", font=label_font,
                                     fg="#7F8C8D", bg="#F2F4F4")
        no_vehicles_label.pack(pady=10)


def main():
    # Initialize app components
    root = Tk()
    db = Database()
    parking_lot = ParkingLot(db)
    app = ParkingGUI(root, parking_lot)

    # Add Show Parked Vehicles button
    show_vehicles_button = tk.Button(root, text="Show Parked Vehicles",
                                     command=lambda: show_parked_vehicles(root, parking_lot),
                                     font=("Helvetica", 12, "bold"), bg="#3498DB", fg="white", width=20)
    show_vehicles_button.pack(pady=50)

    # Start the Tkinter loop
    root.mainloop()


if __name__ == "__main__":
    main()
