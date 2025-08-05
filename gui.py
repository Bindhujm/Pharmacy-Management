import tkinter as tk
from tkinter import ttk, messagebox
import database
from datetime import datetime

class CourierApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Courier Management System")
        self.geometry("800x600")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, padx=10, fill="both", expand=True)

        self.create_add_order_tab()
        self.create_view_orders_tab()
        self.create_track_order_tab()
        self.create_update_status_tab()

    def create_add_order_tab(self):
        add_order_frame = ttk.Frame(self.notebook)
        self.notebook.add(add_order_frame, text="Add Order")

        ttk.Label(add_order_frame, text="Sender Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.sender_name_entry = ttk.Entry(add_order_frame, width=40)
        self.sender_name_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(add_order_frame, text="Receiver Name:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.receiver_name_entry = ttk.Entry(add_order_frame, width=40)
        self.receiver_name_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(add_order_frame, text="Pickup Address:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.pickup_address_entry = ttk.Entry(add_order_frame, width=40)
        self.pickup_address_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(add_order_frame, text="Delivery Address:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.delivery_address_entry = ttk.Entry(add_order_frame, width=40)
        self.delivery_address_entry.grid(row=3, column=1, padx=10, pady=5)

        add_button = ttk.Button(add_order_frame, text="Add Order", command=self.add_order)
        add_button.grid(row=4, column=0, columnspan=2, pady=20)

    def create_view_orders_tab(self):
        view_orders_frame = ttk.Frame(self.notebook)
        self.notebook.add(view_orders_frame, text="View All Orders")

        self.tree = ttk.Treeview(view_orders_frame, columns=("ID", "Sender", "Receiver", "Pickup", "Delivery", "Status", "Date"), show="headings")
        self.tree.heading("ID", text="Order ID")
        self.tree.heading("Sender", text="Sender Name")
        self.tree.heading("Receiver", text="Receiver Name")
        self.tree.heading("Pickup", text="Pickup Address")
        self.tree.heading("Delivery", text="Delivery Address")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Date", text="Date Created")
        self.tree.pack(fill="both", expand=True)

        refresh_button = ttk.Button(view_orders_frame, text="Refresh", command=self.populate_orders)
        refresh_button.pack(pady=10)
        self.populate_orders()

    def create_track_order_tab(self):
        track_order_frame = ttk.Frame(self.notebook)
        self.notebook.add(track_order_frame, text="Track Order")

        ttk.Label(track_order_frame, text="Enter Order ID:").pack(pady=10)
        self.track_id_entry = ttk.Entry(track_order_frame)
        self.track_id_entry.pack(pady=5)
        track_button = ttk.Button(track_order_frame, text="Track", command=self.track_order)
        track_button.pack(pady=10)

        self.track_result = ttk.Label(track_order_frame, text="", font=("Helvetica", 12))
        self.track_result.pack(pady=20)

    def create_update_status_tab(self):
        update_status_frame = ttk.Frame(self.notebook)
        self.notebook.add(update_status_frame, text="Update Status")

        ttk.Label(update_status_frame, text="Order ID:").pack(pady=10)
        self.update_id_entry = ttk.Entry(update_status_frame)
        self.update_id_entry.pack(pady=5)

        ttk.Label(update_status_frame, text="New Status:").pack(pady=10)
        self.status_var = tk.StringVar()
        status_options = ["Booked", "Picked Up", "In Transit", "Delivered"]
        self.status_dropdown = ttk.Combobox(update_status_frame, textvariable=self.status_var, values=status_options, state="readonly")
        self.status_dropdown.pack(pady=5)
        self.status_dropdown.set("Booked")

        update_button = ttk.Button(update_status_frame, text="Update Status", command=self.update_status)
        update_button.pack(pady=20)


    def add_order(self):
        sender = self.sender_name_entry.get()
        receiver = self.receiver_name_entry.get()
        pickup = self.pickup_address_entry.get()
        delivery = self.delivery_address_entry.get()
        status = "Booked"
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if sender and receiver and pickup and delivery:
            order_data = (sender, receiver, pickup, delivery, status, date)
            database.add_order(order_data)
            self.clear_add_order_fields()
            self.populate_orders()
        else:
            messagebox.showwarning("Input Error", "All fields are required.")

    def clear_add_order_fields(self):
        self.sender_name_entry.delete(0, tk.END)
        self.receiver_name_entry.delete(0, tk.END)
        self.pickup_address_entry.delete(0, tk.END)
        self.delivery_address_entry.delete(0, tk.END)

    def populate_orders(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        orders = database.get_all_orders()
        for order in orders:
            self.tree.insert("", "end", values=order)

    def track_order(self):
        order_id = self.track_id_entry.get()
        if order_id:
            order = database.get_order_by_id(order_id)
            if order:
                result_text = f"Order ID: {order[0]}\n" \
                              f"Sender: {order[1]}\n" \
                              f"Receiver: {order[2]}\n" \
                              f"Status: {order[5]}"
                self.track_result.config(text=result_text)
            else:
                messagebox.showinfo("Not Found", "Order ID not found.")
        else:
            messagebox.showwarning("Input Error", "Please enter an Order ID.")

    def update_status(self):
        order_id = self.update_id_entry.get()
        new_status = self.status_var.get()
        if order_id and new_status:
            database.update_order_status(order_id, new_status)
            self.populate_orders()
            self.update_id_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please provide both Order ID and a new status.")