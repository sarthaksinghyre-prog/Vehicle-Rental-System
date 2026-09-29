import tkinter as tk
from tkinter import ttk, messagebox

from data_manager import DataManager
from vehicle import Vehicle
from vehicle_manager import VehicleManager
from rental_manager import RentalManager
from validators import valid_price, valid_days, valid_phone
from receipt import make_receipt


class VehicleRentalApp:
    def __init__(self):
        data = DataManager()
        data.create_default_data()

        self.vehicle_manager = VehicleManager(data)
        self.rental_manager = RentalManager(self.vehicle_manager)

        self.root = tk.Tk()
        self.root.title("Vehicle Rental System")
        self.root.geometry("950x650")
        self.root.minsize(850, 580)

        self.make_window()
        self.show_vehicles()

    def make_window(self):
        tk.Label(self.root, text="VEHICLE RENTAL SYSTEM",
                 font=("Arial", 21, "bold")).pack(pady=12)

        search = tk.Frame(self.root)
        search.pack(pady=4)

        tk.Label(search, text="Search").pack(side=tk.LEFT, padx=5)
        self.search_entry = tk.Entry(search, width=32)
        self.search_entry.pack(side=tk.LEFT, padx=5)

        tk.Button(search, text="Search", command=self.search).pack(side=tk.LEFT, padx=4)
        tk.Button(search, text="Show All", command=self.show_all).pack(side=tk.LEFT, padx=4)

        table_box = tk.Frame(self.root)
        table_box.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        cols = ("ID", "Vehicle", "Type", "Price/Day", "Status")
        self.table = ttk.Treeview(table_box, columns=cols, show="headings")

        for col in cols:
            self.table.heading(col, text=col)

        self.table.column("ID", width=100)
        self.table.column("Vehicle", width=230)
        self.table.column("Type", width=130)
        self.table.column("Price/Day", width=130)
        self.table.column("Status", width=130)

        scroll = ttk.Scrollbar(table_box, orient=tk.VERTICAL,
                               command=self.table.yview)
        self.table.configure(yscrollcommand=scroll.set)
        self.table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        add_box = tk.LabelFrame(self.root, text="Add New Vehicle", padx=10, pady=10)
        add_box.pack(fill=tk.X, padx=20, pady=5)

        tk.Label(add_box, text="ID").grid(row=0, column=0, padx=4)
        self.id_entry = tk.Entry(add_box, width=12)
        self.id_entry.grid(row=0, column=1, padx=4)

        tk.Label(add_box, text="Name").grid(row=0, column=2, padx=4)
        self.name_entry = tk.Entry(add_box, width=19)
        self.name_entry.grid(row=0, column=3, padx=4)

        tk.Label(add_box, text="Type").grid(row=0, column=4, padx=4)
        self.type_entry = tk.Entry(add_box, width=12)
        self.type_entry.grid(row=0, column=5, padx=4)

        tk.Label(add_box, text="Price").grid(row=0, column=6, padx=4)
        self.price_entry = tk.Entry(add_box, width=12)
        self.price_entry.grid(row=0, column=7, padx=4)

        tk.Button(add_box, text="Add Vehicle", command=self.add_vehicle).grid(
            row=0, column=8, padx=10)

        buttons = tk.Frame(self.root)
        buttons.pack(pady=12)
        tk.Button(buttons, text="Rent Vehicle", width=16,
                  command=self.rent_vehicle).grid(row=0, column=0, padx=5)
        tk.Button(buttons, text="Return Vehicle", width=16,
                  command=self.return_vehicle).grid(row=0, column=1, padx=5)
        tk.Button(buttons, text="Remove Vehicle", width=16,
                  command=self.remove_vehicle).grid(row=0, column=2, padx=5)
        tk.Button(buttons, text="Exit", width=16,
                  command=self.root.destroy).grid(row=0, column=3, padx=5)

    def show_vehicles(self, vehicles=None):
        for row in self.table.get_children():
            self.table.delete(row)

        if vehicles is None:
            vehicles = self.vehicle_manager.vehicles

        for v in vehicles:
            status = "Available" if v.available else "Rented"
            self.table.insert("", tk.END, values=(
                v.vehicle_id, v.name, v.vehicle_type,
                "Rs. %.2f" % v.price, status
            ))

    def selected_vehicle(self):
        item = self.table.selection()
        if not item:
            messagebox.showwarning("Select Vehicle", "Please select a vehicle first.")
            return None

        values = self.table.item(item[0], "values")
        return self.vehicle_manager.find_vehicle(values[0])

    def add_vehicle(self):
        vehicle_id = self.id_entry.get().strip()
        name = self.name_entry.get().strip()
        vehicle_type = self.type_entry.get().strip()
        price = self.price_entry.get().strip()

        if not vehicle_id or not name or not vehicle_type:
            messagebox.showerror("Error", "Please fill all vehicle details.")
            return
        if not valid_price(price):
            messagebox.showerror("Error", "Enter a valid price.")
            return

        vehicle = Vehicle(vehicle_id, name, vehicle_type, float(price))
        ok, msg = self.vehicle_manager.add_vehicle(vehicle)

        if ok:
            self.clear_form()
            self.show_vehicles()
            messagebox.showinfo("Done", msg)
        else:
            messagebox.showerror("Error", msg)

    def clear_form(self):
        for box in (self.id_entry, self.name_entry,
                    self.type_entry, self.price_entry):
            box.delete(0, tk.END)

    def search(self):
        text = self.search_entry.get()
        self.show_vehicles(self.vehicle_manager.search(text))

    def show_all(self):
        self.search_entry.delete(0, tk.END)
        self.show_vehicles()

    def rent_vehicle(self):
        vehicle = self.selected_vehicle()
        if vehicle is None:
            return
        if not vehicle.available:
            messagebox.showwarning("Not Available", "This vehicle is already rented.")
            return

        win = tk.Toplevel(self.root)
        win.title("Rent Vehicle")
        win.geometry("390x320")
        win.resizable(False, False)

        tk.Label(win, text="Customer Details", font=("Arial", 16, "bold")).pack(pady=12)
        form = tk.Frame(win)
        form.pack()

        tk.Label(form, text="Name").grid(row=0, column=0, pady=8)
        name = tk.Entry(form, width=25)
        name.grid(row=0, column=1, pady=8)

        tk.Label(form, text="Phone").grid(row=1, column=0, pady=8)
        phone = tk.Entry(form, width=25)
        phone.grid(row=1, column=1, pady=8)

        tk.Label(form, text="Days").grid(row=2, column=0, pady=8)
        days = tk.Entry(form, width=25)
        days.grid(row=2, column=1, pady=8)

        def finish():
            customer = name.get().strip()
            phone_no = phone.get().strip()
            day_text = days.get().strip()

            if not customer or not valid_phone(phone_no):
                messagebox.showerror("Error", "Enter a name and valid phone number.", parent=win)
                return
            if not valid_days(day_text):
                messagebox.showerror("Error", "Days should be a whole number above 0.", parent=win)
                return

            ok, msg, bill = self.rental_manager.rent_vehicle(
                vehicle.vehicle_id, customer, phone_no, int(day_text))

            if ok:
                win.destroy()
                self.show_vehicles()
                messagebox.showinfo("Rental Receipt", make_receipt(bill))
            else:
                messagebox.showerror("Error", msg, parent=win)

        tk.Button(win, text="Complete Rental", width=20, command=finish).pack(pady=15)

    def return_vehicle(self):
        vehicle = self.selected_vehicle()
        if vehicle is None:
            return

        ok, msg = self.rental_manager.return_vehicle(vehicle.vehicle_id)
        if ok:
            self.show_vehicles()
            messagebox.showinfo("Returned", msg)
        else:
            messagebox.showwarning("Warning", msg)

    def remove_vehicle(self):
        vehicle = self.selected_vehicle()
        if vehicle is None:
            return

        if not messagebox.askyesno("Remove Vehicle", "Remove " + vehicle.name + "?"):
            return

        ok, msg = self.vehicle_manager.remove_vehicle(vehicle.vehicle_id)
        if ok:
            self.show_vehicles()
            messagebox.showinfo("Done", msg)
        else:
            messagebox.showerror("Error", msg)

    def run(self):
        self.root.mainloop()
