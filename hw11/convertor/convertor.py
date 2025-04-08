import pandas as pd
import os

def csv_to_xlsx(csv_file, xlsx_file=None):
    df = pd.read_csv(csv_file)
    if not xlsx_file:
        xlsx_file = os.path.splitext(csv_file)[0] + ".xlsx"
    df.to_excel(xlsx_file, index=False, engine='openpyxl')
    print(f"✅ CSV успішно конвертовано у XLSX: {xlsx_file}")

def xlsx_to_csv(xlsx_file, csv_file=None):
    df = pd.read_excel(xlsx_file, engine='openpyxl')
    if not csv_file:
        csv_file = os.path.splitext(xlsx_file)[0] + ".csv"
    df.to_csv(csv_file, index=False)
    print(f"✅ XLSX успішно конвертовано у CSV: {csv_file}")

if __name__ == "__main__":
    # використовуй одну з них, залежно від типу файлу:
    # csv_to_xlsx("example.csv")
    xlsx_to_csv("example.xlsx")
