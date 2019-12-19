"""
merge_excel.py

practice merging excel files
"""
# Imports
import os
import pandas as pd

# List Files
path = os.getcwd()
files = os.listdir(path)
files_xls = [f for f in files if f[-4:]=='xlsx']

# Initialize Empty dataframe
df = pd.DataFrame()
for f in files_xls:
    data = pd.read_excel(f,'Sheet1')
    df = df.append(data)
df.to_excel("test_combined_OH_Inventory3.xlsx")