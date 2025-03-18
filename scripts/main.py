# main.py
# Main script to process ID data and output formatted SQL queries.
# python scripts/main.py --file sample.csv --idtype whkey
# python scripts/main.py --file sample.xlsx --idtype pidm

import os
import argparse
import pandas as pd
from scripts.utils import break_up_pidms, break_up_whkeys, break_up_pantherids

# Set paths
UPLOADS_DIR = "uploads"
OUTPUTS_DIR = "outputs"

# Ensure outputs directory exists
os.makedirs(OUTPUTS_DIR, exist_ok=True)

def process_file(input_file, id_type):
    """
    Determines which function to call based on the ID type (pidm, whkey, pantherid).
    
    :param input_file: Path to the input CSV or Excel file.
    :param id_type: The ID type to process (pidm, whkey, pantherid).
    """
    # Construct output file path
    output_txt = os.path.join(OUTPUTS_DIR, f"{id_type}_output.txt")
    
    # Check file type
    if input_file.endswith(".csv"):
        df = pd.read_csv(input_file)
    elif input_file.endswith(".xlsx"):
        df = pd.read_excel(input_file)
    else:
        print("Error: Unsupported file format. Use .csv or .xlsx.")
        return

    # Validate if the necessary column exists
    if id_type.upper() not in df.columns:
        print(f"Error: Column '{id_type.upper()}' not found in the file.")
        return
    
    # Call the appropriate function
    if id_type == "pidm":
        break_up_pidms(input_file, output_txt)
    elif id_type == "whkey":
        break_up_whkeys(input_file, output_txt)
    elif id_type == "pantherid":
        break_up_pantherids(input_file, output_txt)
    else:
        print("Error: Invalid ID type. Choose from 'pidm', 'whkey', or 'pantherid'.")

if __name__ == "__main__":
    # Setup argument parser
    parser = argparse.ArgumentParser(description="Process ID data and output formatted SQL queries.")
    parser.add_argument("--file", required=True, help="The name of the input CSV/Excel file located in /uploads.")
    parser.add_argument("--idtype", required=True, choices=["pidm", "whkey", "pantherid"], help="The type of ID to process.")
    
    args = parser.parse_args()
    
    # Construct input file path
    input_file_path = os.path.join(UPLOADS_DIR, args.file)

    # Check if file exists
    if not os.path.exists(input_file_path):
        print(f"Error: File '{args.file}' not found in /uploads.")
    else:
        process_file(input_file_path, args.idtype)
        print(f"Output saved to /outputs/{args.idtype}_output.txt")

