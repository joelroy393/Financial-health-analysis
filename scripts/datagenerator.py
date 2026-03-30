import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# Set seed for reproducibility
random.seed(42)

def generate_data(num_rows=2000):
    """
    Generates two files:
    1. Finance_Actuals_v2.csv (Daily transactions)
    2. Finance_Budget_v2.csv (Monthly targets)
    """
    # Set your desired output folder here
    output_dir = r'E:\Work & studies\Power BI projects\xlsx&csv'
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 1. Setup Data Categories
    cities = {
        'Windsor': ('Ontario', 'Canada',  42.3149, -83.0364),
        'Toronto': ('Ontario', 'Canada',  43.6532, -79.3832),
        'Detroit': ('Michigan', 'United States', 42.3314, -83.0458),
        'Kitchener': ('Ontario', 'Canada', 43.4516, -80.4925),
        'Ottawa':  ('Ontario', 'Canada',  45.4215, -75.6972),
    }
    payment_modes = ['Credit Card', 'Debit Card', 'E-Transfer', 'Cash']
    
    categories = {
        'Expense': ['Rent', 'Groceries', 'Utilities', 'Dining', 'Tech', 'Transport', 'Cybersecurity', 'Entertainment', 'Healthcare'],
        'Income': ['Salary', 'Freelance', 'Investments', 'Gift']
    }

    # 2. Generate Actual Transactions
    start_date = datetime(2025, 1, 1)
    actuals_list = []

    for _ in range(num_rows):
        type_choice = random.choices(['Expense', 'Income'], weights=[0.82, 0.18])[0]
        category = random.choice(categories[type_choice])
        date = start_date + timedelta(days=random.randint(0, 450))
        
        # Logic for amounts
        if category == 'Rent':
            amount = 1200.00
        elif category == 'Salary':
            amount = round(random.uniform(2400, 2600), 2)
        else:
            amount = round(random.uniform(10, 400), 2)

        city = random.choice(list(cities.keys()))
        province, country, lat, lon = cities[city]
        actuals_list.append([
            date.strftime('%Y-%m-%d'),
            category,
            type_choice,
            amount,
            city,
            province,
            country,
            lat,
            lon,
            random.choice(payment_modes),
            f"TXN-{random.randint(100000, 999999)}"
        ])

    df_actuals = pd.DataFrame(actuals_list, columns=[
        'Date', 'Category', 'Type', 'Amount',
        'City', 'Province', 'Country', 'Latitude', 'Longitude',
        'PaymentMode', 'TransactionID'
    ])

    # 3. Generate Monthly Budget
    budget_list = []
    # Base monthly targets
    monthly_targets = {
        'Groceries': 500, 'Dining': 300, 'Utilities': 200, 
        'Tech': 150, 'Transport': 250, 'Cybersecurity': 100, 
        'Entertainment': 100, 'Healthcare': 80, 'Rent': 1200
    }

    for year in [2025, 2026]:
        for month in range(1, 13):
            for cat, target in monthly_targets.items():
                budget_list.append([f"{year}-{month:02d}-01", cat, target])

    df_budget = pd.DataFrame(budget_list, columns=['BudgetMonth', 'Category', 'BudgetAmount'])

    # 4. Save to CSV
    actuals_path = os.path.join(output_dir, "Finance_Actuals_v2.csv")
    budget_path = os.path.join(output_dir, "Finance_Budget_v2.csv")
    
    df_actuals.to_csv(actuals_path, index=False)
    df_budget.to_csv(budget_path, index=False)
    
    print("-" * 30)
    print(f"SUCCESS: Data Generated")
    print(f"Actuals: {actuals_path}")
    print(f"Budget:  {budget_path}")
    print("-" * 30)

if __name__ == "__main__":
    generate_data(2000)