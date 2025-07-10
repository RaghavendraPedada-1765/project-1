import tkinter as tk
from tkinter import ttk, messagebox

# Mocked exchange rates (relative to USD)
EXCHANGE_RATES = {
    'USD': 1.0,
    'EUR': 0.93,
    'INR': 83.5,
    'GBP': 0.79,
    'JPY': 157.1,
    'AUD': 1.52,
    'CAD': 1.37
}

CURRENCIES = list(EXCHANGE_RATES.keys())

def convert_currency(amount, source, target):
    """Convert amount from source to target currency."""
    try:
        usd_amount = float(amount) / EXCHANGE_RATES[source]
        converted = usd_amount * EXCHANGE_RATES[target]
        return round(converted, 2)
    except Exception:
        return None

# CLI version
def cli_app():
    print("Currency Converter CLI")
    print("Supported currencies:", ', '.join(CURRENCIES))
    amount = input("Enter amount: ")
    source = input("Enter source currency (e.g., USD): ").upper()
    target = input("Enter target currency (e.g., EUR): ").upper()
    if source not in EXCHANGE_RATES or target not in EXCHANGE_RATES:
        print("Unsupported currency.")
        return
    result = convert_currency(amount, source, target)
    if result is not None:
        print(f"{amount} {source} = {result} {target}")
    else:
        print("Error in conversion. Please check your input.")

# Tkinter GUI version (optional)
class CurrencyConverterGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Currency Converter")
        self.geometry("350x200")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Amount:").grid(row=0, column=0, padx=10, pady=10)
        self.amount_var = tk.StringVar()
        tk.Entry(self, textvariable=self.amount_var).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self, text="From:").grid(row=1, column=0, padx=10, pady=10)
        self.source_var = tk.StringVar(value=CURRENCIES[0])
        ttk.Combobox(self, textvariable=self.source_var, values=CURRENCIES, state='readonly').grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self, text="To:").grid(row=2, column=0, padx=10, pady=10)
        self.target_var = tk.StringVar(value=CURRENCIES[1])
        ttk.Combobox(self, textvariable=self.target_var, values=CURRENCIES, state='readonly').grid(row=2, column=1, padx=10, pady=10)

        tk.Button(self, text="Convert", command=self.do_convert).grid(row=3, column=0, columnspan=2, pady=15)

        self.result_label = tk.Label(self, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def do_convert(self):
        amount = self.amount_var.get()
        source = self.source_var.get()
        target = self.target_var.get()
        if source == target:
            messagebox.showinfo("Info", "Source and target currencies are the same.")
            return
        try:
            result = convert_currency(amount, source, target)
            if result is not None:
                self.result_label.config(text=f"{amount} {source} = {result} {target}")
            else:
                self.result_label.config(text="Error: Invalid input")
        except Exception as e:
            self.result_label.config(text=f"Error: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "cli":
        cli_app()
    else:
        app = CurrencyConverterGUI()
        app.mainloop()
