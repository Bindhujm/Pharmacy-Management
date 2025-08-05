import sqlite3
from tkinter import messagebox

def connect():
    """Connect to the SQLite database and return the connection and cursor."""
    try:
        conn = sqlite3.connect("courier.db")
        cursor = conn.cursor()
        return conn, cursor
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Error connecting to database: {e}")
        return None, None

def create_table():
    """Create the orders table if it doesn't exist."""
    conn, cursor = connect()
    if conn:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS orders (
                    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sender_name TEXT NOT NULL,
                    receiver_name TEXT NOT NULL,
                    pickup_address TEXT NOT NULL,
                    delivery_address TEXT NOT NULL,
                    status TEXT NOT NULL,
                    date_created TEXT NOT NULL
                )
            """)
            conn.commit()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error creating table: {e}")
        finally:
            conn.close()

def add_order(order_data):
    """Add a new order to the database."""
    conn, cursor = connect()
    if conn:
        try:
            cursor.execute("""
                INSERT INTO orders (sender_name, receiver_name, pickup_address, delivery_address, status, date_created)
                VALUES (?, ?, ?, ?, ?, ?)
            """, order_data)
            conn.commit()
            messagebox.showinfo("Success", "Order added successfully!")
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error adding order: {e}")
        finally:
            conn.close()

def get_all_orders():
    """Retrieve all orders from the database."""
    conn, cursor = connect()
    if conn:
        try:
            cursor.execute("SELECT * FROM orders")
            orders = cursor.fetchall()
            return orders
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error fetching orders: {e}")
            return []
        finally:
            conn.close()

def get_order_by_id(order_id):
    """Retrieve a single order by its ID."""
    conn, cursor = connect()
    if conn:
        try:
            cursor.execute("SELECT * FROM orders WHERE order_id=?", (order_id,))
            order = cursor.fetchone()
            return order
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error fetching order: {e}")
            return None
        finally:
            conn.close()

def update_order_status(order_id, new_status):
    """Update the status of an existing order."""
    conn, cursor = connect()
    if conn:
        try:
            cursor.execute("UPDATE orders SET status=? WHERE order_id=?", (new_status, order_id))
            conn.commit()
            messagebox.showinfo("Success", "Order status updated successfully!")
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error updating order status: {e}")
        finally:
            conn.close()