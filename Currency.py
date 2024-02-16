import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta
from ttkthemes import ThemedStyle
import config

API_KEY = config.api_key

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("800x600")
        self.root.resizable(True, True)

        # Apply modern theme
        style = ThemedStyle(self.root)
        style.set_theme("equilux")

        # Create menu bar
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

        # Add menu options
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menubar.add_cascade(label="File", menu=self.file_menu)

        self.data_menu = tk.Menu(self.menubar, tearoff=0)
        self.data_menu.add_command(label="Standard", command=self.fetch_standard_data)
        self.data_menu.add_command(label="Pair", command=self.fetch_pair_data)
        self.data_menu.add_command(label="Enriched", command=self.fetch_enriched_data)
        self.data_menu.add_command(label="Historical", command=self.fetch_historical_data)
        self.data_menu.add_command(label="Supported Codes", command=self.fetch_supported_codes)
        self.menubar.add_cascade(label="Data", menu=self.data_menu)

        # Create main frame
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Base currency dropdown
        self.base_currency_label = ttk.Label(self.main_frame, text="Base Currency:")
        self.base_currency_label.grid(row=0, column=0, padx=10, pady=5)
        self.base_currency_var = tk.StringVar()
        self.base_currency_dropdown = ttk.Combobox(self.main_frame, textvariable=self.base_currency_var)
        self.base_currency_dropdown.grid(row=0, column=1, padx=10, pady=5)

        # Target currency dropdown
        self.target_currency_label = ttk.Label(self.main_frame, text="Target Currency:")
        self.target_currency_label.grid(row=1, column=0, padx=10, pady=5)
        self.target_currency_var = tk.StringVar()
        self.target_currency_dropdown = ttk.Combobox(self.main_frame, textvariable=self.target_currency_var)
        self.target_currency_dropdown.grid(row=1, column=1, padx=10, pady=5)

        # Amount entry
        self.amount_label = ttk.Label(self.main_frame, text="Amount:")
        self.amount_label.grid(row=2, column=0, padx=10, pady=5)
        self.amount_entry = ttk.Entry(self.main_frame)
        self.amount_entry.grid(row=2, column=1, padx=10, pady=5)

        # Convert button
        self.convert_button = ttk.Button(self.main_frame, text="Convert", command=self.convert_currency)
        self.convert_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Result label
        self.result_label = ttk.Label(self.main_frame, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

        # Graph frame
        self.graph_frame = ttk.Frame(self.main_frame)
        self.graph_frame.grid(row=5, column=0, columnspan=2, pady=10)

        # Initialize base currency and target currency dropdowns
        self.fetch_supported_codes()

    def fetch_supported_codes(self):
        # Make API call to fetch supported currency codes
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/codes"
        response = requests.get(url)
        data = response.json()

        if data['result'] == 'success':
            supported_codes = [currency_info[0] for currency_info in data['supported_codes']]
            self.base_currency_dropdown['values'] = supported_codes
            self.target_currency_dropdown['values'] = supported_codes
        else:
            messagebox.showerror("Error", "Failed to fetch supported codes")

    def fetch_standard_data(self):
        # Placeholder for fetching standard data
        messagebox.showinfo("Standard Data", "Fetching standard data...")

    def fetch_pair_data(self):
        # Placeholder for fetching pair data
        messagebox.showinfo("Pair Data", "Fetching pair data...")

    def fetch_enriched_data(self):
        # Placeholder for fetching enriched data
        messagebox.showinfo("Enriched Data", "Fetching enriched data...")

    def fetch_historical_data(self):
        # Placeholder for fetching historical data
        messagebox.showinfo("Historical Data", "Fetching historical data...")

    def convert_currency(self):
        base_currency = self.base_currency_var.get()
        target_currency = self.target_currency_var.get()
        amount = self.amount_entry.get()

    # Make API call to fetch exchange rate
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{base_currency}/{target_currency}"
        response = requests.get(url)
        data = response.json()

        if data['result'] == 'success':
            exchange_rate = data['conversion_rate']
            converted_amount = float(amount) * exchange_rate
            self.result_label.config(text=f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
        else:
            messagebox.showerror("Error", "Failed to fetch exchange rate")


if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
