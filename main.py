import database
from gui import CourierApp

if __name__ == "__main__":
    database.create_table()
    app = CourierApp()
    app.mainloop()