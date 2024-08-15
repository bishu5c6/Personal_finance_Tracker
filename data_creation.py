import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_descriptipn


class CSV:
    CSV_FILE = "finance_data.csv1"
    COLUMNS = ["date","amount","category","description"]
    
    @classmethod#it will use the class method does not interact with object methods
    def intialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns = cls.COLUMNS)#columns that i want to insert
            df.to_csv(cls.CSV_FILE,index=False)
            
    @classmethod #now we will try to add some eminties to the folder
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully")
            
            
CSV.intialize_csv()
CSV.add_entry("15-08-2024", 20000, "Medical", "Successfully completed")