# Python Pharmacy Management System

A desktop-based Pharmacy Management System built with Python, using Tkinter for the graphical user interface (GUI) and SQLite for local database storage. This application helps manage medicine inventory and process sales efficiently.

## Features

*   **Inventory Management**:
    *   Add new medicines with details like name, manufacturer, quantity, and price.
    *   View a complete list of all medicines in stock.
    *   Stock levels are automatically updated after each sale.
*   **Billing System**:
    *   Process sales by selecting a medicine ID and quantity.
    *   Validates against available stock to prevent overselling.
    *   Records all sales transactions for future reference (feature can be extended).
*   **User-Friendly Interface**: A clean, tabbed interface for easy navigation between inventory and billing modules.
*   **Local Database**: Uses SQLite to create a persistent, file-based database (`pharmacy.db`) in the project directory.

## Prerequisites

*   **Python 3.x**: Ensure you have Python 3 installed. You can get it from [python.org](https://www.python.org/downloads/).

The required libraries (`tkinter` and `sqlite3`) are part of the Python standard library, so no additional installations are needed.

## How to Install and Run

1.  **Create a Project Folder**:
    ```bash
    mkdir pharmacy_management
    cd pharmacy_management
    ```

2.  **Create Project Files**:
    Inside the `pharmacy_management` directory, create the following three files:
    *   `main.py`
    *   `database.py`
    *   `gui.py`

3.  **Add the Code**:
    Copy and paste the provided code into the corresponding files.

4.  **Run the Application**:
    Open a terminal or command prompt, navigate to your project directory, and execute the `main.py` script:
    ```bash
    python main.py
    ```
    The application window will open. A database file named `pharmacy.db` will be automatically created in the folder on the first run.

## How to Use the System

The application has two main tabs:

### 1. Inventory Management Tab

*   **Add a Medicine**:
    *   Fill in the "Name", "Manufacturer", "Quantity", and "Price/Unit" fields in the "Add New Medicine" section.
    *   Click the "Add Medicine" button.
*   **View Stock**:
    *   The "Current Stock" table displays all medicines in the inventory.
    *   Note the **Med ID** from this table, as it is required for making a sale.
    *   Click "Refresh Stock List" to see the latest inventory data.

### 2. Process Sale / Billing Tab

*   **Make a Sale**:
    *   Enter the **Medicine ID** of the item you wish to sell (you can find this in the inventory tab).
    *   Enter the desired **Quantity to Sell**.
    *   Click the "Process Sale" button.
    *   If the sale is successful, the stock in the inventory will be automatically reduced. You can verify this by checking the "Inventory Management" tab again.

## Project File Structure
