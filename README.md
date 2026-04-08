# Student Budget Optimizer 📊

## Project Description
A Python-based financial tool designed to help students track their income (scholarships/jobs) and expenses. It provides a visual dashboard to categorize spending and alerts the user if they are overspending.

## Requirements & Setup
1. **Python 3.x** installed.
2. **Install External Library:** `python3 -m pip install tabulate`
3. **Run the application:**
   `python3 calculatorstudent.py`

## Main Features
* **Detailed Registration:** Input for income/expense categories and amounts.
* **Data Persistence:** Automatically saves data to a `budget_data.csv` file.
* **Smart Dashboard:** Uses the `tabulate` library to display a grid of all transactions.
* **Overspending Alerts:** Visual warnings when the balance becomes negative.
* **Reset Function:** Easy one-click database cleanup.

## Technical Decisions
* **GUI:** Built with `tkinter` for accessibility.
* **Storage:** CSV format was chosen for lightweight persistence and compatibility with Excel.
* **Library:** `tabulate` was chosen to maintain a clean, readable UI in the dashboard.
