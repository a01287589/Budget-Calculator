import csv
import os
import tkinter as tk
from tkinter import messagebox, ttk
from tabulate import tabulate # External library for formatting

DATA_FILE = "budget_data.csv"

def initialize_file():
    """Ensures the CSV storage exists with proper headers."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Type", "Category", "Amount"])

def save_transaction(t_type, cat, amt):
    """Writes data to CSV for persistence."""
    with open(DATA_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([t_type, cat, amt])

def get_all_data():
    """Retrieves all rows and calculates totals."""
    total_income = 0
    total_expenses = 0
    rows = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    amt = float(row['Amount'])
                    rows.append([row['Type'], row['Category'], f"${amt:.2f}"])
                    if row['Type'] == 'Income':
                        total_income += amt
                    else:
                        total_expenses += amt
                except (ValueError, KeyError):
                    continue 
    return total_income, total_expenses, rows

class BudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Budget Optimizer v2.0")
        self.root.geometry("400x550")
        
        # UI Elements
        tk.Label(root, text="Student Budget Optimizer", font=("Arial", 16, "bold")).pack(pady=20)
        
        tk.Label(root, text="Category/Source:").pack()
        self.entry_cat = tk.Entry(root)
        self.entry_cat.pack(pady=5)
        
        tk.Label(root, text="Amount ($):").pack()
        self.entry_amt = tk.Entry(root)
        self.entry_amt.pack(pady=5)
        
        # Action Buttons
        ttk.Button(root, text="Add Income", command=lambda: self.add("Income")).pack(pady=5)
        ttk.Button(root, text="Add Expense", command=lambda: self.add("Expense")).pack(pady=5)
        ttk.Button(root, text="Show Detailed Dashboard", command=self.display_stats).pack(pady=15)
        ttk.Button(root, text="Reset All Data", command=self.reset_data).pack(pady=20)

    def add(self, t_type):
        """Input validation and saving."""
        cat = self.entry_cat.get()
        amt = self.entry_amt.get()
        if not cat or not amt:
            messagebox.showwarning("Error", "Fill all fields")
            return
        try:
            save_transaction(t_type, cat, float(amt))
            messagebox.showinfo("Success", f"{t_type} added!")
            self.entry_cat.delete(0, tk.END)
            self.entry_amt.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")

    def display_stats(self):
        """Displays the detailed category list and totals[cite: 67, 68]."""
        inc, exp, rows = get_all_data()
        bal = inc - exp
        
        # Create a detailed string table using tabulate
        table_str = tabulate(rows, headers=["Type", "Category", "Amount"], tablefmt="grid")
        
        summary = f"\nSummary:\nIncomes: ${inc:.2f}\nExpenses: ${exp:.2f}\nBalance: ${bal:.2f}"
        if bal < 0: summary += "\n⚠️ ALERT: Overspending!"

        # Show in a new window to handle size
        dash_window = tk.Toplevel(self.root)
        dash_window.title("Detailed Dashboard")
        text_area = tk.Text(dash_window, height=20, width=50)
        text_area.insert(tk.END, table_str + "\n" + summary)
        text_area.config(state=tk.DISABLED) # Read only
        text_area.pack(padx=10, pady=10)

    def reset_data(self):
        if messagebox.askyesno("Confirm", "Delete all data?"):
            if os.path.exists(DATA_FILE): os.remove(DATA_FILE)
            initialize_file()
            messagebox.showinfo("Reset", "Data cleared")

if __name__ == "__main__":
    initialize_file()
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()